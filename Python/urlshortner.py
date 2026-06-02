import hashlib


class URLShortener:

    def __init__(self):
        self.urls = {}

    def shorten_url(self, url):

        short_url = hashlib.md5(url.encode()).hexdigest()[:6]

        self.urls[short_url] = url

        return short_url

    def get_original_url(self, short_url):

        if short_url in self.urls:
            return self.urls[short_url]

        return "URL Not Found"


shortener = URLShortener()

url = "https://www.google.com"

short_code = shortener.shorten_url(url)

print(f"Original URL : {url}")
print(f"Short URL Code : {short_code}")

print("\nRedirect Simulation")
print(f"Retrieved URL : {shortener.get_original_url(short_code)}")