import requests
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import  messagebox





class CeviriApp(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("THT-Çeviri Programı")
        self.root.geometry("500x400")
        self.root.configure(bg="#10434B")

        self.txt = Label(self.root, text="Kelime", bg="#10434B",fg="white",font=('Courier New',12)).place(
            x=6,
            y=40,
        )
        self.entry = Entry(self.root, width=30)
        self.entry.place(
            x=76,
            y=42
        )

        self.btnSend = Button(self.root, text="Çevir",bd=3, width=10,font=('Comic Sans MS',9),command=self.RequestsTureng).place(
            x=76,
            y=80
        )
        self.btnCls = Button(self.root, text="Temizle", bd=3, width=10, font=('Comic Sans MS', 9),command=self.clearBtn).place(
            x=176,
            y=80
        )
        self.RequestsTureng()

        self.root.mainloop()

    def RequestsTureng(self):
        url = bs(requests.get(f"https://tureng.com/tr/turkce-ingilizce/{self.entry.get()}").content,"lxml").find_all("td",class_="tr ts",limit=1)
        for i in (url):
            messagebox.showinfo("Çeviri Sonucu", str(i.get_text()))

    def clearBtn(self):
        self.entry.delete(0, 'end')




if __name__ == "__main__":CeviriApp()