from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import serializeDict,serializeList
from bson import ObjectId
user=APIRouter()

@user.get("/todo-list")
async def get_all_todos():

    return serializeList(conn.local.user.find())



@user.post("/create-todo")
async def Add_new_todo(user:User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())


@user.put("/update-todo/{id}")
async def update_todo(id,user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))




@user.delete("/delete-todo/{id}")
async def delete_todo(id, user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))

@user.get("/get-todo/{id}")
async def get_todoBy_id(id):
    return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))





