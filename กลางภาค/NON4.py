import tkinter as tk
from tkinter import*
from pytube import YouTube
from tkinter import messagebox, filedialog


def Widget():
    link_label = Label(root, text="YouTube Link :",
                       bg="#789CCE")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable="video_link")
    root.linkText.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    destination_label = Label(root, text="Destination :",
                              bg="#789CCE")
    destination_label.grid(row=2, column=0, padx=5, pady=5,)

    root.destinationText = Entry(root,
                                 width=40, textvariable="Dowload_Path")
    root.destinationText.grid(row=2, column=1, padx=5, pady=5)

    browse_B = Button(root,
                      text="Browse",
                      command=BROWSE,
                      width=10,
                      bg="#789CCE")
    browse_B.grid(row=2, column=2, pady=1, padx=1)

    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="#789CCE")
    Download_B.grid(row=3, column=1, pady=3, padx=3)


def Brown():
    download_Directory = filedialog.askdirectory(
        initialdir=" ที่อยู่ของโฟร์เดอร์")

    download_Path.set(download_Directory)


def Download():
    YouTube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(YouTube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWALOADED AND SAVED IN \n" + download_Folder)


root = tk.Tk()

root.geometry("500x100")
root.resizable(False, False)
root.title("ดาวน์โหลดวิดีโอด้วยลิ้งค์ YouTube by Subbarung-k")
root.config(bg="#000000")

video_Link = StringVar()
Download_Path = StringVar()

Widget()
root.mainloop()
