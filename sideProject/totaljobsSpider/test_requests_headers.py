import requests

url = 'https://www.totaljobs.com/jobs/sales/in-london?radius=10&searchOrigin=Resultlist_top-search'

# pretending to access as a browser
headers = {"content-type": "text/html; charset=utf-8", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
print(res.status_code)