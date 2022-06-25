from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot 
		bot.get('https://twitter.com/login')
		time.sleep(10)
		email = bot.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
		email.clear()
		email.send_keys(self.username)
		next_button = bot.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
		next_button.click()
		time.sleep(10)
		password = bot.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
		password.clear()
		password.send_keys(self.password)
		login_button=bot.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
		login_button.click()


	def post(self):
		bot = self.bot
		time.sleep(15)
		tweet_button = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
		tweet_button.click()
		time.sleep(5)
		tweet = 'building bots with python is fun!'
		text = bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
		text.send_keys(tweet)
		post_button = bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
		post_button.click()
ayo = TwitterBot('#username here', '#password here')
ayo.login()
ayo.post()
