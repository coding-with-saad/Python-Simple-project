import webbrowser

browser=webbrowser.get()

while True:
    url=input("enter the url")
    browser.open_new_tab(url)

