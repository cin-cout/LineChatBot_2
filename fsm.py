from transitions.extensions import GraphMachine

from utils import send_text_message, shownews, send_button_message, send_image, show_intro

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_news(self, event):
        text = event.message.text
        return text.lower() == "news"

    def is_going_to_parties(self, event):
        text = event.message.text
        return text.lower() == "introduction of political parties"

    def is_going_to_dpp(self, event):
        text = event.message.text
        return text.lower() == "dpp"

    def is_going_to_kmt(self, event):
        text = event.message.text
        return text.lower() == "kmt"

    def is_going_to_tpp(self, event):
        text = event.message.text
        return text.lower() == "tpp"

    def is_going_to_npp(self, event):
        text = event.message.text
        return text.lower() == "npp"

    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "intro"
    
    def is_going_to_yuan(self, event):
        text = event.message.text
        return text.lower() == "yuan"

    def is_going_to_leg(self, event):
        text = event.message.text
        return text.lower() == "leg"

    def is_going_to_exe(self, event):
        text = event.message.text
        return text.lower() == "exe"

    def is_going_to_exa(self, event):
        text = event.message.text
        return text.lower() == "exa"

    def is_going_to_con(self, event):
        text = event.message.text
        return text.lower() == "con"

    def is_going_to_jud(self, event):
        text = event.message.text
        return text.lower() == "jud"

    def on_enter_news(self, event):
        print("I'm entering news")
        shownews(event.reply_token)
        self.go_back(event)

    def on_enter_parties(self, event):
        print("I'm entering parties")
        reply_token = event.reply_token
        img = 'https://cnews.com.tw/wp-content/uploads/2022/03/noname-4.jpg'
        title = '政黨總攬:'
        uptext = '想了解哪一個政黨?'
        texts = ['DPP', 'KMT', 'TPP', 'NPP']
        labels = ['民主進步黨', '中國國民黨', '台灣民眾黨', '時代力量']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_dpp(self, event):
        print("I'm entering dpp")
        userid = event.source.user_id
        img = 'https://upload.wikimedia.org/wikipedia/zh/thumb/c/c1/Emblem_of_Democratic_Progressive_Party_%28new%29.svg/1200px-Emblem_of_Democratic_Progressive_Party_%28new%29.svg.png'
        send_image(userid, img)
        url = 'https://zh.wikipedia.org/wiki/%E6%B0%91%E4%B8%BB%E9%80%B2%E6%AD%A5%E9%BB%A8'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_kmt(self, event):
        print("I'm entering kmt")
        userid = event.source.user_id
        img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Emblem_of_the_Kuomintang.svg/1200px-Emblem_of_the_Kuomintang.svg.png'
        send_image(userid, img)
        url = 'https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9C%8B%E5%9C%8B%E6%B0%91%E9%BB%A8'
        show_intro(userid, url)
        self.back_user(event)
    
    def on_enter_tpp(self, event):
        print("I'm entering tpp")
        userid = event.source.user_id
        img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Emblem_of_Taiwan_People%27s_Party_2019.svg/1200px-Emblem_of_Taiwan_People%27s_Party_2019.svg.png'
        send_image(userid, img)
        url = 'https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%B0%91%E7%9C%BE%E9%BB%A8_(2019%E5%B9%B4)'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_npp(self, event):
        print("I'm entering npp")
        userid = event.source.user_id
        img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Emblem_of_New_Power_Party.svg/1200px-Emblem_of_New_Power_Party.svg.png'
        send_image(userid, img)
        url = 'https://zh.wikipedia.org/wiki/%E6%99%82%E4%BB%A3%E5%8A%9B%E9%87%8F'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_intro(self, event):
        print("I'm entering intro")
        reply_token = event.reply_token
        text = "祝你順利成為政治小能手!!!\n以下為不同功能對應之關鍵字:\n\n功能介紹 : intro\n政黨介紹 : introduction of political parties\n臺灣五院介紹 : introduction of each yuan\n最新政治新聞 : news"
        send_text_message(reply_token, text)
        self.go_back(event)

    def on_enter_yuan(self, event):
        print("I'm entering yuan")
        reply_token = event.reply_token
        img = 'http://www.taiwan.net.tw/userfiles/image/mobile_2013/flag.png'
        title = '臺灣五院:'
        uptext = '想了解哪一個院?'
        texts = ['Leg', 'Exe', 'Exa', 'Con', 'Jud']
        labels = ['立法院', '行政院', '考試院', '監察院', '司法院']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_leg(self, event):
        print("I'm entering leg")
        userid = event.source.user_id
        url = 'https://zh.wikipedia.org/zh-cn/%E7%AB%8B%E6%B3%95%E9%99%A2'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_exe(self, event):
        print("I'm entering exe")
        userid = event.source.user_id
        url = 'https://zh.wikipedia.org/zh-cn/%E8%A1%8C%E6%94%BF%E9%99%A2'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_exa(self, event):
        print("I'm entering exa")
        userid = event.source.user_id
        url = 'https://zh.wikipedia.org/zh-cn/%E8%80%83%E8%A9%A6%E9%99%A2'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_con(self, event):
        print("I'm entering con")
        userid = event.source.user_id
        url = 'https://zh.wikipedia.org/wiki/%E7%9B%A3%E5%AF%9F%E9%99%A2'
        show_intro(userid, url)
        self.back_user(event)

    def on_enter_jud(self, event):
        print("I'm entering jud")
        userid = event.source.user_id
        url = 'https://zh.wikipedia.org/wiki/%E5%8F%B8%E6%B3%95%E9%99%A2'
        show_intro(userid, url)
        self.back_user(event)
    


