import webbrowser
url = 'https://www.google.com/search?q=om+chaurasia+blogs'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
for i in range(1):
    webbrowser.get(chrome_path).open_new(url)
