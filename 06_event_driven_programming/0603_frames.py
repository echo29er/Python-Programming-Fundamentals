import tkinter

def create_reminder(note_text, x, y):
    # Create a top-level window for the reminder
    reminder_window = tkinter.Toplevel() 
    reminder_window.geometry(f"200x100+{x}+{y}")
    reminder_window.title("Reminder")

    # Add the note text to the window
    reminder = tkinter.Label(reminder_window, text=note_text.strip(), wraplength=180)
    reminder.pack(pady=10)

    # Add a close button 
    close_button = tkinter.Button(reminder_window, text="Close", command=reminder_window.destroy)
    close_button.pack(pady=5)

def create_generic_window(text_in, x, y):
    # Create a generic top-level window information
    generic_window = tkinter.Toplevel()
    generic_window.geometry(f"200x200+{x}+{y}")
    generic_window.title("Contact")

    # Add the note text to the window
    note_label = tkinter.Label(generic_window, bg="yellow", text=text_in.strip(), wraplength=180)
    note_label.pack(pady=10)

    # Add a close button 
    close_button = tkinter.Button(generic_window, text="Close", command=generic_window.destroy)
    close_button.pack(pady=5)


def main():
    def about():
        about_text = "This app can hold a reminder"
        create_generic_window(about_text, root.winfo_rootx()+5, root.winfo_rooty()+5)
    
    def quit():
        root.destroy()

    def post():
        print("Post")
        # Get the text from the reminder text widget and remove trailing space
        new_reminder_text = reminder_text.get("1.0", tkinter.END).strip()

        if new_reminder_text: # Only execute when there is text
            # Call create_reminder to display the reminder
            reminder_window = create_reminder(new_reminder_text, root.winfo_rootx()+50, root.winfo_rooty()+50)
            
            # Add the note and ites window reference to the lists
            notes.append(new_reminder_text)
            reminders.append(reminder_window)

            # Clear the text widget after posting
            reminder_text.delete("1.0", tkinter.END)
    
    def show_all_notes():
        print("Displaying all notes")
        all_notes = "\n".join(notes)
        create_generic_window(all_notes or "No reminders yet.", root.winfo_rootx()+50, root.winfo_rooty()+50)

    def contact():
        contact_text = "This was made by Stephen Bassett\n Reach him at sbassettuk@gmail.com"
        create_generic_window(contact_text, root.winfo_rootx()+5, root.winfo_rooty()+5)

    # Create the root window
    root = tkinter.Tk()

    # Create the title
    root.title("Reminder!")

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

    # Assign the menu to the root window 
    root.config(menu=bar)

    # Set the size of the main window
    root.geometry("400x300")

    # Create a main frame
    mainFrame = tkinter.Frame(root, padx=10, pady=10)
    mainFrame.grid(row=0, column=0, sticky="nsew")

    # Configure the grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Add widgets inside the main frame
    reminder_label = tkinter.Label(mainFrame, text="Enter your reminder:")
    reminder_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    # reminder_entry = tkinter.Entry(mainFrame, width=20)
    # reminder_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Text widget for entering reminders
    reminder_text = tkinter.Text(mainFrame, bg="yellow", width = 20, height = 3)
    reminder_text.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Add Reminder button
    add_button = tkinter.Button(mainFrame, text="Add Reminder", command=post)
    add_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Show All Notes button
    show_button = tkinter.Button(mainFrame, text="Show All Notes", command=show_all_notes)
    show_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Contact button 
    contact_button = tkinter.Button(mainFrame, text="Contact us", command=contact)
    contact_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Adjust grid weights inside the frame for better responsiveness
    mainFrame.grid_columnconfigure(1, weight=1)

    # Initialise dummy variables for notes and reminders
    notes = []
    reminders = []

    root.mainloop()

if __name__ == "__main__":
    main()

