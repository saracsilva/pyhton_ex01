import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure("")
        video.download()
        finishLabel.configure(text="Dowloaded!")
    except:
        finishLabel.configure(text="Youtube link is invalid.", text_color="red")


# System settings

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements

title = customtkinter.CTkLabel(app, text="Insert an youtube link")
title.pack(padx=10, pady=10)

# Link Input

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Progress percentage

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.5)
progressBar.pack(padx=10, pady=10)

# Finished download

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()


# Download Button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app

app.mainloop()
