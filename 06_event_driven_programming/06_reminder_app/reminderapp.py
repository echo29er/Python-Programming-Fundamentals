import ui_components as uic
import reminder_manager as rm
import view

class ReminderApp:

    """
    Class Purpose: Creates the Reminder app: the main application class to manage the reminders. 
    This is the Control in the MVC model: it brings together the View and Model, and manages/controls them to create a user experience. 

    Attributes:
        root (tkinter object): The tkinter object on which all other objects are built.
    """

    # Define the class constructor 
    def __init__(self, root):
        
        # Initialise the model
        self.notes = [] # initialise list to store notes
        self.reminders = [] # initalise list to store window objects
        self.reminder_manager = rm.ReminderManager(self.notes, self.reminders) 

        # Initialise the view
        self.view = view.ReminderView(root)

        # Set up callbacks for the View
        self.view.set_callbacks({
            'on_add_reminder': self.new_reminder,
            'on_show_all_notes': self.show_all_notes,
            'on_save_to_file': self.save_notes_to_file, 
            'on_load_from_file': self.load_notes_from_file, 
            'on_delete_all': self.delete_all_notes,
            'on_about': self.about,
            'on_contact': self.contact
        })

        # Create UI elements 
        self.view.create_widgets() 
        self.view.setup_menu() 

    # Create a new remidner
    def new_reminder(self):
        reminder_text = self.view.get_reminder_text()

        if reminder_text: # Only execute when there is text. This is an example of the predicate function
            self.reminder_manager.add_reminder(
                reminder_text, 
                self.view.root.winfo_rootx()+50, 
                self.view.root.winfo_rooty()+50
            )
            # Clear the text widget after posting
            self.view.clear_reminder_input()

    # Show all notes
    def show_all_notes(self):
        all_notes = "\n".join(self.notes) or "No reminders yet."
        uic.create_window(
            "All Notes", 
            all_notes, 
            self.view.root.winfo_rootx()+50, 
            self.view.root.winfo_rooty()+50
        )

    # Deleting all notes
    def delete_all_notes(self):
        deletion_text = "All notes have been deleted"
        self.reminder_manager.delete_all_reminders()
        uic.create_window(
            "Deleted", 
            deletion_text, 
            self.view.root.winfo_rootx()+5, 
            self.view.root.winfo_rooty()+5
        )

    # Save reminders to JSON
    def save_notes_to_file(self):
        saved_text = "All notes have saved"
        self.reminder_manager.save_to_file()
        uic.create_window(
            "Saved", 
            saved_text, 
            self.view.root.winfo_rootx()+5, 
            self.view.root.winfo_rooty()+5
        )

    # Load reminders from JSON
    def load_notes_from_file(self):
        load_text = "All notes have been loaded"
        self.reminder_manager.load_from_file()
        uic.create_window(
            "Loaded", 
            load_text, 
            self.view.root.winfo_rootx()+5, 
            self.view.root.winfo_rooty()+5
        )

    # Show the about window
    def about(self):
        uic.create_window(
            "About", 
            "This app can hold a reminder.", 
            self.view.root.winfo_rootx() + 5, 
            self.view.root.winfo_rooty() + 5
        )

    # Show the contact us window
    def contact(self):
        contact_text = "This was made by me"
        uic.create_window(
            "Contact", 
            contact_text, 
            self.view.root.winfo_rootx()+5, 
            self.view.root.winfo_rooty()+5
        )