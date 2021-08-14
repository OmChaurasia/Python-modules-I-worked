import requests
r= requests.get("https://github.com/")
htmlcontent= r.content
print(htmlcontent)