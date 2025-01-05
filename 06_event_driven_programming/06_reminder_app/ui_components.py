from tkinter import Button, Label, Text, Toplevel

'''
This is the Model in the MVC model, responsible for managing the data model.
Interacts with the Controller (ReminderApp) to update and retrieve data as needed.
'''  

def create_window(title: str, text: str, x: int, y: int, bg_color: str=None) -> Toplevel :
    """
    Function Purpose: Create Toplevel window objects that are configurable to the use case.

    Args:
        title (str): The text to be used as the window title.
        text (str): The text to be used in the window.
        x (int): X-coordinate for the window.
        y (int): Y-coordinate for the window.
        bg_color (str): Background colour of the window's text field. 

    Returns:
        A Toplevel object
    """

    # Create a top-level window object for the reminder
    window = Toplevel() 
    window.geometry(f"200x100+{x}+{y}")
    window.title(title)

    # When there is text create a label object, add it to the window
    label = Label(window, text=text.strip(), wraplength=180, bg=bg_color)
    label.pack(pady=10)

    # Add a close button object 
    close_button = Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=5)

    return window # Return a window object

def create_button(parent: str, text: str, command: str, row: int, column: int, columnspan: int=1, pady: int=5) -> Button:
    """
    Function Purpose: Create a generic button object for commands on a window object.

    Args:
        parent (str): The window object in which the button will be housed.
        text (str): The text presented on the button.
        command (str): The function to be called on the window object from this button.
        row (int): Using a grid starting from 0, place the button on this row. 
        column (int): Using a grid starting from 0, place the button on this column. 
        columnspan (int): Using a grid starting from 0, this value signifies the number of columns to span. 
        pady (int): This provides padding on the y-axis i.e. above and below the button.

    Returns:
        Button object
    """
    button = Button(parent, text=text, command=command)
    button.grid(row=row, column=column, columnspan=columnspan, pady=pady)
    return button

def create_label_and_input(parent: str, label_text: str, input_bg: str="white", label_row: int=0, label_column: int=0, input_row: int=0, input_column: int=1, padx: int=5, pady: int=5) -> tuple[Label, Text]:
    """
    Function Purpose: Create a label to describe to the user what to do, and a text input box to the right of the label.

    Args:
        parent (str): The window object in which the button will be housed.
        label_text (str): The text instructions presented to the user.
        input_bg (str): The background colour of the text input box. 
        label_row (int): In the grid, the row on which the label will be placed.  
        label_column (int): In the grid, the column on which the label will be placed.
        input_row (int): In the grid, the row on which the label will be placed.  
        input_column (int): In the grid, the column on which the label will be placed.
        padx (int): Horizontal axis padding for the label and widget 
        pady (int): Vertical axis padding for the label and widget 
    
    Returns:
        A tuple of Label and Text objects
    """
    label = Label(parent, text=label_text)
    label.grid(row=label_row, column=label_column, padx=padx, pady=pady, sticky="w")
    
    input_widget = Text(parent, bg=input_bg, width=20, height=3)
    input_widget.grid(row=input_row, column=input_column, padx=padx, pady=pady, sticky="ew")
    return label, input_widget # This is a tuple