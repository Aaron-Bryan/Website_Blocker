#tkinter handles all the GUI stuff
from tkinter import *

#The host file is needed, because we want to block the sites to be
#blocked in our respective systems.
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

#Block Function
def Block():
    target_site = enter_Website.get(1.0, END)
    Website = list(target_site.split(","))
    with open(host_path, "r+") as host_file:
        content = host_file.read()

        for site in Website:
            if site in content:
                block_label_1 = Label(window, text = "Site is already Blocked", font = "arial")
                block_label_1.place(x = 200, y = 200)
                pass
            else:
                host_file.write(ip_address + " " + site + "\n")
                block_label_2 = Label(window, text = "Site is now Blocked")
                block_label_2.place(x = 230, y = 200)

#Unblock Function
def Unblock():
    target_site = enter_Website.get(1.0, END)
    Website = list(target_site.split(","))
    with open (host_path, "r+") as host_file:
        content = host_file.readline()

        for site in Website:
            if site in target_site:
                with open (host_path, "r+") as edit:
                    for line in content:
                        if line.strip(",") != target_site:
                            edit.write(line)
                            unblock_label_1 = Label(window, text = "UnBlocked", font = 'arial')
                            unblock_label_1.place(x = 350, y = 200)
            else:
                unblock_label_2 = Label(window, text = "Site is not in the List", font = "arial")
                unblock_label_2.place(x = 350,y = 200)


#Initializing the window
window = Tk()
window.geometry("650x400")
window.minsize(650,400)
window.maxsize(650,400)
window.title("Website Blocker")

heading = Label(window, text = "Website Blocker", font = "arial")
heading.pack

#Labels
website_label=Label(window, text ='Enter Website :' , font ='arial 13 bold')
website_label.place(x=5 ,y=60)
enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)

#Buttons for the functions
block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Block ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 150)
unblock_button = Button(window, text = 'Unblock',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)

window.mainloop()
