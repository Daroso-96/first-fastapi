from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad user
class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int


users_list = [User(id=1, name="Sasha", lastname="dog", url="https://sashita.dog", age=3),
              User(id=2, name="Dayana", lastname="Romero", url="https://dayana.dev", age=26)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Sasha", "lastname": "Dog", "url": "https://sashita.dog", "age": 3},
            {"name": "Dayana", "lastname": "Romero", "url": "https://dayana.dev", "age": 26}]


@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
      return list(users)[0]
    except:
          return {"error":" No se ha encontrado el usuario"}

#Query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user:User):
    if type(search_user(user.id)) == User:
        return {"messsage": "Este usuario ya existe"}
    else:
        users_list.append(user)
        return user


@app.put("/user/")
async def user(user:User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": " No se ha actualizado  el usuario"}
    else:
        return user


@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": " No se ha encontrado el usuario"}





