from fastapi import Request
# from starlette.responses import RedirectResponse
# from Scripts.constants.app_configuration import collection
from Scripts.core.db.mongo_utility import mongo
from schemas.models import User
from Scripts.core.logging.logs.logger import logging
from fastapi.templating import Jinja2Templates

Templates = Jinja2Templates(directory="Templates")


async def signup(request: Request):
    return Templates.TemplateResponse("SignUp.html", {"request": request})


async def login(request: Request):
    return Templates.TemplateResponse("Login.html", {"request": request})


async def add(request: Request):
    return Templates.TemplateResponse("add_books.html", {"request": request})


async def delete(request: Request):
    return Templates.TemplateResponse("delete_book.html", {"request": request})


async def update(request: Request):
    return Templates.TemplateResponse("update_book.html", {"request": request})


# async def display_1(request: Request):
#     return Templates.TemplateResponse("disp.html", {"request": request})
#

async def user_signup(request: Request):
    try:
        temp_var = await request.form()
        user = User(
            username=temp_var["username"],
            password=temp_var["password"],
            email=temp_var["email"]
        )
        if user:
            result = mongo.for_sign_insert_one("Sanket_library_management", user)
            logging.info("SignUp success")
            return Templates.TemplateResponse("Login.html", {"request": request})
        else:
            return {"None"}
    except Exception as e:
        return {"error:", str(e)}


async def user_login(request: Request):
    try:
        data = await request.form()
        username = data["username"]
        password = data["password"]
        find_username = {"username": username}
        find_password = {"password": password}
        user_username = mongo.for_find_one("Sanket_library_management", find_username)
        user_password = mongo.for_find_one("Sanket_library_management", find_password)
        if user_username:
            if user_password:
                logging.info("login Success")
                return Templates.TemplateResponse("add_books.html", {"request": request})
            else:
                logging.error("login failed")
                return {"***You entered wrong password***"}
        else:
            logging.warning("enter correct user name or create account")
            return {"***Enter correct user name or create account***"}
    except Exception as e:
        return {"error:", str(e)}


async def add_book(request: Request):
    try:
        data = await request.form()
        book_id = data["book_id"]
        book_name = data["book_name"]
        author = data["author"]
        book = {"book_name": book_name}
        user = mongo.for_find_one("Sanket_library_management", book)
        if user:
            logging.warning("It is already there")
            return {"Book is already exist"}
        else:
            details = {"book_id": book_id, "book_name": book_name, "author": author}
            adding = mongo.for_insert_one("Sanket_library_management", details)
            if adding:
                logging.info("Book Added")
                return {"Added successfully"}
            else:
                logging.error("Something wrong")
                return {"Check something is wrong"}
    except Exception as e:
        return {"error:", str(e)}


async def books_delete(request: Request):
    try:
        data = await request.form()
        book_id = data["book_id"]
        book_name = data["book_name"]
        author = data["author"]
        delete_name = {"book_id": book_id, "book_name": book_name, "author": author}
        user = mongo.for_find_one("Sanket_library_management", delete_name)
        if user:
            delete_detail = {"book_id": book_id}
            mongo.for_delete_one("Sanket_library_management", delete_detail)
            logging.info("delete success")
            return {"Book details deleted successfully"}
        else:
            logging.info("Its not available")
            return {"Book is not there"}
    except Exception as e:
        return {"error:", str(e)}
    # else:
    #     logging.warning("Check book id and name")
    #     return {"WARNING:book details not found"}


async def books_update(request: Request):
    try:
        data = await request.form()
        book_id = data["book_id"]
        book_name = data["book_name"]
        find_book_id = {"book_id": book_id}
        set_det = {"$set": {"book_name": book_name}}
        user = mongo.for_find_one("Sanket_library_management", find_book_id)
        # user = mongo.for_update_one("Sanket_library_management", update_details, set_det)
        if user:
            mongo.for_update_one("Sanket_library_management", find_book_id, set_det)
            logging.info("UPDATED SUCCESSFULLY")
            return {"updated successfully"}
        else:
            logging.warning("Check id")
            return {"WARNING:Failed to Update, check book id"}
    except Exception as e:
        return {"error", str(e)}

# async def display(request: Request):
#     data = await request.form()
# book_id = data["book_id"]
# book_name = collection.find_one(data["book_name"])
# author = data["author"]
# user = collection.find_many({"book_id": book_id, "book_name": book_name, "author": author})
# # books = collection.find_one({"document_type": "book_name"})
# if user:
#     return Templates.TemplateResponse("disp.html", {"request": request})
# else:
#     return 0
# user = collection.find_one()
# for all_books in user:
#     return all_books
