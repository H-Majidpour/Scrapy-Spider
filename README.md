# **Spiders**

## Overview 
Spiders are classes which define how a certain site (or a group of sites) will be scraped, including how to perform the crawl (i.e. follow links) and how to extract structured data from their pages (i.e. scraping items). In other words, Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).

**For spiders, the scraping cycle goes through something like this:**
1. You start by generating the initial Requests to crawl the first URLs, and specify a callback function to be called with the response downloaded from those requests.

2. In the callback function, you parse the response (web page) and return item objects, Request objects, or an iterable of these objects. Those Requests will also contain a callback (maybe the same) and will then be downloaded by Scrapy and then their response handled by the specified callback.

3. In callback functions, you parse the page contents, typically using Selectors (but you can also use BeautifulSoup, lxml or whatever mechanism you prefer) and generate items with the parsed data.

4. Finally, the items returned from the spider will be typically persisted to a database.


## How to use
You have to install scrapy framework:
- In command prompt/Terminal: pip install scrapy

Once you have installed scrapy framework, just clone/download this project, access the folder in command prompt/Terminal and run the following command:
- scrapy crawl book_crawler

</br>
</br>
</br>
</br>


### **taTIran** :)


