# -*-coding: Utf-8 -*-

## MODULES IMPORTER ##
import os, sys, socket
from tkinter import *
from tkinter.messagebox import *


class Application(Tk):
    def connection(self, event):
        self.HOST = self.ent.get()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.HOST, 19111))
            self.msgServeur_1 = self.sock.recv(1024).decode("Utf8")
            showinfo("Connection", self.msgServeur_1)
        except socket.error:
            if askyesno("Error", u"Error socket. Verifier le host et Relancer?"):
                return self.connection
            else:
                sys.exit

    def chat(self, event):
        """Evenement clavier"""
        msgClient = self.msgClient
        self.sock.send(msgClient.get().encode("Utf8"))
        self.frome()

    """Interface graphique"""

    def __init__(self, ):
        Tk.__init__(self, )
        self['bg'] = "black"
        self.title("Client Socket")
        self.iconbitmap('icon.ico')
        self.value_1 = StringVar()
        self.value_2 = StringVar()
        self.value_1.set("")
        self.value_2.set("")
        # Entry
        self.ent = Entry(self, width=31, selectbackground="royal blue", textvariable=self.value_1, font="Cambria 9")
        self.ent.bind("<Return>", self.connection)
        self.ent.pack(padx=1, pady=2)
        # Canvas
        self.can = Canvas(self, width=711, height=311, bg="red")
        txt = self.can.create_text(355, 18, text="Lamine", font="Lucida 15", fill="black")
        self.can.pack(padx=6, pady=6)
        # Entry
        self.msgClient = Entry(self, width=71, selectbackground="royal blue", textvariable=self.value_2,
                               font="Cambria 10")
        self.msgClient.bind("<Return>", self.chat)
        self.msgClient.pack(padx=4, pady=4)

    def frome(self):
        self.Msg_S = self.sock.recv(1024).decode("Utf8")


if __name__ == '__main__':
    app = Application()
    app.mainloop()