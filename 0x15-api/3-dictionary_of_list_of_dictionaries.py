#!/usr/bin/python3
""" Python script to export data in the JSON format """

import json
import requests


if __name__ == '__main__':

    file_name = "todo_all_employees.json"
    link = "https://jsonplaceholder.typicode.com/"

    users_response = requests.get(f"{link}/users")
    users_data = users_response.json()

    todos_response = requests.get(f"{link}/todos")
    todos_data = todos_response.json()

    json_data = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": td.get("title"),
                "completed": td.get("completed")
            }
            for td in todos_data if td.get("userId") == user_id
        ]
        json_data[user_id] = user_tasks

    with open(file_name, "w") as file:
        json.dump(json_data, file)
