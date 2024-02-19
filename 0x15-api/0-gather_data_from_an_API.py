#!/usr/bin/python3
"""fetches data from API using jsonplaceholder"""

import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')

    user = user_response.json()

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    print(f"Employee {user.get('name')} is done with tasks"
          f"({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print("\t", task.get('title'))
