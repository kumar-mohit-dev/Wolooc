import tkinter as tk
from tkinter import ttk

class RoundedButton(tk.Canvas):
    def __init__(self, master, text, command, radius=50, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.radius = radius
        
        # Create rounded rectangle
        self.create_rounded_rectangle(0, 0, 200, 50, self.radius, fill="#4CAF50", outline="")
        
        # Create text
        self.text_id = self.create_text(100, 25, text=text, fill="white", font=("Arial", 14))
        
        # Bind click event
        self.bind("<Button-1>", self.on_click)
        
        # Configure canvas size
        self.config(width=200, height=50)

    def create_rounded_rectangle(self, x1, y1, x2, y2, r, **kwargs):
        """Draw a rectangle with rounded corners."""
        self.create_arc(x1, y1, x1 + r*2, y1 + r*2, start=90, extent=90, **kwargs)  # Top left
        self.create_arc(x2 - r*2, y1, x2, y1 + r*2, start=0, extent=90, **kwargs)  # Top right
        self.create_arc(x1, y2 - r*2, x1 + r*2, y2, start=180, extent=90, **kwargs)  # Bottom left
        self.create_arc(x2 - r*2, y2 - r*2, x2, y2, start=270, extent=90, **kwargs)  # Bottom right
        self.create_rectangle(x1 + r, y1, x2 - r, y2, **kwargs)  # Middle rectangle
        self.create_rectangle(x1, y1 + r, x1 + r, y2 - r, **kwargs)  # Left rectangle
        self.create_rectangle(x2 - r, y1 + r, x2, y2 - r, **kwargs)  # Right rectangle

    def on_click(self, event):
        """Trigger the command when the button is clicked."""
        self.command()

# Example usage
def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Rounded Button Example")

rounded_button = RoundedButton(root, text="Click Me", command=on_button_click, bg="#4CAF50")
rounded_button.pack(pady=20)

root.mainloop()
