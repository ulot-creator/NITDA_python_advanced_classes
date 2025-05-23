import tkinter

screen = tkinter.Tk()
screen.title("Better placement")

# takes the size of the window
screen.geometry("300x300")

name = tkinter.Label(screen, text = "Name").place(x = 30, y = 50) # x and y are the coordinates of the label, basically freedom to place it anywhere
email = tkinter.Label(screen, text = "Email").place(x = 30, y = 90)

n1 = tkinter.Entry(screen).place(x = 80, y = 50) # x and y are the coordinates of the entry box
e1 = tkinter.Entry(screen).place(x = 80, y = 90)

screen.mainloop()