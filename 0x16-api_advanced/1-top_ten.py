#!/usr/bin/python3
"""
Defines a function that queries Reddit API
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'advanced-api/0.0.1 by Huseini'}
    try:
        req = requests.get(url=url, headers=headers, allow_redirects=False)
        req.raise_for_status()  # Raises HTTPError for bad status codes
        response = req.json()
        titles = [child['data']['title']
                  for child in response['data']['children'][:10]]
        for title in titles:
            print(title)
    except requests.HTTPError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <subreddit>")
        sys.exit(1)
    top_ten(sys.argv[1])
