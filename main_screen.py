import tkinter as tk
from weather_lib import *


class Screen:
    def __init__(self):

        #Screen Config
        self.root = tk.Tk()
        self.root.title("Consulta de temperatura")
        self.root.geometry("500x500")  #Tamanho da janela
        #row-column configure
        #self.root.rowconfigure(0,weight=10)
        #self.root.columnconfigure(0,weight=10)
        self.fontArial18 = ("Arial", 18)

        #Widgets
        #self.textLabel1 = tk.Label(self.root, text="Insira a localização a ser pesquisada", font=self.fontArial18)
        #self.textLabel1.grid(sticky=tk.EW,pady=10)

        self.textLabel2 = tk.Label(self.root,text="Localização: ",font=("TkDefaultFont",10))
        self.textLabel2.grid(row=0,column=0,stick=tk.W,padx=10,pady=10)

        self.place = tk.Entry(self.root)
        self.place.grid(row=0,column=1)

        self.daysLabel = tk.Label(self.root,text="Dias a serem previstos: ",font=("TkDefaultFont",10))
        self.daysLabel.grid(row=1,column=0,stick=tk.W,padx=10,pady=10)

        self.days = tk.Entry(self.root)
        self.days.grid(row=1,column=1)

        self.fetchPlaceBtn = tk.Button(self.root, text="Pesquisar", command=self.getData,font=("TkDefaultFont",10))
        self.fetchPlaceBtn.grid(row=5,column=3,stick=tk.SE)

        #Start
        self.root.mainloop()

        #Functions

    def getData(self):
        if self.place.get() != "" and 0 < int(self.days.get()) <= 16:
            self.coordenadas = fetchLocation(self.place.get())#Coordenadas
            self.params = weatherDailyParams(self.coordenadas,int(self.days.get()))
            self.data = resquestData(self.params)
            #self.weatherLabel = tk.Label(self.root, text=self.data.Daily().Variables(0).ValuesAsNumpy())
            #self.weatherLabel.grid()
            print(self.data.Daily().Variables(0).ValuesAsNumpy())
        else:
            print("Caixa de entrada vazia ou quantidade de dias invalidos")
