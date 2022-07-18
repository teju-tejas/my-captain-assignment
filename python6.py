import requests
url ="https://www.croma.com/oneplus-9-pro-5g-256gb-rom-12gb-ram-le2121-in-pine-green-/p/233756?utm_source=bing&utm_medium=ps&utm_campaign=sok_pla_standard_focus_products_bing&msclkid=d8c8ffd618601fc543d99d03984a952d&utm_term=4576579731703101&utm_content=Focus%20SKUs"
page = requests.get(url)

from bs4 import beautifulsoup4

soup = beautifulsoup ( page.content, "html parser")
price = soup.find_all('div',attrs={"class":"amount"})[0].get_text()


