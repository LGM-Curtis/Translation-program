"""
Author:Curtis
Time:2018.07-2018.10
这是一个简单的翻译程序，默认是中英互译，但是在翻译内容框中输入非中文语言，翻译结果为中文。
"""
import json
from tkinter import *
import requests


def fany():
    content = entry1.get().strip()
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        'i': content,
        'doctype': 'json'
    }
    r = requests.post(url, data=data)
    ret = r.content.decode()
    result = json.loads(ret)
    # print(result)
    res.set(result['translateResult'][0][0]['tgt'])
    # print(content)

master = Tk()
master.title('翻译&Translation')
# 小x,非大X
master.geometry('500x300+100+300')
# 设置标签
Label(master, text="输入内容：", font=('GB2312', 18), fg='blue').grid(row=0, column=0)
Label(master, text="翻译结果：", font=('GB2312', 18), fg='blue').grid(row=1, column=0)

# 设置文本框
entry1 = Entry(master, font=('GB2312', 18))
entry1.grid(row=0, column=1)

res = StringVar()
entry2 = Entry(master, font=('GB2312', 18), textvariable=res)
entry2.grid(row=1, column=1)
# 设置按钮
Button(master, text="翻译", width=10, font=('GB2312', 18), command=fany).grid(row=2, column=0, sticky=W)
Button(master, text="退出", width=0, font=('GB2312', 18), command=master.quit).grid(row=2, column=1, sticky=E)

master.mainloop()