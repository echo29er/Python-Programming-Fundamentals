import tkinter 

import ui_components as uic

class ReminderView: 
    """
    Class Purpose: The View component in MVC. Responsible for all UI elements and their layout. 
    Delegates all business logic to the controller through callbacks. 

    Attributes:

    Methods:
        
    """
    def __init__(self, root):
        self.root = root 

        # Set up the main window
        self.root.title("Reminder!")
        self.root.geometry("340x300")

        # Create the main frame container
        self.main_frame = tkinter.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the grid layout for responsiveness
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Will be set by controller
        self.callbacks = {
            'on_add_reminder': None,
            'on_show_all_notes': None,
            'on_save_to_file': None, 
            'on_load_from_file': None, 
            'on_delete_all': None,
            'on_about': None,
            'on_contact': None
        }

    # Define a function to create widget objects
    def create_widgets(self):

        """
        Create and arrange all widgets for the main application window.
        """

        # Create label and input field
        self.reminder_label, self.reminder_input = uic.create_label_and_input(
        parent=self.main_frame,
        label_text="Enter your reminder:",
        input_bg="yellow",
        label_row=0,
        label_column=0,
        input_row=0,
        input_column=1
        )

        # Create buttons
        self.add_reminder_button = uic.create_button(
        parent=self.main_frame,
        text="Add Note",
        command=self._handle_add_reminder,
        row=1,
        column=0,
        columnspan=2
        )

        self.show_all_notes_button = uic.create_button(
        parent=self.main_frame,
        text="Show Notes",
        command=self._handle_show_all_notes,
        row=2,
        column=0,
        columnspan=1
        )

        self.contact_button = uic.create_button(
        parent=self.main_frame,
        text="Delete Notes",
        command=self._handle_delete_all,
        row=2,
        column=1,
        columnspan=1
        )

        self.contact_button = uic.create_button(
        parent=self.main_frame,
        text="Save Notes",
        command=self._handle_save_to_file,
        row=3,
        column=0,
        columnspan=1
        )

        self.contact_button = uic.create_button(
        parent=self.main_frame,
        text="Load Notes",
        command=self._handle_load_from_file,
        row=3,
        column=1,
        columnspan=1
        )
        
        self.contact_button = uic.create_button(
        parent=self.main_frame,
        text="Contact",
        command=self._handle_contact,
        row=4,
        column=0,
        columnspan=1
        )

    # Define a function to create the setup menu objects for the ReminderApp constructor
    def setup_menu(self):
        bar = tkinter.Menu(self.root)

        # File menu
        file_menu = tkinter.Menu(bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tkinter.Menu(bar, tearoff=0)
        help_menu.add_command(label="About", command=self._handle_about)
        bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=bar)

    def set_callbacks(self, callbacks):
        """Set the callback functions that will be called when UI events occur"""
        self.callbacks = callbacks

    def get_reminder_text(self):
        """Get the current text from the reminder input"""
        return self.reminder_input.get("1.0", tkinter.END).strip()
    
    def clear_reminder_input(self):
        """Clear the reminder input field"""
        self.reminder_input.delete("1.0", tkinter.END)

    # Private handler methods that delegate to controller callbacks
    def _handle_add_reminder(self):
        if self.callbacks['on_add_reminder']:
            self.callbacks['on_add_reminder']()
            
    def _handle_show_all_notes(self):
        if self.callbacks['on_show_all_notes']:
            self.callbacks['on_show_all_notes']()
            
    def _handle_delete_all(self):
        if self.callbacks['on_delete_all']:
            self.callbacks['on_delete_all']()

    def _handle_save_to_file(self):
        if self.callbacks['on_save_to_file']:
            self.callbacks['on_save_to_file']()

    def _handle_load_from_file(self):
        if self.callbacks['on_load_from_file']:
            self.callbacks['on_load_from_file']()
            
    def _handle_about(self):
        if self.callbacks['on_about']:
            self.callbacks['on_about']()
            
    def _handle_contact(self):
        if self.callbacks['on_contact']:
            self.callbacks['on_contact']()