#!/usr/bin/python3

import requests
import json

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API to get the number of subscribers for a subreddit.

  Args:
      subreddit: The name of the subreddit.

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Use a custom User-Agent to avoid rate limiting issues
  headers = {"User-Agent": "My Reddit Subscriber Count App"}

  # Construct the API URL
  url = f"https://www.reddit.com/r/{subreddit}/about.json"

  try:
    # Send a GET request without following redirects
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    # Parse JSON response
    data = response.json()

    # Check if 'data' and 'subscribers' keys exist
    if "data" in data and "subscribers" in data["data"]:
      return data["data"]["subscribers"]
    else:
      return 0

  except requests.exceptions.RequestException as e:
    # Handle any errors during the request
    print(f"Error: {e}")
    return 0

# Example usage
subreddit_name = "programming"
num_subscribers = number_of_subscribers(subreddit_name)

if num_subscribers > 0:
  print(f"Subreddit '{subreddit_name}' has {num_subscribers:,} subscribers.")
else:
  print(f"Subreddit '{subreddit_name}' is invalid or not found.")
