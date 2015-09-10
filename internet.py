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
		self.titleLabel = Label(self, text='一键联网器', width=8, font=("Arial", 19))
		self.titleLabel.grid(row = 0, column=1)
		self.btn0 = Button(self, text='14jhwang', width=8, command=lambda:self.selectUser(0))
		self.btn0.grid(row=1, column=0)
		self.btn1 = Button(self, text='14ktyang', width=8, command=lambda:self.selectUser(1))
		self.btn1.grid(row=1, column=1)
		self.btn2 = Button(self, text='14jyzhou', width=8, command=lambda:self.selectUser(2))
		self.btn2.grid(row=1, column=2)
		self.btn3 = Button(self, text='14dhuang', width=8, command=lambda:self.selectUser(3))
		self.btn3.grid(row=2, column=0)
		self.btn4 = Button(self, text='14jrlei', width=8, command=lambda:self.selectUser(4))
		self.btn4.grid(row=2, column=1)
		self.btn5 = Button(self, text='14hlfu', width=8, command=lambda:self.selectUser(5))
		self.btn5.grid(row=2, column=2)
		self.btn6 = Button(self, text='14rmguan', width=8, command=lambda:self.selectUser(6))
		self.btn6.grid(row=3, column=0)
		self.btn7 = Button(self, text='14jygao', width=8, command=lambda:self.selectUser(7))
		self.btn7.grid(row=3, column=1)
		self.btn8 = Button(self, text='14lxlu', width=8, command=lambda:self.selectUser(8))
		self.btn8.grid(row=3, column=2)
		self.btn9 = Button(self, text='14ypmo', width=8, command=lambda:self.selectUser(9))
		self.btn9.grid(row=4, column=0)
		self.btn10 = Button(self, text='14hlhuang', width=8, command=lambda:self.selectUser(10))
		self.btn10.grid(row=4, column=1)
		self.curBtn = Button(self, text='流量', width=8, command=self.showCurrent)
		self.curBtn.grid(row=5, column=1)
		self.curBtn = Button(self, text='登出', width=8, command=self.logout)
		self.curBtn.grid(row=5, column=0)
		self.exitBtn = Button(self, text='退出', width=8, command=self.quit)
		self.exitBtn.grid(row=5, column=2)

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
			self.link('14jhwang', 'diaonilaomao')
		elif id == 1:
			self.link('14ktyang', 'diaonilaomao')
		elif id == 2:
			self.link('14jyzhou', 'diaonilaomao')
		elif id == 3:
			self.link('14dhuang', 'pw146369')
		elif id == 4:
			self.link('14jrlei', 'pw146397')
		elif id == 5:
			self.link('14hlfu', 'pw146148')
		elif id == 6:
			self.link('14rmguan', 'pw146013')
		elif id == 7:
			self.link('14jygao', 'pw146407')
		elif id == 8:
			self.link('14lxlu', 'pw145944')
		elif id == 9:
			self.link('14ypmo', 'pw146365')
		elif id == 10:
			self.link('14hlhuang', 'pw146391')

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
app.master.title('一键联网器 beta版')
app.mainloop()
