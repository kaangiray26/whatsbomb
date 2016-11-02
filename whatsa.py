#!/usr/bin/python
#-*- coding: utf-8 -*-
#Created by Kaanthegmr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
raw_input("Press enter if you logged in:")
img = driver.find_element_by_class_name("intro-title")
try:
    assert img.text in driver.page_source
except AssertionError:
    print "Log in failure"
    time.sleep(3)
    driver.close()
isim=driver.find_element_by_css_selector(".input.input-search")
isim.send_keys(raw_input("Name:"))
time.sleep(5)
driver.find_element_by_css_selector(".emojitext.ellipsify").click()
time.sleep(2)
def send(text):
    mesaj=driver.find_element_by_class_name("input-container").send_keys(text)
    driver.find_element_by_css_selector(".icon.btn-icon.icon-send.send-container").click()
global text
text=raw_input("Message:")
range=input("How many times:")
for i in range(int(range):
    send(text)
