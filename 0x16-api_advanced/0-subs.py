#!/usr/bin/python3
"""
get number of subscribers in a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    # Reddit API URL for subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "linux:0x16.api.advanced by Malika)"}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data["data"]["subscribers"]
        elif response.status_code == 404:
            # If the subreddit is not found, return 0
            return 0
        else:
            # Handle other status codes if needed
            print("Error: {}".format(response.status_code))
            return 0

    except Exception as e:
        print("Error: {}".format(e))
        return 0
