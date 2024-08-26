#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users,
      total subscribers) for a given subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditBot/0.1)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        # If there's an exception in the request, return 0
        return 0
