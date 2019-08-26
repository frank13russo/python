import webbrowser , sys, pyperclip
sys.path.insert(1,'Q:\Git\python')
import fmrstd
import logging
import os
import requests, bs4
from selenium import webdriver

#mapit.py


fmrstd.basicSetup()

"""

Gets a street address from the command line arguments or clipboard.
Opens the web browser to the Google Maps page for the address.


Read the command line arguments from sys.argv.
Read the clipboard contents.

Call the webbrowser.open() function to open the web browser.
Open a new file editor window and save it as mapIt.py.
"""

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    #TODO Get address from clipboard.
    logging.debug(address)
else:
    address=pyperclip.paste()
    logging.debug(address)
    
webbrowser.open('https:www.google.com/maps/place/' + address)
    
"""
The sys.argv variable stores a list of the
 program’s filename and command line arguments. 
 If this list has more than just the filename in it, 
 then len(sys.argv) evaluates to an integer greater than 1, 
 meaning that command line arguments have indeed been provided.
 """
 
res = requests.get('https://www.google.com/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

"""XKCD Scraper"""

#SELENIUM

browser = webdriver.Firefox()
type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')