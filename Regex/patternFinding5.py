import re
def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.google.com/news/Market/2021/22/02/sensex/"
print(extract_date(url1))
