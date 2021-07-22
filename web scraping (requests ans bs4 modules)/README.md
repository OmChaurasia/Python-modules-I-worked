# Web Scraping 
## Importing modules
```
import requests
from bs4 import BeautifulSoup
```
## Requesting URL
```
r= requests.get("https://github.com/")
```
## Getting html content
```
htmlcontent= r.content
```
## Parse html using BeautifulSoup
```
soup= BeautifulSoup(htmlcontent , 'html.parser')
```
## To prettify soup
This is optional
```
print(soup.prettify)
```
## To get title  of page
```
title= soup.title
print(title)
print(title.string)
```
## To find  a tag 
```
anchor= soup.find_all('a')
print(anchor)
```
## To get a specific element and text

```
print(anchor[1])
print(anchor[1]['class'])
print(soup.find_all("a", class_="btn"))
print(anchor[1].get_text())
```