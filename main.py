import requests,time,random
from bs4 import BeautifulSoup

head= headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

finance_urls = ['https://finance.yahoo.com/', 'https://www.investing.com/', 'https://www.marketwatch.com/']

for url in finance_urls:
    finance_data= requests.get(url, headers= head)
    finance_content= finance_data.content
    finance_soup= BeautifulSoup(finance_content, 'lxml' )
 

    print(f'---{url}---')
    print(finance_soup.text.strip())
    print()

    time.sleep(random.uniform(1,3))



# src_yahoo = requests.get('https://finance.yahoo.com/', headers=head)
# src_investing = requests.get('https://www.investing.com/', headers=head)


# yahoo_content = src_yahoo.content
# investing_content = src_investing.content

# yahoo_soup = BeautifulSoup(yahoo_content, 'lxml')
# investing_soup =BeautifulSoup(investing_content, 'lxml')
