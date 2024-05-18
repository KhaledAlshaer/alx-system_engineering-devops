#!/usr/bin/python3
"""Python script that for a given employee ID, returns information about
his/her TODO list progress"""

import requests
import sys

if __name__ == '__main__':

    link = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    params = {'userId': employee_id}

    request = requests.get(f"{link}/users/{employee_id}")
    user_data = request.json()
    name = user_data.get("name")

    todo = requests.get(f"{link}/todos", params=params)
    todo_data = todo.json()

    completed = [td['title'] for td in todo_data if td['completed']]

    all_todo = len(todo_data)
    complete = len(completed)

    print(f"Employee {name} is done with tasks({complete}/{all_todo}):")

    for task in completed:
        print(f"\t {task}")
