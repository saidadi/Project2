import requests
import pandas as pd
import xml.etree.ElementTree as ET

class SitemapParser:
    def __init__(self, url):
        self.url = url
    """
    ### Sitemap Data:
    The sitemap data provides information about URLs and their corresponding metadata. 
    Fields:
    - 'loc': URL of the page
    - 'lastmod': Last modification timestamp

    Questions:
    1. What are the recently modified pages on the website?
    2. How frequently are the pages updated?
    """
    def get_sitemap_urls(self):
        robots_url = f"{self.url}/robots.txt"
        response = requests.get(robots_url)
        lines = response.text.split('\n')

        sitemap_urls = []
        for line in lines:
            if line.startswith("Sitemap:"):
                sitemap_url = line.split(": ")[1]
                sitemap_urls.append(sitemap_url)

        return sitemap_urls

    def parse_sitemap(self, sitemap_url):
        response = requests.get(sitemap_url)
        root = ET.fromstring(response.content)
        sitemap_data = []

        for url_elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
            loc_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
            lastmod_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")

            url = loc_elem.text if loc_elem is not None else ""
            lastmod = lastmod_elem.text if lastmod_elem is not None else ""

            sitemap_data.append({"loc": url, "lastmod": lastmod})

        return pd.DataFrame(sitemap_data)

    def download_sitemaps(self):
        sitemap_urls = self.get_sitemap_urls()

        if sitemap_urls:
            dfs = []
            for sitemap_url in sitemap_urls:
                sitemap_df = self.parse_sitemap(sitemap_url)
                dfs.append(sitemap_df)

            combined_df = pd.concat(dfs, ignore_index=True)
            return combined_df
        else:
            print("No sitemap URLs found in the robots.txt file.")
            return None
