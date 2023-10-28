import smtplib
import requests
from bs4 import BeautifulSoup

def check_for_word_in_webpage(url, word):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text().lower()
    return word.lower() in page_text

def send_email(subject, body, to_email, from_email, from_email_password):
    with smtplib.SMTP('smtp.gmail.com', 587) as server: # Make sure SMTP is OK, This is for sending from Gmail
        server.starttls()
        server.login(from_email, from_email_password)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(from_email, to_email, message)

def main():
    url = 'https://sportal.blic.rs/fudbal/zvala-me-zvezda-goran-pandev-ugostio-sportal-i-pricao-o-srpskom-fudbalu-kosarci-i-otkrio-da-zamera-jednom-coveku-moram-da-dodjem-u-arenu-video/2023102709380996581' # Replace address
    word = 'Zvezda' # Replace with your word

    if check_for_word_in_webpage(url, word):
        send_email(
            subject=f'{word} Found',
            body=f'"{word}" was found at {url}. Check it out!',
            to_email='TO-EMAIL', #Email address where you would like to get the email
            from_email='FROM-EMAI',
            from_email_password='FROM PASSWORD'
        )

if __name__ == '__main__':
    main()


