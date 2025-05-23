import tkinter
# import the window for window to work
window = tkinter.Tk()
window.title("My GUI")

# for the label, first parameter is the window, second is the text
label = tkinter.Label(window, text="Hello World").pack() #without the pack you cant see the label

# Once the window is added to the label, no need to keep adding it as a parameter
# to make a text box
lab = tkinter.Label(text = "Welcome", background = "pink").pack() #without the pack this won't work


# clickable button, doesn't do anything yet
bt = tkinter.Button(text = "Click Me", background = "Red").pack()

# entry input for a single line of text from user .Entry()
# text input is for multiline texts from user .Text()

# only input necessary is the width, but you can add more parameters like background, font, etc
txt = tkinter.Entry(width = 20).pack()

# text input for multiline texts from user
# The whole input acts as the entry box
another_txt = tkinter.Text().pack() 

# mainloop to keep the window open, without this the window will close immediately
window.mainloop()