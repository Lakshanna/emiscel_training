from django.test import TestCase
from selenium import webdriver

browser = webdriver.Firebox()
browser.get('http://localhost:8000/admin')
body = browser.find_element_by_tag_name('body')
assert "Django administration" in body.text
browser.quit()
# Create your tests here.
