from PyQt5 import QtWidgets
import sys
import random
import requests
from bs4 import BeautifulSoup

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.baslik = QtWidgets.QLabel("Film Seçme Sihirbazına Hoşgeldiniz!\nAşağıdaki İşlemleri Uygulayarak İzleyeceğiniz Filmi Bulun!")
        self.action = QtWidgets.QRadioButton("Aksiyon")
        self.adventure = QtWidgets.QRadioButton("Macera")
        self.sci = QtWidgets.QRadioButton("Bilim-Kurgu")
        self.comedy = QtWidgets.QRadioButton("Komedi")
        self.rating = QtWidgets.QLineEdit()
        self.label = QtWidgets.QLabel("En Düşük Puan:")

        self.buton = QtWidgets.QPushButton("İzleyeceğin Filmi Bul")
        self.buton3 = QtWidgets.QPushButton("Rastgele Seç")
        self.buton2 = QtWidgets.QPushButton("Çıkış Yap")

        x = QtWidgets.QHBoxLayout()
        x.addWidget(self.buton)
        x.addWidget(self.buton3)
        x.addWidget(self.buton2)

        a = QtWidgets.QHBoxLayout()
        a.addWidget(self.action)
        a.addWidget(self.adventure)

        b = QtWidgets.QHBoxLayout()
        b.addWidget(self.sci)
        b.addWidget(self.comedy)

        c = QtWidgets.QHBoxLayout()
        c.addWidget(self.label)
        c.addWidget(self.rating)

        d = QtWidgets.QHBoxLayout()
        d.addWidget(self.label)
        d.addWidget(self.rating)

        y = QtWidgets.QVBoxLayout()
        y.addWidget(self.baslik)
        y.addLayout(d)
        y.addLayout(a)
        y.addLayout(b)
        y.addLayout(c)
        y.addLayout(x)

        self.buton.clicked.connect(lambda : self.click(self.action.isChecked(),self.adventure.isChecked(),self.comedy.isChecked(),self.sci.isChecked()))
        self.buton2.clicked.connect(self.click2)
        self.buton3.clicked.connect(self.click2)

        self.setLayout(y)
        self.setGeometry(400,400,250,250)
        self.setWindowTitle("Film Seçme Sihirbazı")
        self.show()

    def click(self,action,adventure,comedy,sci):

        if action:
            self.aksiyon()

        if adventure:
            self.macera()

        if comedy:
            self.komedi()

        if sci:
            self.bilim()


    def click2(self):
        sender = self.sender()

        if sender.text() == "Çıkış Yap":
            QtWidgets.qApp.quit()

        elif sender.text() == "Rastgele Seç":
            self.rastgele()

    def rastgele(self):

        url =  "https://www.imdb.com/chart/top"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik,"html.parser")

        basliklar = list()
        deger = list()
        deger2 = list()

        baslik = soup.find_all("td",{"class":"titleColumn"})
        degerler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

        for a,b in zip(baslik,degerler):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            basliklar.append(a)
            deger.append(b)

        for a in deger:
            a = float(a)
            deger2.append(a)

        if (self.rating.text() == ""):
            x = random.randint(0,249)
            self.baslik.setText("{} = {}\nİyi Seyirler!".format(basliklar[x],deger[x]))

        else:
            while True:
                y = random.randint(0,249)

                if (deger2[y] > float(self.rating.text()) or deger2[y] == float(self.rating.text())):
                    self.baslik.setText("{} = {}\nİyi Seyirler!".format(basliklar[y],deger2[y]))
                    break

                else:
                    continue

    def macera(self):

        url = "https://www.imdb.com/search/title/?genres=adventure&groups=top_250&view=simple&sort=user_rating,desc&ref_=adv_prv"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik,"html.parser")

        basliklar = soup.find_all("div",{"class":"col-title"})
        degerler = soup.find_all("div",{"class":"col-imdb-rating"})

        bas = list()
        deg = list()
        deg2 = list()

        for a,b in zip(basliklar,degerler):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            bas.append(a)
            deg.append(b)

        url = "https://www.imdb.com/search/title/?genres=adventure&groups=top_250&view=simple&sort=user_rating,desc&start=51&ref_=adv_nxt"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik, "html.parser")

        x = soup.find_all("div", {"class": "col-title"})
        y = soup.find_all("div", {"class": "col-imdb-rating"})

        for a,b in zip(x,y):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            bas.append(a)
            deg.append(b)

        for a in deg:
            a = float(a)
            deg2.append(a)

        while True:
            r = random.randint(0,56)

            if (deg2[r] > float(self.rating.text()) or deg2[r] == float(self.rating.text())):
                self.baslik.setText("{} = {}\nİyi Seyirler!".format(bas[r], deg2[r]))
                break

            else:
                continue

    def aksiyon(self):

        url = "https://www.imdb.com/search/title/?genres=action&groups=top_250&sort=user_rating,desc&view=simple"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik,"html.parser")

        basliklar = soup.find_all("div",{"class":"col-title"})
        degerler = soup.find_all("div",{"class":"col-imdb-rating"})

        bas = list()
        deg = list()
        deg2 = list()

        for a,b in zip(basliklar,degerler):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            bas.append(a)
            deg.append(b)

        for a in deg:
            a = float(a)
            deg2.append(a)

        while True:

            x = random.randint(0,37)

            if (deg2[x] > float(self.rating.text()) or deg2[x] == float(self.rating.text())):
                self.baslik.setText("{} = {}\nİyi Seyirler!".format(bas[x], deg2[x]))
                break

            else:
                continue

    def komedi(self):

        url = "https://www.imdb.com/search/title/?genres=comedy&groups=top_250&sort=user_rating,desc&view=simple"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik,"html.parser")

        basliklar = soup.find_all("div",{"class":"col-title"})
        degerler = soup.find_all("div",{"class":"col-imdb-rating"})

        bas = list()
        deg = list()
        deg2 = list()

        for a,b in zip(basliklar,degerler):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            bas.append(a)
            deg.append(b)

        for a in deg:
            a = float(a)
            deg2.append(a)

        while True:

            x = random.randint(0,41)

            if (deg2[x] > float(self.rating.text()) or deg2[x] == float(self.rating.text())):
                self.baslik.setText("{} = {}\nİyi Seyirler!".format(bas[x], deg2[x]))
                break

            else:
                continue

    def bilim(self):

        url = "https://www.imdb.com/search/title/?genres=sci-fi&groups=top_250&sort=user_rating,desc&view=simple"
        response = requests.get(url)
        icerik = response.content
        soup = BeautifulSoup(icerik,"html.parser")

        basliklar = soup.find_all("div",{"class":"col-title"})
        degerler = soup.find_all("div",{"class":"col-imdb-rating"})

        bas = list()
        deg = list()
        deg2 = list()

        for a,b in zip(basliklar,degerler):

            a = a.text
            a = a.strip()
            a = a.replace("\n"," ")

            b = b.text
            b = b.strip()
            b = b.replace("\n"," ")

            bas.append(a)
            deg.append(b)

        for a in deg:
            a = float(a)
            deg2.append(a)

        while True:

            x = random.randint(0,29)

            if (deg2[x] > float(self.rating.text()) or deg2[x] == float(self.rating.text())):
                self.baslik.setText("{} = {}\nİyi Seyirler!".format(bas[x], deg2[x]))
                break

            else:
                continue


























app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())



