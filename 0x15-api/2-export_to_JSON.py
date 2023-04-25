#!/usr/bin/python3
"""A script that exports to-do list to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(uid)).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.json".format(uid), "w") as jsonfile:
        json.dump({uid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
