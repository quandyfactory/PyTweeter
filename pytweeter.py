#!/usr/bin/env python

__title__ = 'PyTweeter: Post Status Updates to Twitter'
__version__ = 0.1
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/pyhtmledit/"
__copyright__ = "(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
This program lets you post status updates to twitter. That's pretty much it for now.
"""


try:
    file = open('config.ini', 'r')
    config = file.read()
    config = config.split('\n')
    for l in config:
        kv = l.split('=')
        key = kv[0].strip()
        value = kv[1].strip()
        if key == 'username':
            username = value
        elif key == 'password':
            password = value
    file.close()
except:
    username = ''
    password = ''



import twitter
from Tkinter import *
import tkMessageBox 

class App:
    def __init__(self,parent):

        f = Frame(parent)
        f.pack(padx=15, pady=15)

        self.username_label = Label(f, text="Username")
        self.username_label.pack(side=TOP, padx=10, pady=0)
        self.username = Entry(f, text="Username")
        self.username.pack(side=TOP, padx=10, pady=0)
        self.username.insert(0, username)
        
        self.password_label = Label(f, text="Password")
        self.password_label.pack(side=TOP, padx=10, pady=0)
        self.password = Entry(f, text="Password", show="*")
        self.password.pack(side=TOP, padx=10, pady=0)
        self.password.insert(0, password)

        self.status_label = Label(f, text="Status")
        self.status_label.pack(side=TOP, padx=10, pady=0)
        self.status = Text(f, width=36, height=4)
        self.status.pack(side=TOP, padx=10, pady=0)

        self.button = Button(f, text="Post Update", command=self.PostUpdate)
        self.button.pack(side=BOTTOM, padx=10, pady=10)

    def CheckLength(self):
        """
        Checks the length of a message
        """
        string = self.status.get()
        return string.length()

    def ConfigureApi(self):
        """
        Grabs the current username and password and configures the twitter api
        """
        username = self.username.get()
        password = self.password.get()
        return twitter.Api(username=username, password=password)

    def PostUpdate(self):
        """
        Posts an update to twitter and then calls the SetConfig function
        """
        api = self.ConfigureApi()
        tweet = self.status.get(1.0, END)
        api.PostUpdate(status=tweet)
        self.SetConfig()
        tkMessageBox.showinfo('Message Posted', 'Your message was posted to twitter.')
        self.status.delete(1.0, END)

    def SetConfig(self):
        """
        Sets a config file to save the username and password
        """
        output = 'username={username}\npassword={password}'.format(username = self.username.get(), password = self.password.get())
        file = open('config.ini', 'w')
        file.write(output)
        file.close()



root = Tk()
root.title(__title__)
app = App(root)
root.mainloop()

