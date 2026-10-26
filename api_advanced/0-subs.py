#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://old.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": (
            "linux:subreddit-fetcher:v1.0 (by /u/InternationalSet4877)"
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    if not results:
        return 0
    return results.get("subscribers", 0)
