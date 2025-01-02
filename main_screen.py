import tkinter as tk
from weather_lib import *

class Screen:
    def __init__(self):
        self.fontArial18 = ("Arial",18)
        self.root = tk.Tk()
        self.root.title("Consulta de temperatura")
        self.root.geometry("500x500")#Tamanho da janela

        self.testLabel = tk.Label(self.root, text="Insira a localização a ser pesquisada",font=self.fontArial18)
        self.testLabel.pack(padx=10,pady=10)

        self.place = tk.Entry(self.root)
        self.place.pack()

        self.fetchPlaceBtn = tk.Button(self.root, text="Pesquisar", command=self.getData)
        self.fetchPlaceBtn.pack()


        self.root.mainloop()


        #Funções

    def getData(self):
        self.url = fetchLocation(self.place.get())
        self.requestedData = resquestData(self.url)
        self.weatherLabel = tk.Label(self.root,text=self.requestedData.Daily().Variables(0).ValuesAsNumpy())
        self.weatherLabel.pack()
