from playwright.sync_api import sync_playwright
from time import sleep


def clicker(path):
    page.click(path)


def input_text(path, text):
    page.fill(path, text)


email = "your email"
senha = "your key"

while True:
    print('start btc')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://freebitco.in/?op=home")
        sleep(6)
        clicker('//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')
        clicker('text=LOGIN')
        input_text('//*[@id="login_form_btc_address"]', email)
        input_text('//*[@id="login_form_password"]', senha)
        clicker('//*[@id="login_button"]')
        sleep(6)
        clicker('//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')
        clicker('//*[@id="free_play_form_button"]')
        sleep(4)
        clicker('//*[@id="myModal22"]/a')
        value_btc = float(page.inner_text('//*[@id="winnings"]'))
        browser.close()
        print(f'{value_btc:.8f}BTC await 60min')
        sleep(3615)
