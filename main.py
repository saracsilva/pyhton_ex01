import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid.")
    print("Download complete")


# System settings

customtkinter.set_appearance_mode("System")
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


# Download Button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)


# Run app

app.mainloop()
