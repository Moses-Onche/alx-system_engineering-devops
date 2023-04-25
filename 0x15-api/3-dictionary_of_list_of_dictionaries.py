#!/usr/bin/python3
"""A script that exports to-do list to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as j_file:
        json.dump({
            p.get("id"): [{
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": p.get("username")
            } for item in requests.get(url + "todos",
                                    params={"userId": p.get("id")}).json()]
            for p in employee}, j_file)
