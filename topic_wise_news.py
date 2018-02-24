from mainfile import get_urls, get_news

def get_topic_wise_news(topic):
    # Change the company name, you want news for
    topic = topic
    base_url = "https://news.google.com/news/search/section/q/"
    follow_url = '?hl=en-IN&gl=IN&ned=in'
    url = base_url + topic + '/' + topic + follow_url
    print("Scrapping all news article links related to " + topic)
    links = get_urls(url)
    for key in links:
        # print(key)
        # print(links[key])
        print(get_news({key : links[key]}))

if __name__ == '__main__':
    given_topic = 'narendra singh modi'
    get_topic_wise_news(given_topic)
    
