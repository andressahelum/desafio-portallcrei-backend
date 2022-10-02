# desafio back end Portal Lacrei
# Criar uma lista de tarefas que permite listagem e criação de novas tarefas.

from flask import Flask, request
from database import to_do_lists


app = Flask(__name__)
app.debug = True


@app.get('/to-do-list')
def get_todolists():
    return {"to_do_lists": to_do_lists}, 200


@app.get('/to-do-list/<string:name>')
def get_todolist(name):
    for todolist in to_do_lists:
        if todolist["todolist_name"] == name:
            return todolist, 200
    return {"message": "to-do-list not found"}, 404


@app.post('/to-do-list')
def create_todolist():
    request_data = request.get_json()
    new_todolist = {"todolist_name": request_data["name"], "tasks":[]}
    to_do_lists.append(new_todolist)
    return new_todolist, 201


@app.post('/to-do-list/<string:name>/task')
def create_task(name):
    request_data = request.get_json()
    for todolist in to_do_lists:
        if todolist["todolist_name"] == name:
            todolist["tasks"].append(request_data["task_name"])
            return request_data["task_name"], 201
    return {"message": "to-do list not found"}, 404


@app.get('/to-do-list/<string:name>/task')
def get_todolist_task(name):
    for todolist in to_do_lists:
        if todolist["todolist_name"] == name:
            return {"task": todolist["tasks"]}, 200
    return {"message": "to-do list not found"}, 404



