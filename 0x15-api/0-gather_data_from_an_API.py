#!/usr/bin/python3
#  A script that uses a REST API for a given employee ID
#+ and returns a TODO list progress.
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo_items = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    for i in todo_items:
        if i.get("completed") is True:
            completed.append(i.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todo_items)))
    for item in completed:
        print("\t {}".format(item))
