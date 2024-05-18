#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':

    link = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    params = {'userId': employee_id}

    request = requests.get(f"{link}/users/{employee_id}").json()
    todo = requests.get(f"{link}/todos", params=params).json()
    completed = [td['title'] for td in todo if td['completed']]

    name = request.get("name")
    all_todo = len(todo)
    complete = len(completed)

    print(f"Employee {name} is done with tasks ({complete}/{all_todo})")
