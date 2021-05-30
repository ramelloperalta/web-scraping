#Scrapes images off the front page of r/food


import scrapy

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    start_urls = ['https://www.reddit.com/r/food']
    
    def parse(self, response):
        links = response.xpath('//img/@src') #takes link attributes using xpath
        html = ''
        
        for link in links:
            url = link.get() 
            
            #does url have image?
            if any(extension in url for extension in ['.jpg', '.gif', '.png']):
                html += f'''<a href='{url}'target='_blank'><img src='{url}'
                height='33%' width='33%'/><a/>'''
                
                with open('frontpage.html', 'a') as page:
                    page.write(html)
