import requests
from bs4 import BeautifulSoup
data = {
    'Name':'[python]',
    'Email':'[pyth@on]',
    'Mobile':'[python]',
    'Message':'[ppy]'
}
r= requests.post("https://omchaurasia.github.io/blogs/contact.html",data=data)
htmlcontent= r.content
soup= BeautifulSoup(htmlcontent , 'html.parser')

print(soup.prettify)