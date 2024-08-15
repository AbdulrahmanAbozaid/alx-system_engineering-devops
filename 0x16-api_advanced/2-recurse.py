#!/usr/bin/python3
"""Recurse it!"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing
      the titles of all hot articles for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    top_posts = requests.get(url, headers=headers,
                             params=params, allow_redirects=False)

    if top_posts.status_code != 200:
        return None

    top_posts = top_posts.json().get('data')
    after = top_posts.get("after")
    count += top_posts.get("dist")

    for post in top_posts.get("children"):
        hot_list.append(post.get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
