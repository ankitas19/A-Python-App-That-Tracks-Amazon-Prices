import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/gp/product/B089F3WL8T/ref=s9_acss_bw_cg_Lap_2c1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=FF3YNZHPX33S6KZ4AJG9&pf_rd_t=101&pf_rd_p=c28ba8e3-77cc-4a2f-b64a-b39616b4469c&pf_rd_i=21570146031'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
def check_price():
res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[1:])
if(converted_price<42999):
send_mail()
print(converted_price)
print(title.strip()) 
if(converted_price > 42999):
send_mail() 
def send_mail():
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('sonal.as2@gmail.com', 'ptfpmcgzefjievwz')
subject = 'Price has gone down!'
body = 'Check the Amazon Link https://www.amazon.in/gp/product/B089F3WL8T/ref=s9_acss_bw_cg_Lap_2c1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=FF3YNZHPX33S6KZ4AJG9&pf_rd_t=101&pf_rd_p=c28ba8e3-77cc-4a2f-b64a-b39616b4469c&pf_rd_i=21570146031'
msg = f"Subject: {subject}\n\n{body}"
server.sendmail(
    'sonal.as2@gmail.com',
    'ankita1230.cse18@chitkara.edu.in',
    msg
)
print('EMAIL HAS BEEN SENT!')
server.quit()
while(True):
    check_price()
    time.sleep(60 * 60)