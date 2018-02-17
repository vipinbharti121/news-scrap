from bs4 import BeautifulSoup
import requests

# Change the company name, you want news for
company_name = 'tcs'
base_url = "https://news.google.com/news/search/section/q/"
follow_url = '?hl=en-IN&gl=IN&ned=in'
full_url = base_url + company_name + '/' + company_name + follow_url

txtfile_name = company_name + '.txt'

def get_urls(full_url):
    # Fetching all news article urls from google news site
    links = []
    try:
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        #Get all links from google news
        link_container = soup.findAll("a", {"class" : "nuEeue hzdq5d ME7ew"})
        for link in link_container:
            links.append(link['href'])
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
    return links

def get_news(article_url):
    try:
        response = requests.get(article_url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        '''
        EconomicsTime div{"class" : "Normal"}
        HindustanTimes div{"class" : "story-details"}
        NDTV div{"class" : "ins_storybody"}
        Livemint div{"class" : "content"}
        ANINews div{"class" : "content"})
        TimesOfIndia div{"class" : "Normal"}
        Bloomberg div{"class" : "body-copy"}
        FinancialExpress div{"class" : "main-story-content"}
        IndianExpress div{"class" : "full-details"})
        Reuters div{"class" : "StandardArticleBody_container_17wb1"})
        TheQuint div{"class" : "story-article__content__element--text"})
        ZeeBusiness div{"class" : "field-item even"})
        FirstPost div{"class" : "article-full-content"})

        '''
        f= open(txtfile_name,"a+")

        ec_container = html_soup.findAll("div", {"class" : "Normal"})
        for news in ec_container:
            # print(news.text)
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        hindustan_container = html_soup.findAll("div", {"class" : "story-details"})
        for news in hindustan_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        ndtv_container = html_soup.findAll("div", {"class" : "ins_storybody"})
        for news in ndtv_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        bloomberg_container = html_soup.findAll("div", {"class" : "body-copy"})
        for news in bloomberg_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        financialexp_container = html_soup.findAll("div", {"class" : "main-story-content"})
        for news in financialexp_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        indianexp_container = html_soup.findAll("div", {"class" : "full-details"})
        for news in indianexp_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        reuters_container = html_soup.findAll("div", {"class" : "StandardArticleBody_container_17wb1"})
        for news in reuters_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        thequint_container = html_soup.findAll("div", {"class" : "story-article__content__element--text"})
        for news in thequint_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        aninews_container = html_soup.findAll("div", {"class" : "content"})
        for news in aninews_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        zeebusiness_container = html_soup.findAll("div", {"class" : "field-item even"})
        for news in zeebusiness_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        firstpost_container = html_soup.findAll("div", {"class" : "article-full-content"})
        for news in firstpost_container:
            if news.text is not None:
                f.write('article :\n')
                f.write(article_url)
                f.write(news.text.strip())

        f.close()
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
    # print(response.text)
    return "success"

if __name__ == '__main__':

    print("Scrapping all news article links related to " + company_name)
    all_links = get_urls(full_url)
    print("Got all links")
    for link in all_links:
        print("Fetching news from "+ link)
        get_news(link)
    print("execution complete")
