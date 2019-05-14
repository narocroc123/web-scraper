# import libraries
from urllib.parse import urlsplit
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from collections import deque

# specifying the url
url = "INPUT URL HERE"

# deque object to queue urls to be scraped next
new_urls = deque([url])

# set of urls that have been processed
processed_urls = set()

# set of domains inside target website
local_urls = set()

# set of domains outside taget website
foreign_urls = set()

# set of broken urls
broken_urls = set()

# process urls until queue is exhausted
while len(new_urls):
    # move url from queue to processed
    url = new_urls.popleft()
    processed_urls.add(url)
    # print current url
    print("Processing" % url)
    # catching broken urls
    try:
        response = request.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
        # add broken url to own set
        broken_urls.add(url)
        continue
    # extract base url to differentiate between local and foreign links
    parts = urlsplit(url)
    base = "{0.netloc}".format(parts)
    strip_base = base.replace("www.", "")
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    # using BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")

    for link in soup.find.all('a'):
        # extract links from anchor tags
        anchor = link.attrs["href"] if "href" in link.attrs else ''
    
    # scrape links and sort into correct sets
    if anchor.startswith('/'):
        local_link = base_url + anchor
        local_urls.add(local_link)
    elif strip_base in anchor:
        local_urls.add(anchor)
    elif not anchor.startswith('http'):
        local_link = path + anchor
        local_urls.add(local_link)
    else:
        foreign_urls.add(anchor)

    # limit scraping to local urls
    for link in local_urls:
        if not link in new_urls and not link in processed_urls:
            new_urls.append(link)

print(processed_urls)