#personal Finance Manager
import requests
from bs4 import BeautifulSoup
import smtplib

def check_price(URL, headers):
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    price = soup.find('span', {'class': 'a-price-whole'}).get_text()
    return float(price.replace(',', ''))

def send_email(product_name, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your_email_address@gmail.com', 'your_email_password')
    subject = f'Price fell down for {product_name}!'
    body = f'Check the Amazon link: {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'your_email_address@gmail.com',
        'recipient_email_address@gmail.com',
        msg
    )
    print('Hey! An email has been sent to notify you of the price drop.')

URL = 'https://www.amazon.in/dp/B08XGDNZBQ'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
price = check_price(URL, headers)
if price < 1000:
    send_email('product_name', URL)

