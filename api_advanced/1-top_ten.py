#!/usr/bin/python3
"""Function to print the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://old.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": (
            "linux:subreddit-fetcher:v1.0 (by /u/InternationalSet4877)"
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
    print(None)
    return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
