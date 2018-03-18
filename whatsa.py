#!/usr/bin/python
#-*- coding: utf-8 -*-
#Created by Kaanthegmr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
time.sleep(2)
while True:
  try:
    img = driver.find_element_by_id("input-chatlist-search")
  except NoSuchElementException:
    pass
  try:
    if img.is_displayed():
      break
  except NameError:
    pass
time.sleep(2)
search=driver.find_element_by_id("input-chatlist-search")
name=raw_input("Name:")
search.send_keys(name)
time.sleep(5)
for i in driver.find_element_by_class_name("RLfQR").find_elements_by_class_name("matched-text"):
    if name in i.text:
        i.click()
        break
time.sleep(2)
def send(text):
    driver.find_element_by_id("main").find_element_by_css_selector("._2S1VP.copyable-text.selectable-text").click()
    mesaj=driver.find_element_by_id("main").find_element_by_css_selector("._2S1VP.copyable-text.selectable-text").send_keys(text,Keys.ENTER)
msg=raw_input("Message:")
numid=input("Repeat for:")
for i in range(int(numid)):
    send(msg)
print "Done"
