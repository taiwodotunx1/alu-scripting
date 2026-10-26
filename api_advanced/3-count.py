#!/usr/bin/python3
"""Function to count keywords in hot posts for a given subreddit."""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    """Count and print keywords found in hot post titles."""
    if not counts:
        counts = {word.lower(): 0 for word in word_list}

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
        return
    data = response.json().get("data")
    children = data.get("children", [])
    after = data.get("after")

    for post in children:
        title = post.get("data").get("title").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, hot_list, after, counts)
