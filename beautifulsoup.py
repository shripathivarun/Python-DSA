import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input("Enter -")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")
# Retrieve all of the anchor tags
tags=soup('a')
for tag in tags:
    print(tag('href',None))










import ssl
import urllib.request
from bs4 import BeautifulSoup

# Ignore SSL certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup.find_all('span', class_='comments')

total = 0
count = 0
for span in spans:
    number = int(span.text.strip())
    total += number
    count += 1

print("Count:", count)
print("Sum:", total)

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User inputs
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Loop to follow links
for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position - 1].get('href', None)

# Extract and print the last name
last_name = url.split("_")[-1].split(".")[0]
print("The answer to the assignment is:", last_name)