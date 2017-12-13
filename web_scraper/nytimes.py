#!/usr/bin/env python3

"""
nytimes.py

This program scrapes an article from the New York Times website and 
extracts the relevant information using BeautifulSoup. The results 
are displayed in an HTML template via Flask.
"""

import flask
import requests
from bs4 import BeautifulSoup


app = flask.Flask(__name__) #flask object

@app.route('/')
def scrape_times_article():

	url = 'https://www.nytimes.com/2017/10/29/business/virtual-reality-driverless-cars.html'

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser') #beautifulSoup object

	# get article elements
	title = soup.find('h1', {'id': 'headline'}).text
	author = soup.find('span', {'class': 'byline-author'}).text
	pub_date = soup.find('time', {'class': 'dateline'}).text

	article = soup.find_all('p', {'class': 'story-body-text story-content'}) #get all paragraphs in the source code
	p_list = []

	for p in article:
	    p_list.append(p.text) #loop through each paragraph and append the text to the list

	paragraphs = '\n\n'.join(p_list) #combine & format individual paragraphs

	paragraphs = paragraphs.replace('\n', '<br/>') #workaround to keep paragraph separation in HTML template

	images = soup.find_all('img', {'class': 'media-viewer-candidate'}) # find all images with this class
	img_list = []

	for img in images:
	    img_list.append(img['src']) #get the src attribute of the img tag

	image_1 = img_list[0] #create individual containers for each image
	image_2 = img_list[1]
	image_3 = img_list[2]

	return flask.render_template('index.html', 
		title=title,
		author=author,
		pub_date=pub_date,
		paragraphs=paragraphs,
		image_1=image_1,
		image_2=image_2,
		image_3=image_3)

if __name__ == '__main__':
	app.run()
