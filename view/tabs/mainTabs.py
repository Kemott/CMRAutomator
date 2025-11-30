from tkinter import *
from tkinter import ttk
import view.frames.tabsFrame as frame
import model.CMR as cmr

class MainTabs(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.addTabs()

    def addTabs(self):
        # Partia do usunięcia, wstawiona testowo
        test1 = cmr.CMR()
        test1.direction = "LPP_GDANSK"
        test1.car = "W1DHLEV"
        test1.trailer = "PZ3H223"
        test1.contentsLines = ["2 PALETY ZWROTÓW", "+ 2 PUSTE PALETY"]
        test1.carrierLines = ["JTD LOGISTIK", "Paprotnia 81 98-161 Zapolice"]
        test1.carriersCommentsLines = ["PRZESYŁKI KURIERSKIE"]
        test1.createName()

        test2 = cmr.CMR()
        test2.direction = "LPP_SERED"
        test2.car = "W2DHLEV"
        test2.trailer = "PZ3H258"
        test2.contentsLines = ["30 PALLETS"]
        test2.carrierLines = ["JTD LOGISTIK", "Paprotnia 81 98-161 Zapolice"]
        test2.carriersCommentsLines = ["PRZESYŁKI KURIERSKIE"]
        test2.createName()

        test3 = cmr.CMR()
        test3.direction = "LPP_JASIONKA"
        test3.car = "W3DHLEV"
        test3.containers = ["123456", "789012"]
        test3.contentsLines = ["LUŹNE PACZKI", "CONTAINERS: 123456, 789012"]
        test3.carrierLines = ["JTD LOGISTIK", "Paprotnia 81 98-161 Zapolice"]
        test3.carriersCommentsLines = ["PRZESYŁKI KURIERSKIE"]
        test3.createName()

        test4 = cmr.CMR()
        test4.direction = "LT"
        test4.car = "W4DHLEV"
        test4.trailer = "BI1234"
        test4.contentsLines = ["32 PALLETS"]
        test4.createName()

        test5 = cmr.CMR()
        test5.direction = "PANTERA"
        test5.car = "W5DHLEV"
        test5.trailer = "BI5678"
        test5.contentsLines = ["Vom Gateway Robakowo/PL:", "Pal. LV: 5", "Pal. EE: 10", "Pal. LT: 17", "", "Movement ID: DD6988A"]
        test3.carrierLines = ["Spedition Servisco / Sp zo.o.", "Ul. Komornicka 16", "PL-62-052 Komorniki Głuchowo"]
        test5.createName()
        # Koniec partii do usunięcia

        toBeCompletedFrame = frame.TabsFrame(self, data=[test1.getListText(), test2.getListText(), test3.getListText(), test4.getListText(), test5.getListText()])
        completedFrame = frame.TabsFrame(self)
        archiveFrame = frame.TabsFrame(self)

        self.add(toBeCompletedFrame, text="Dane do uzupełnienia")
        self.add(completedFrame, text="Dane uzupełnione")
        self.add(archiveFrame, text="Archiwum")
        
