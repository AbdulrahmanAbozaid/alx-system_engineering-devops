#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users,
      total subscribers) for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    subreddits = requests.get(url, headers=headers, allow_redirects=False)
    if subreddits.status_code == 200:
        subreddits = subreddits.json()
        return subreddits['data']['subscribers']
    else:
        return 0
