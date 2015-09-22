##!/usr/bin/env python
## -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.titleLabel = Label(self, text='一键猫呆联网器', width=12, font=("Arial", 19))
        self.titleLabel.grid(row = 0, column=1)
        self.btn0 = Button(self, text='12sjqin', width=8, command=lambda:self.selectUser(0))
        self.btn0.grid(row=1, column=0)
        self.btn1 = Button(self, text='12qliu2', width=8, command=lambda:self.selectUser(1))
        self.btn1.grid(row=1, column=1)
        self.btn2 = Button(self, text='12rhzeng', width=8, command=lambda:self.selectUser(2))
        self.btn2.grid(row=1, column=2)
        self.btn3 = Button(self, text='12ehluo', width=8, command=lambda:self.selectUser(3))
        self.btn3.grid(row=2, column=0)
        self.btn4 = Button(self, text='14ychen2', width=8, command=lambda:self.selectUser(4))
        self.btn4.grid(row=2, column=1)
        self.btn5 = Button(self, text='13zjye1', width=8, command=lambda:self.selectUser(5))
        self.btn5.grid(row=2, column=2)
        self.btn6 = Button(self, text='13xsliu', width=8, command=lambda:self.selectUser(6))
        self.btn6.grid(row=3, column=0)
        self.btn7 = Button(self, text='14zqlin', width=8, command=lambda:self.selectUser(7))
        self.btn7.grid(row=3, column=1)
        self.btn8 = Button(self, text='14zxhuang2', width=8, command=lambda:self.selectUser(8))
        self.btn8.grid(row=3, column=2)
        self.btn9 = Button(self, text='14jmwei', width=8, command=lambda:self.selectUser(9))
        self.btn9.grid(row=4, column=0)
        self.btn10 = Button(self, text='14mysun', width=8, command=lambda:self.selectUser(10))
        self.btn10.grid(row=4, column=1)
        self.btn11 = Button(self, text='14qma', width=8, command=lambda:self.selectUser(11))
        self.btn11.grid(row=4, column=2)
        self.btn12 = Button(self, text='14jwchen2', width=8, command=lambda:self.selectUser(12))
        self.btn12.grid(row=5, column=0)
        self.btn13 = Button(self, text='14sxfu', width=8, command=lambda:self.selectUser(13))
        self.btn13.grid(row=5, column=1)
        self.btn14 = Button(self, text='14jyhu2', width=8, command=lambda:self.selectUser(14))
        self.btn14.grid(row=5, column=2)
        self.btn15 = Button(self, text='14yyang1', width=8, command=lambda:self.selectUser(15))
        self.btn15.grid(row=6, column=0)
        self.btn16 = Button(self, text='14hlli3', width=8, command=lambda:self.selectUser(16))
        self.btn16.grid(row=6, column=1)
        self.btn17 = Button(self, text='13lwxie', width=8, command=lambda:self.selectUser(17))
        self.btn17.grid(row=6, column=2)
        self.btn18 = Button(self, text='13lxpeng', width=8, command=lambda:self.selectUser(18))
        self.btn18.grid(row=7, column=0)
        self.btn19 = Button(self, text='14qllei', width=8, command=lambda:self.selectUser(19))
        self.btn19.grid(row=7, column=1)
        self.btn20 = Button(self, text='14zxliang', width=8, command=lambda:self.selectUser(20))
        self.btn20.grid(row=7, column=2)
        self.curBtn = Button(self, text='流量', width=8, command=self.showCurrent)
        self.curBtn.grid(row=8, column=1)
        self.curBtn = Button(self, text='登出', width=8, command=self.logout)
        self.curBtn.grid(row=8, column=0)
        self.exitBtn = Button(self, text='退出', width=8, command=self.quit)
        self.exitBtn.grid(row=8, column=2)

    def logout(self):
        values = {
            'Logout': ''
        }
        data = urllib.urlencode(values)
        url = 'http://192.168.31.4:8080/?status=ok&url='
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        print 'Log Out'
        tkMessageBox.showinfo('提示', '已登出当前用户!')

    def showCurrent(self):
        url = 'http://192.168.31.4:8080/'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        responseStr = response.read()
        if not 'you have been logged out by another' in responseStr:
            currentTuple = self.getCurrent(responseStr)
            tkMessageBox.showinfo('提示', '流量查询: \n\n已使用流量:  %s 字节\n所拥有流量:  %s 字节' % (currentTuple[0], currentTuple[1]))
        else:
            tkMessageBox.showinfo('提示', '请先登入校园网!')
            
    def selectUser(self, id):
        if id == 0:
            self.link('12sjqin', 'pw139802')
        elif id == 1:
            self.link('12qliu2', 'pw138833')
        elif id == 2:
            self.link('12rhzeng', 'pw139629')
        elif id == 3:
            self.link('12ehluo', 'pw139478')
        elif id == 4:
            self.link('14ychen2', 'pw145907')
        elif id == 5:
            self.link('13zjye1', 'pw143060')
        elif id == 6:
            self.link('13xsliu', 'pw143889')
        elif id == 7:
            self.link('14zqlin', 'pw145929')
        elif id == 8:
            self.link('14zxhuang2', 'pw146806')
        elif id == 9:
            self.link('14jmwei', 'pw146514')
        elif id == 10:
            self.link('14mysun', 'pw146833')
        elif id == 11:
            self.link('14qma', 'pw147414')
        elif id == 12:
            self.link('14jwchen2', 'pw146784')
        elif id == 13:
            self.link('14sxfu', 'pw147028')
        elif id == 14:
            self.link('14jyhu2', 'pw147127')
        elif id == 15:
            self.link('14yyang1', 'pw146614')
        elif id == 16:
            self.link('14hlli3', 'pw147416')
        elif id == 17:
            self.link('13lwxie', 'pw143223')
        elif id == 18:
            self.link('13lxpeng', 'pw144090')
        elif id == 19:
            self.link('14qllei', 'pw146434')
        elif id == 20:
            self.link('14zxliang', 'pw146277')

    def getCurrent(self, responseStr):
        a1 = responseStr.split("id=\"ub\">")
        a2 = a1[1].split('</td>')
        used = a2[0]
        a3 = a2[3].split('id=\"tb\">')
        total = a3[1]
        return (used, total)

    def link(self, username, password):
        values = {
            'AuthenticateUser':username, 
            'AuthenticatePassword':password
        }
        data = urllib.urlencode(values)
        url = 'http://192.168.31.4:8080/?status=ok&url='
        request = urllib2.Request(url, data)
        try:
            response = urllib2.urlopen(request)
            responseStr = response.read()
            if not 'you have been logged out by another' in responseStr:
                print 'Log In'
                currentTuple = self.getCurrent(responseStr)
                tkMessageBox.showinfo('提示', '登录成功!\n\n用户:  %s\n已使用流量:  %s 字节\n所拥有流量:  %s 字节' % (username, currentTuple[0], currentTuple[1]))
            else:
                print 'Log Out'
                tkMessageBox.showinfo('提示', '已登出当前用户!  (请再次选择登入用户)')

        except urllib2.HTTPError, e:
            print e.code
            print e.reason
        except urllib2.URLError, e:
            print e.reason
            tkMessageBox.showinfo('提示', '登录失败!\n\n请确保缆线已插好!')


app = Application()
app.master.title('一键猫呆联网器v2')
app.mainloop()