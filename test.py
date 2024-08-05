from tkinter import *
from custom_hovertip import CustomTooltipLabel


# Create the main application window
root = Tk()
root.geometry("300x200")
root.title("Tooltip Example with Tix")

# Create a label widget
label1 = Label(root, text="Welcome to GeeksforGeeks")
label1.pack(pady=20)

CustomTooltipLabel(anchor_widget=label1, text="This is tooltip text.",
                   )


# Create a button widget
button1 = Button(root, text="Click Me", bg="green", fg="white")
button1.pack(pady=10)

# Assign tooltips to the widgets


# Run the main application loop
root.mainloop()