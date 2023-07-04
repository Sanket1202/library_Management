from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import uvicorn


app = FastAPI()


mongodb_url = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
client = MongoClient(mongodb_url)
db = client["todo_app"]
tasks_collection = db["tasks"]
users_collection = db["usersc"]


class User(BaseModel):
    username: str
    password: str


class Task(BaseModel):
    id: int
    title: str
    description: str
    user_id: int


@app.post("/signup")
def signup(user: User):
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    users_collection.insert_one(user.dict())
    return {"message": "User created successfully"}


@app.post("/login")
def login(username: str, password: str):
    user = users_collection.find_one({"username": username, "password": password})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful"}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks_collection.find_one({"id": task_id})

    if not task or task["user_id"] != 1:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.get("/tasks")
def get_tasks():
    tasks = tasks_collection.find({"user_id": 1})
    return list(tasks)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    existing_task = tasks_collection.find_one({"id": task_id})

    if existing_task:
        updated_task = task.dict()
        tasks_collection.update_one({"id": task_id}, {"$set": updated_task})
        return {"message": f"Task {task_id} updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = tasks_collection.find_one({"id": task_id})

    if not task or task["user_id"] != 1:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_collection.delete_one({"id": task_id})
    return {"message": f"Task {task_id} deleted"}


if __name__ == "__main__":
    uvicorn.run("Sample:app", host="127.0.0.1", port=5000)
