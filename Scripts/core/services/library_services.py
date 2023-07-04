from fastapi import Request, APIRouter
from fastapi import FastAPI
from Scripts.core.handler.library_handler import signup, login, add, delete, update
from Scripts.core.handler.library_handler import user_signup, user_login, add_book, books_delete, books_update
from Scripts.constants.app_constants import MyConst
app = FastAPI()
library_router = APIRouter()


@library_router.get(MyConst.Sign)
async def sign_get(request: Request):
    try:
        return await signup(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.get("/")
async def login_get(request: Request):
    try:
        return await login(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.get(MyConst.Add)
async def add_get(request: Request):
    try:
        return await add(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.get(MyConst.Delete)
async def delete_get(request: Request):
    try:
        return await delete(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.get(MyConst.Update)
async def update_get(request: Request):
    try:
        return await update(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.post(MyConst.Sign)
async def sign_post(request: Request):
    try:
        return await user_signup(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.post(MyConst.Login)
async def login_post(request: Request):
    try:
        return await user_login(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.post(MyConst.Add)
async def add_2(request: Request):
    try:
        return await add_book(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.post(MyConst.Delete)
async def delete_post(request: Request):
    try:
        return await books_delete(request)
    except Exception as e:
        return {"error:", str(e)}


@library_router.post(MyConst.Update)
async def update_post(request: Request):
    try:
        return await books_update(request)
    except Exception as e:
        return {"error:", str(e)}


# @library_router.get("/display")
# async def disp(request: Request):
#     return await display(request)
#
#
# @library_router.post("/display")
# async def disp_post(request: Request):
#     try:
#         return await display(request)
#     except Exception as e:
#         return {"Error:", str(e)}
