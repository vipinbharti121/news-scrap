from bs4 import BeautifulSoup
import requests


def get_urls(full_url):
    # Fetching all news article urls and their heading title from google news site
    # links = {'title' : 'url'}
    links = {}
    try:
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get all links from google news
        link_container = soup.findAll("a", {"class": "nuEeue hzdq5d ME7ew"})
        for link in link_container:
            links[link.text.strip()] = link['href']
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
    return links


def get_news(article_url):
    try:
        url = ''
        title = ''
        for key in article_url:
            title = key
            url = article_url[key]
        response = requests.get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        '''
        EconomicsTime div{"class" : "Normal"}
        HindustanTimes div{"class" : "story-details"}
        NDTV div{"class" : "ins_storybody"}
        Livemint div{"class" : "content"}
        ANINews div{"class" : "content"})s
        TimesOfIndia div{"class" : "Normal"}
        Bloomberg div{"class" : "body-copy"}
        FinancialExpress div{"class" : "main-story-content"}
        IndianExpress div{"class" : "full-details"})
        Reuters div{"class" : "StandardArticleBody_container_17wb1"})
        TheQuint div{"class" : "story-article__content__element--text"})
        ZeeBusiness div{"class" : "field-item even"})
        FirstPost div{"class" : "article-full-content"})

        '''
        # data = {'title':'value', 'url' : 'value', 'content' : 'value'}
        data = {}
        full_data = []
        ec_container = html_soup.findAll("div", {"class" : "Normal"})
        for news in ec_container:
            # print(news.text)
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)    

        hindustan_container = html_soup.findAll("div", {"class" : "story-details"})
        for news in hindustan_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        ndtv_container = html_soup.findAll("div", {"class" : "ins_storybody"})
        for news in ndtv_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        bloomberg_container = html_soup.findAll("div", {"class" : "body-copy"})
        for news in bloomberg_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        financialexp_container = html_soup.findAll("div", {"class" : "main-story-content"})
        for news in financialexp_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        indianexp_container = html_soup.findAll("div", {"class" : "full-details"})
        for news in indianexp_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        reuters_container = html_soup.findAll("div", {"class" : "StandardArticleBody_container_17wb1"})
        for news in reuters_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        thequint_container = html_soup.findAll("div", {"class" : "story-article__content__element--text"})
        for news in thequint_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        aninews_container = html_soup.findAll("div", {"class" : "content"})
        for news in aninews_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        zeebusiness_container = html_soup.findAll("div", {"class" : "field-item even"})
        for news in zeebusiness_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        firstpost_container = html_soup.findAll("div", {"class" : "article-full-content"})
        for news in firstpost_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        indianexpress_container = html_soup.findAll("div", {"class" : "articles"})
        for news in indianexpress_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)
        
        indiatoday_container = html_soup.findAll("div", {"class" : "description"})
        for news in indiatoday_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)
        
        news18_container = html_soup.findAll("div", {"class" : "paragraph"})
        for news in news18_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        # Daily news and Analysis
        dnaindia_container = html_soup.findAll("div", {"class" : "col-md-8"})
        for news in dnaindia_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        mensxp_container = html_soup.findAll("div", {"class" : "left-container  pull-left"})
        for news in mensxp_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        deccanchronicle_container = html_soup.findAll("div", {"id" : "storyBody"})
        for news in deccanchronicle_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

        timesnow_container = html_soup.findAll("div", {"class" : "ab_consumption_paras"})
        for news in timesnow_container:
            if news.text is not None:
                data['title'] = title
                data['url'] = url
                data['content'] = news.text.strip()
                full_data.append(data)

    except requests.exceptions.ConnectionError:
        print('ConnectionError')
    return full_data

if __name__ == '__main__':
    print('Google news scraper')