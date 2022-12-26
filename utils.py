import os
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, MessageTemplateAction, TemplateSendMessage, ButtonsTemplate, CarouselColumn, URITemplateAction, CarouselTemplate, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_news_carousel(reply_token, imglinks, titles, links):

    cols = []
    for i in range(5):
        cols.append(
            CarouselColumn(
                thumbnail_image_url=imglinks[i],
                title='臺灣政治新聞',
                text=titles[i],
                actions=[
                    URITemplateAction(
                        label='Read more',
                        uri=links[i]
                    )
                ]
            )
        )

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=cols)
    )

    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_image(id, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, message)

    return "OK"

def show_intro(id, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    text = soup.find('p').getText()
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text=text))


def shownews(reply_token):
    url = 'https://www.chinatimes.com/realtimenews/260407/?chdtv'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    imglinks = []
    titles = []
    links = []

    news = soup.find_all('div', class_='articlebox-compact')
    for new in news[:5]:
        img = new.find('img', class_='photo')
        title = new.find('h3', class_='title').getText()
        imglink = img['src']
        link = url
        imglinks.append(imglink)
        titles.append(title)
        links.append(link)

    send_news_carousel(reply_token, imglinks, titles, links)

def send_button_message(reply_token, img, title, uptext, labels, texts):

    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"
