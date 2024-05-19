#!/usr/bin/python3
""" Python script to export data in the Json format """

import json
import requests
import sys


if __name__ == '__main__':

    file_name = f"{employee_id}.json"
    link = "https://jsonplaceholder.typicode.com/"

    request = requests.get(f"{link}/users")
    user_data = request.json()
    name = user_data.get("username")

    todo = requests.get(f"{link}/todos")
    todo_data = todo.json()

    json_data = {
            request.get("id"): [
                {
                    "task": td.get("title"),
                    "completed": td.get("completed"),
                    "username": name
                    } for td in todo_data
                ] for user in request
            }

    with open(file_name, "w") as file:
        json.dump(json_data, file)
