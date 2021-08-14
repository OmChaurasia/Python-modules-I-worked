import requests

url = "https://www.amazon.in/"
payload = {'field-keywords':'phone'}
r = requests.get(url, payload)
htmlcontent= r.content
print(htmlcontent)