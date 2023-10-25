from tkinter import*
from tkinter import filedialog
from pytube import YouTube


root = Tk()


def brw():
    drictory = filedialog.askdirectory(title = "Save video")
    et2.delete(0 , "end")
    et2.insert(0 , drictory)
def dwl():
    status.config(text = "Status : downloading .....")
    link = et1.get()
    folder = et2.get()
    YouTube(link , on_complete_callback = fnish).streams.filter(progressive = True , file_extension = "mp4").order_by("resolution").desc().first().download(folder)
def fnish(stream=None , chunk=None ,file_handle=None , remaining=None):
    status.config(text = "Status : complete")
#youtube logo
ytlogo = PhotoImage(file = "c:\\Users\\anase\\OneDrive\\Desktop\\course.py\\download (1).png")
ytlabel = Label(root , image = ytlogo)
ytlabel.place(x = 280 , y = 30)
#window name
root.title("YouTube video downloader")
root.geometry("800x600")
#labels
label = Label(text = "Video link")
label.place(x = 110 , y = 290)
label2 = Label( text = "Folder link")
label2.place(x = 110 , y = 320)
#video link 
et1 = Entry(width = 75)
et1.place(x = 180 , y = 290)
#download button
btn1 = Button(text = "Download" , font = "Aharoni" , bg = "red" , fg = "white" , pady = 5 , command = dwl )
btn1.place(x = 360 , y = 360)
#folder label
label1 = Label(text = "Folder Link")
#folder link
et2 = Entry(width = 60)
et2.place(x = 180 , y = 320)
#browse button
btn = Button(text = "Browse" , command = brw)
btn.place(x = 560 , y = 315 )
#status
status = Label(text = "status : Ready" , fg = "black" , bg = "white" , anchor = "w")
status.place(rely = 1 , anchor = "sw" , relwidth = 1)


root.mainloop()
