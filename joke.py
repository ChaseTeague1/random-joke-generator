import requests
import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

#Create function that gets new joke
def get_new():
    url = "https://icanhazdadjoke.com/"

    headers = {
        'Accept' : 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        joke = data['joke']
        joke_label.config(text=joke)
    else:
        joke_label.config(text="Could not fetch joke")

joke_label = tk.Label(root, text="Click the button to get a joke!", wraplength=300, width=60, height=5, anchor='center')
joke_label.pack(pady=20)

joke_button = tk.Button(root, text="Get a Joke", command=get_new)
joke_button.pack(pady=10)

root.title("Random Joke Generator")
root.mainloop()