import re
import math
from lxml import html, etree
import csv, os, json
from requests import get
from time import sleep



url = "https://www.newegg.com/PlayStation/Category/ID-335?Tid=22019"

body = get(url)
doc = html.fromstring(body.content)

info = doc.xpath('/html/body/div[6]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[4]/div/div[2]/ul/li[3]/strong[@class="price-current-label"]/text()')
print (info)