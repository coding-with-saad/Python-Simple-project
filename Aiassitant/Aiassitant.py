import tkinter as tk
from tkinter import Entry,Label,Button
import webbrowser

root=tk.Tk()

root.title("Your Ai Assitant")
root.configure(bg="sea green")

def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)



def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)



def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_instagram():
    Username=entry.get().replace('@',"")
    url=f"www.instagram.com/{Username}/"
    webbrowser.open(url)


Label(root,text="enter your command:").pack(pady=10)

entry=Entry(root,width=50)
entry.pack(pady=10)


Button(root,text="search on youtube",command=search_youtube).pack(pady=5)
Button(root,text="search on google",command=search_google).pack(pady=5)
Button(root,text="search on instagram",command=search_instagram).pack(pady=5)

root.mainloop()

