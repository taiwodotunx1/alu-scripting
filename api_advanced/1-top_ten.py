#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": (
            "linux:subreddit-fetcher:v1.0 (by /u/InternationalSet4877)"
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
