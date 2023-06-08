import tkinter as tk
from tkinter import Label
import requests
def getdata(canvas):
 url = "https://imdb8.p.rapidapi.com/title/find"
 name = textfeild.get()
 querystring = {"q":name}

 headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "274ce6002dmsh23a7b18ef246b51p10ae68jsn432857d9eb92"
    }

 response = requests.request("GET", url, headers=headers, params=querystring)

 data = response.json()

 info = data['results'][0]['runningTimeInMinutes']
 no_of_episodes = int(data['results'][0]['numberOfEpisodes'])

 sum = info * no_of_episodes
 final = sum/60

 FINAL_DATA="\n"+"Total Number of Episodes:- " + str(no_of_episodes) + "\n""\n" + "Duration of one Episode approx:- " + str(info) + " minutes" + "\n" + "Total time you need to BING WATCH:- " + str(final) + " hours"

 label1.config(text = FINAL_DATA)


canvas = tk.Tk()

canvas.geometry("1100x1000")
canvas.configure(bg="#FFFFE0")

canvas.title("Time SAVER")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfeild=tk.Entry( canvas,font=t)
textfeild.pack(pady=20)
textfeild.focus()
textfeild.bind('<Return>', getdata)

label1=tk.Label(canvas, font=t, fg="black",bg="#FFFFE0")
label1.pack()
label2=tk.Label(canvas, font=t, fg="black",bg="#FFFFE0")
label2.pack()
label3=tk.Label(canvas, font=t, fg="black",bg="#FFFFE0")
label3.pack()

canvas.mainloop()