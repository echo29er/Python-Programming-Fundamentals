import tkinter

def main():
    def about():
        print("About was selected")

    def quit():
        root.destroy()

    root = tkinter.Tk()
    root.title("Silly Program")

    # Create the menu bar
    bar = tkinter.Menu(root)

    # File menu
    fileMenu = tkinter.Menu(bar, tearoff=0)
    fileMenu.add_command(label="Exit", command=quit)
    bar.add_cascade(label="File", menu=fileMenu)

    # Help menu
    helpMenu = tkinter.Menu(bar, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    bar.add_cascade(label="Help", menu=helpMenu)

    #Assign the menu to the root window 
    root.config(menu=bar)

    root.geometry("300x100")
    label = tkinter.Label(root, text="This is a Tkinter test.")
    label.pack()


    root.mainloop()

if __name__ == "__main__":
    main()

