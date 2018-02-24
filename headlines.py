from mainfile import get_urls, get_news
# from bs4 import BeautifulSoup
# import requests

def get_headline_news(url):
	print("Scrapping headlines from google news")
	links = get_urls(url)
	for key in links:
		print(get_news({key : links[key]}))

if __name__ == '__main__':
	headline_url = 'https://news.google.com/news/headlines?ned=in&hl=en-IN&gl=IN'
	get_headline_news(headline_url)
