from Tkinter import Tk, Label, Button, StringVar, Text, END, DISABLED
from threading import Thread
import time

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set("TITULO")
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()
	
	# Chat container
	self.chatContainer = Text(master, height=10, width=30)
	self.chatContainer.config(state=DISABLED)
	self.chatContainer.pack()

	# Message container
	self.messageContainer = Text(master, height=2, width=30)
	self.messageContainer.pack()
        self.greet_button = Button(master, text="Send", command=self.sendMsg)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.closeConnection)
        self.close_button.pack()

	thread = Thread(target = self.recieveMsg)
	thread.start()

    def recieveMsg(self):
	for i in range(1,5):
	  texto = "HOLA N "+str(i)+"\n"
	  self.chatContainer.configure(state='normal')
	  self.chatContainer.insert(END, texto)
	  self.chatContainer.configure(state=DISABLED)
	  time.sleep(5)

    def sendMsg(self):
	texto = self.messageContainer.get("1.0",END)
	if texto and texto.strip():
	  print("Mensaje a enviar:")
	  self.messageContainer.delete('1.0', END)
	  self.chatContainer.configure(state='normal')
	  self.chatContainer.insert(END, texto)
	  self.chatContainer.configure(state=DISABLED)
	  print(texto)

    def closeConnection(self):
	print("Cerrando chat.")
	self.master.quit()

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
