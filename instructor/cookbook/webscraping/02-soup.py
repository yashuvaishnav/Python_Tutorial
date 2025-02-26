import requests
from bs4 import BeautifulSoup

url = "https://teachyourselfcoding.com/blog/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())  # Pretty-print the parsed HTML
else:
    print("Failed to retrieve the page")

# Extract all divs
paragraphs = soup.find_all("article")
for p in paragraphs:
    print(p.text)

# Extract all links
print("LINKS IN THE WEBSITE: ");
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# Extract all images
print("IMAGES: ")
images = soup.find_all("img")
for img in images:
    print(img["src"])
