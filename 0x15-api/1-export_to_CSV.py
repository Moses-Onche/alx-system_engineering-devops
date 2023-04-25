#!/usr/bin/python3
"""A script that exports a todo list into a CSV file."""

import csv
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(uid)).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [uid, username, t.get("completed"), t.get("title")]
         ) for t in todos]
