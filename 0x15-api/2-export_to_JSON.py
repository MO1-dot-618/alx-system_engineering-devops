#!/usr/bin/python3
"""fetches data from API and  exports to jsn"""

import json
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

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
