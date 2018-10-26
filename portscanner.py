import socket
from tkinter import *

def scanPorts():
    ip = ipEntry.get()
    _from = int(fromEntry.get())
    to = int(toEntry.get())
    
    statusLabel["text"]= ""

    for port in range(_from, to):
        if isPortOpen(ip, port) == True:
            portStatus = 'Port {} is open'.format(port)
        else:
            portStatus = 'Port {} is closed'.format(port)
        
        statusLabel["text"]+= portStatus + "\n"

def isPortOpen(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((ip, port))
        
        print('{} is open'.format(port))
        sock.close()
        return True
    except:
        return False

root = Tk()

ipLabel = Label(root, text= "IP Address")
ipEntry = Entry(root)

portLabel = Label(root, text= "Ports")
fromLabel = Label(root, text= "From:")
fromEntry = Entry(root)

toLabel = Label(root, text= "To:")
toEntry = Entry(root)

checkButton = Button(root, text= "Check", command= scanPorts)
statusLabel = Label(root)
statusLabel.grid(row= 4, column= 0)

ipLabel.grid(row= 0, column= 0)
ipEntry.grid(row= 0, column= 1)

portLabel.grid(row= 1, column= 0)

fromLabel.grid(row= 1, column= 1)
fromEntry.grid(row= 1, column= 2)

toLabel.grid(row= 2, column= 1)
toEntry.grid(row= 2, column= 2)

checkButton.grid(row= 3, column= 1)
    
root.mainloop()
