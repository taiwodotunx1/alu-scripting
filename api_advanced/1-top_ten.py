#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/taiwodotun1)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    children = response.json().get("data", {}).get("children", [])
    if not children:
        print(None)
        return
    for post in children[:10]:
        print(post.get("data", {}).get("title"))
