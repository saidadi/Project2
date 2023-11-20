import advertools as adv
import pandas as pd

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
    def download_sitemap(self):
        sitemap_url = f'{self.url}/sitemap.xml'
        sitemap_df = adv.sitemap_to_df(sitemap_url)
        return sitemap_df
