#!/usr/bin/python3
#install cryptocompare
#pip install cryptocompare
import cryptocompare
import time
import I2C_LCD_driver
import RPi.GPIO as GPIO
import requests
eth_address = ""  # your ethereum address goes here
site = "https://etherchain.org/api/account/" + eth_address

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
req = requests.get(site, headers=hdr)
jsondata = req.json()

state = 4
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mylcd = I2C_LCD_driver.lcd()

while True:
    input_state = GPIO.input(14)
    pricebtc = cryptocompare.get_price('BTC', curr='GBP')
    pricebtc = cryptocompare.get_price('BTC',curr='GBP')
    priceeth = cryptocompare.get_price('ETH', curr='GBP')
    while (input_state == True) and (state == 4):
        pricebtc = cryptocompare.get_price('BTC', curr='GBP')
        mylcd.lcd_display_string(str("BTC GBP {0}".format((pricebtc['BTC']['GBP']))), 1)
        mylcd.lcd_display_string(str(jsondata['data'][0]['balance'] / 1000000000000000000), 2)
        input_state = GPIO.input(14)
        if (input_state == False):
            state = state - 1
            print("going to break")
            break
            req = requests.get(site, headers=hdr)
            jsondata = req.json()

    while (input_state == True) and (state ==3):
        priceeth = cryptocompare.get_price('ETH', curr='GBP')
        mylcd.lcd_display_string(str("ETH GBP {0}".format((priceeth['ETH']['GBP']))), 1)
        mylcd.lcd_display_string(str(jsondata['data'][0]['balance'] / 1000000000000000000), 2)
        input_state = GPIO.input(14)
        if (input_state == False):
            state = state - 1
            print("going to break")
            break
            req = requests.get(site, headers=hdr)
            jsondata = req.json()

    while (input_state == True) and (state == 2):
        priceeth = cryptocompare.get_price('STEEM', curr='USD')
        mylcd.lcd_display_string(str("STEEM USD {0}".format((priceeth['STEEM']['USD']))), 1)
        mylcd.lcd_display_string(str(jsondata['data'][0]['balance'] / 1000000000000000000), 2)

        input_state = GPIO.input(14)
        if (input_state == False):
            state = state - 1
            print("going to break")
            break
            req = requests.get(site, headers=hdr)
            jsondata = req.json()

    while (input_state == True) and (state == 1):
        priceeth = cryptocompare.get_price('ETH', curr='GBP')
        mylcd.lcd_display_string(str("balance {0}".format((float(priceeth['ETH']['GBP']))*jsondata['data'][0]['balance'] / 1000000000000000000.0)), 1)
        mylcd.lcd_display_string(str(jsondata['data'][0]['balance'] / 1000000000000000000), 2)
        input_state = GPIO.input(14)
        if (input_state == False):
            state = state - 1
            print("going to break")
            break
            req = requests.get(site, headers=hdr)
            jsondata = req.json()

    if (state == 0):
        state = 4

