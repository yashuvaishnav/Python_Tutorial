import requests
response = requests.get("https://teachyourselfcoding.com/blog/")
print(response.text[:])  # Output: First 100 characters of webpage
