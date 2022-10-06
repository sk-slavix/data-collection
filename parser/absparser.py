import requests
from bs4 import BeautifulSoup

class AbsParser:

    url = "https://rozetka.com.ua/ua/buromax_bm_291360_02/p341631229/"
    # url = "https://php.zone/php-i-mysql-s-nulya/indeksy-v-mysql"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
    }

    def getData(self):
        
        #code request on site for get data
        req = requests.get(self.url, headers=self.headers)
        src = req.text

        # print(src)

        soup = BeautifulSoup(src, "lxml")
        current_product_title = soup.find("h1", class_="product__title")
        current_product_price = soup.find("p", class_="product-prices__big")
        print(current_product_title.text)
        print(current_product_price.text)