#!/usr/bin/python3
"""Top Ten"""

from email import header
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 10
    }

    top_posts = requests.get(url, headers=headers,
                             params=params, allow_redirects=False)

    if top_posts.status_code == 404:
        print("None")
        return

    top_posts = top_posts.json().get('data')
    [print(post.get('data').get('title'))
     for post in top_posts.get('children')]
