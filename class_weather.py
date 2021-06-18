import json
import requests
import tkinter as tk
from PIL import Image, ImageTk

class Weather:

    def __init__(self, city):
        self.city = city
        self.s = requests.Session()


    def request(self):
        self.s.headers.update({"User-Agent": "Test.2",
                                "From": "skippern23@gmail.com"})
        
    
    def get(self):
        req = self.s.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=4&lat=59&lon=9")
        print(req.status_code)
        data_dump = req.text
        self.langesund = json.loads(data_dump)
        #return self.langesund
    
    def output(self):
      weather_data = self.langesund["properties"]["timeseries"][3]["data"]["instant"]["details"]["air_temperature"]

      #label = tk.Label(root, text="The current air temperature for Langesund is:" + weather_data)
      #label.pack()
      print("The current air temperature for Langesund is:", weather_data)

        #print(langesund["type"])


city = Weather("Langesund")
city.request()
#city.get()
#city.output()

class simpleGUI:
  def __init__(self, master):
    #HEIGHT = 500
    #WIDTH = 600
    self.master = tk.Canvas(height=500, width=600)
    self.master.pack()
    #master.tk.Canvas("Simple GUI")

    self.img = ImageTk.PhotoImage(Image.open("langesund.png"))
    self.label_img = tk.Label(master, image=self.img)
    self.label_img.place(relwidth=1, relheight=1)

    self.frame = tk.Frame(bd=5)
    self.frame.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor="n")

    self.req_button = tk.Button(self.frame, text="Request weather", font=50, command=lambda: city.get())
    self.req_button.pack()#relx=0.7, relheight=1, relwidth=0.3)

    self.print_button = tk.Button(self.frame, text="Print weather", font=50, command=lambda: city.output())
    self.print_button.pack()#(relx=3, relheight=1, relwidth=0.3)


root = tk.Tk()
my_gui = simpleGUI(root)
root.mainloop()






# print(req.request.headers)
# for summary in data_dump:
#     sum_sum = summary["summary"]
#     print(sum_sum)


