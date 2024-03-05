#!/usr/bin/python3
"""
get number of subscribers in a subreddit.
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced by Malika)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            [
                print(c.get("data").get("title"))
                for c in results.get("children")
            ]
        else:
            print("None")
            return

    except Exception as e:
        print("Error: {}".format(e))
