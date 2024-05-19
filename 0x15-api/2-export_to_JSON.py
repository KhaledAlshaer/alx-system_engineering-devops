#!/usr/bin/python3
""" Python script to export data in the Json format """

import json
import requests
import sys


if __name__ == '__main__':

    employee_id = sys.argv[1]
    file_name = f"{employee_id}.json"
    link = "https://jsonplaceholder.typicode.com/"
    params = {"userId": employee_id}

    request = requests.get(f"{link}/users/{employee_id}")
    user_data = request.json()
    name = user_data.get("username")

    todo = requests.get(f"{link}/todos", params=params)
    todo_data = todo.json()

    json_data = {
            employee_id: [
                {
                    "task": td.get("title"),
                    "completed": td.get("completed"),
                    "username": name
                    } for td in todo_data
                ]
            }

    with open(file_name, "w") as file:
        json.dump(json_data, file)
