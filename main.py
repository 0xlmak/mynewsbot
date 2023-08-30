import feedparser
import telegram
#from config import telegram_token_news

def get_news_data(starting_url):
    news_data = []    
    response = feedparser.parse(starting_url)
    for entry in response.entries:
        data = {}
        data["title"] = entry.title
        data["link"] = entry.link
        data["author"] = entry.author
        data["time_published"] = entry.published
        data["tags"] = [tag.term for tag in entry.tags]
        data["authors"] = [author.name for author in entry.authors]
        data["summary"] = entry.summary
        news_data.append(data)

    return news_data
    

def get_msg(news_data):
    msg = "\n\n\n"
    for news_item in news_data[:3]:
        text = news_item["title"]
        link = news_item["link"]
        msg += text+'  [<a href="'+link+'">source</a>]'
        msg += "\n\n"
        
    return msg


bot = telegram.Bot(token="6457857348:AAEY32qJL8_U-igx7M85gqu3ZEW1udbRvqM")
url = "https://www.jeuneafrique.com/pays/cameroun/feed/"

news_data = get_news_data(url)
msg = get_msg(news_data)
#print(msg)
status = bot.send_message(chat_id="@newsbotnow", text=msg, parse_mode='HTML')        
if status:            
    print(status)
else:
    print("no new news")
