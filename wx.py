# encoding:utf-8

import itchat, web, bill, _thread

itchat.auto_login()

@itchat.msg_register('Text')
def text_reply(msg):
    print(msg)
    if msg['Text'] == '记账':
        return u'《购买明细》:\n[金额]:\n[物品]:\n'
    if '《购买明细》:' in msg['Text']:
        msgText = msg['Text']
        time = msg['CreateTime']
        amount = msgText[msgText.index('[金额]:') + 4 : msgText.index('[物品]:')]
        items =  msgText[msgText.index('[物品]:') + 4 :]
        print('金额:', amount)
        print('物品', items)

class wxSendMsg:
    def GET(self):
        data = web.input()
        itchat.send_msg('hh', '@9a4342ec09c017305cd658d24984212310d28ce9d27b6d83fb814268fd2fee75')

def startWeb(self):
    urls = ("/wechatMsg", "wxSendMsg")
    app = web.application(urls, globals())
    app.run()

if __name__ == "__main__":
    _thread.start_new_thread(startWeb, ('thread',))

    itchat.run()