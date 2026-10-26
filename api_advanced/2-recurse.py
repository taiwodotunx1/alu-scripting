#!/usr/bin/python3
"""Function to recursively get all hot posts for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": (
            "linux:subreddit-fetcher:v1.0 (by /u/InternationalSet4877)"
        )
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    children = data.get("children", [])
    after = data.get("after")
    for post in children:
        hot_list.append(post.get("data").get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
