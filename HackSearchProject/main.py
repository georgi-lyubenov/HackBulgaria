from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup
from create_db import *
from urllib.parse import urljoin


class Spider():
    def __init__(self, homepage):
        self.scanned_pages = []
        self.queue = []
        self.engine = create_engine("sqlite:///my_database.db")
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)
        self.homepage = homepage

    def prepare_url(self, url, href):
        return urljoin(url, href)

    def scan_page(self, url):
        self.scanned_pages.append(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        soup.prettify()
        html_title = soup.title.string
        try:
            description = soup.find(attrs={"property": "og:description"}).get("content")
            desc = description
        except Exception as e:
            desc = "None"
        links = soup.findAll('a')
        for link in links:
            url = self.prepare_url(url, link.get("href"))
            obj = Website(URL=url, title=html_title, description=desc)
            self.session.add(obj)
            self.session.commit()
            if "http" in link.get("href"):
                if link.get("href") not in self.scanned_pages:
                    self.queue.append(self.prepare_url(url, link.get("href")))

    def scan_website(self):
        self.scan_page(self.homepage)

        while self.queue:
            print(self.queue.pop(), len(self.scanned_pages))
            try:
                self.scan_page(self.queue.pop())
            except:
                pass
        return ("pages scanned: ", len(self.scanned_pages))


def main():
    base_url = 'http://fmi.py-bg.net/'
    #base_url = 'http://google.com'
    s = Spider(base_url)
    s.scan_website()

if __name__ == '__main__':
    main()

