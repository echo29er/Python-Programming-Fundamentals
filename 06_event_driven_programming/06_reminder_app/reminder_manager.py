import json
import os

from datetime import datetime

import ui_components as uic

class ReminderManager:
    """
    Class Purpose: Handles reminder management: limited to adding reminders for now.
    Features coming soon: 
    * Storing and retrieving reminders.

    This is the Model in the MVC model, responsible for managing the data model.
    Interacts with the Controller (ReminderApp) to update and retrieve data as needed.  

    Attributes:
        notes (list): Stores reminder texts for persistence.
        reminders (list): Tracks active Toplevel windows for reminders.

    Methods:
        add_reminder: Creates a reminder window object and stores the window object and text data in the reminders and notes lists respectively.
    """

    # Constructor
    def __init__(self, notes: list, reminders: list) -> None:
        """
        Constructor Purpose: Constructor for the ReminderManager class.

        Args:
            notes (list): A list to store reminder texts.
            reminders (list): A list to track tkinter Toplevel window objects.

        Returns:
            None
        """
        self.notes = notes
        self.reminders = reminders

    def add_reminder(self, text: str, x: int, y: int) -> None:
        """
        Function Purpose: Create a new reminder window object populated with the text input from the user. Add these to the list objects to manage the data.

        Args:
            text (str): The reminder text.
            x (int): X-coordinate for the window.
            y (int): Y-coordinate for the window.

        Returns:
            None
        """

        # Create the reminder window
        window = uic.create_window("Reminder", text, x, y)
        
        # Append to notes and reminders
        self.notes.append(text) # Accumulator pattern
        self.reminders.append(window)

    def delete_all_reminders(self): 
        """
        Function Purpose: Deletes all reminders from the session. 

        Args:

        Returns:
            None
        """
        self.notes.clear()
        self.reminders.clear()

    def save_to_file(self, filename: str = "reminders.json") -> bool: 
        """
        Function Purpose: Save the reminders to a JSON file

        Args:
            filename(str): Name of file to save to. Defaults to "reminders.json"

        Returns:
            bool: True if save successful, False otherwise
        """
        try: 
            reminder_data = []
            for note in self.notes:
                reminder = {
                    'text': note, 
                    'created_at': datetime.now().isoformat()
                }
                reminder_data.append(reminder)

            with open(filename, 'w') as f:
                json.dump(reminder_data, f, indent=4)
            return True
        
        except Exception as e: 
            print(f"Error saving reminders: {e}")
            return False
        
    
    def load_from_file(self, filename: str = "reminders.json") -> bool:
        """
        Function Purpose: Loads reminders from a JSON file

        Args:
            filename(str): Name of file to load from. Defaults to "reminders.json"

        Returns:
            bool: True if load successful, False otherwise
        """
        if not os.path.exists(filename):
            print(f'File {filename} does not exist')
            return False
        
        try: 
            with open(filename, 'r') as f: 
                reminder_data = json.load(f)

            # Clear current reminders
            self.delete_all_reminders()

            # Calculate position for new windows 
            base_x = base_y = 100
            spacing = 30 

            # Recreate reminders from saved data
            for index, reminder in enumerate(reminder_data):
                x = base_x + (index * spacing)
                y = base_y + (index * spacing)
                self.add_reminder(reminder['text'], x, y)

            return True
        
        except Exception as e:
            print(f'Error loading reminder: {e}')
            return False
        
    def get_reminder_count(self) -> int: 
        """
        Function Purpose: Get the number of active reminders

        Returns:
            int: Number of active reminders
        """
        return len(self.notes)
