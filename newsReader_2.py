import requests
import json

def spk(str):
    from win32com.client import Dispatch
    spk = Dispatch("SAPI.SpVoice")
    spk.Speak(str)

if __name__ == '__main__':
   print("----------------------------------------------------------Top 5 NEWS FOR THE DAY ----------------------------------------------------------------")
   spk("welcome to news bot..... Listen today's top 5 news. ")

   url = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=f6372b28d4994aaa822e846cee5de4d0")
   news = requests.get(url).text
   news_dict = json.loads(news)
   #news_reader = news_dict['articles']
   for i in range(5):
       if i == 4:

           spk('this is the last news for the day. listen carefully.')
           print("News",i+1,"-",news_dict['articles'][i]['title'])
           spk(news_dict['articles'][i]['title'])
           print("For full article click on to the link-\n" , news_dict['articles'][i]['url'])
           spk('Thank you!. for listening')
           print("---------------------------------------------------------------------------------------------------------------------------------------------------")
           print("Thank you! for listening")

       else:

           print("News", i+1, "-", news_dict['articles'][i]['title'])
           spk(news_dict['articles'][i]['title'])
           print("For full article click on to the link-\n" , news_dict['articles'][i]['url'])
           spk('Now, moving toward another news headlines')

       print("---------------------------------------------------------------------------------------------------------------------------------------------------")



