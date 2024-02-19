#!/usr/bin/python3
"""fetches data from API and exports in CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users')

    users = user_response.json()

    for user in users:
        if user['id'] == user_id:
            username = user['username']
            break

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

    todos = todos_response.json()

    with open(f'{user_id}.csv', 'w', newline='') as e:
        tw = csv.writer(e, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task['userId'] == user_id:
                tw.writerow([
                    user_id,
                    username,
                    task.get('completed'),
                    task.get('title')
                ])
