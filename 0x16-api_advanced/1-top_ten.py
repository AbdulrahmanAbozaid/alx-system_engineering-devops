#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'MyRedditBot/0.1'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
        else:
            print("None")
    except Exception:
        print("None")
