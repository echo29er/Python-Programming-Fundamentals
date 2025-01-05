import tkinter

def main():
    # Create the root window
    root = tkinter.Tk()

    # Set the title and make the window non-resizable
    root.title("Reminder!")
    root.resizable(width=False, height=False)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
