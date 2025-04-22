import requests as req
URL="https://realpython.github.io/fake-jobs/"
page=req.get(URL)
print(page.text)