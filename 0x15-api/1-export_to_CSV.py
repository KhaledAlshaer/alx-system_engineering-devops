#!/usr/bin/python3
""" Python script to export data in the CSV format """

import csv
import requests
import sys


if __name__ == '__main__':

    employee_id = sys.argv[1]
    file_name = f"{employee_id}.csv"
    link = "https://jsonplaceholder.typicode.com/"
    params = {"userId": employee_id}

    request = requests.get(f"{link}/users/{employee_id}")
    user_data = request.json()
    user_name = user_data.get("username")


    todo = requests.get(f"{link}/todos", params=params)
    todo_data = todo.json()


    csv_data = [
        [
            employee_id,
            user_name,
            td.get("completed"),
            td.get("title")
        ]
        for td in todo_data
    ]

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
