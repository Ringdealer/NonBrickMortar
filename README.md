# Scraping Amazon.com using web page search function


![](https://img.shields.io/badge/made_by-Ringdealer-blue)


---

## About spider name
All the spiders I use in Scrapy have names related to real spiders. The name of the spider used in this project is taken from the genus `nephila`. These spiders weave impresive webs. You can check more at https://en.wikipedia.org/wiki/Nephila



---

## Table of Contents
- [Description](#description)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Reference](#api-reference)
- [Sample Output](#sample-ouput)


---

## Description
This is a simple scraper for extracting products details from "Amazon.com" when specified in the search page.

---

## Fields

These are the fields the scraper is going to fetch:
- Title
- Stars
- Price
- Image Link
- Image Name
---

### Technologies
- Python
- Scrapy
- PyCharm

---

### Installation
This project uses different packages that need to be installed in PyCharm. In order to do that go to the menu bar and go to:

`file->settings->Project:[project_name]->Python Interpreter`

 and then press the `+` button at the right side to open the package installation and management window. In the search window search for the packages mentioned below and click Install Package (you will need and internet connection)

 - Scrapy
 - Urllib3


  Amazon could ban the computer visiting its web site. If it is the case, to bypass those restrictions we are going to use an USER_AGENT allowed by Amazon to be used by Google. 

  In order to get it we go to https://www.whatismybrowser.com/detect/what-is-my-user-agent and copy the User Agent shown in the web site. In the project folder we open `settings.py` and under the commented code for user agent we paste
  `USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'`

---
## Using the scrapper
1. In the method `start_requests` in the file nephila.py change value in variable `search_text` to look for a new item.
2. In PyCharm terminal run command `scrapy crawl nephila crawler -o items.json` to get data as JSON File. 
---

## API Reference
```python
    def start_requests(self):
        """Function to read keywords from keywords file"""
        #keywords = csv.DictReader(open(os.path.join(os.path.dirname(__file__), "../resources/keywords.csv")))
        search_text = 'earphones'
        # for keyword in keywords:
        #     search_text = keyword["keyword"]
        try:
            url = "https://www.amazon.com/s?k={0}&ref=nb_sb_noss_2".format(search_text)
        except HTTPError as e:
            print(e)
        else:
            yield scrapy.Request(url, callback=self.parse_item, meta={"search_text": search_text})

```

---

## Sample Output 

---
<img src="./demo.jpg">

> Dataframe as shown in Jupyter notebook.
---

## References

[Back to the Top](#Learn-to-Scrape-and-Analyze-Data)






> 



