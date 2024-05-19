#!/usr/bin/python3
""" Python script to export data in the CSV format """

import csv
import requests
import sys


if __name__ == '__main__':

    file_name = f"{user_id}.csv"
    link = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    params = {"userId": employee_id}

    request = requests.get(f"{link}/users/{employee_id}")
    data = request.json()

    todo = requests.get(f"{link}/todos", params=params)
    todo_data = todo.json()

    csv_data = [
            [
                employee_id,
                todo.get["username"],
                todo.get["completed"],
                todo.get["title"],
                ]
            ] for td in todo

    with open(file_name, "w", newline="") as file:

        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
