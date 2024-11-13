import tkinter as tk
from tkinter import ttk
import platform

class KeyCodeDetector:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Key Code Detector")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')  # Light gray background
        
        # Set modern style
        self.style = ttk.Style()
        self.style.theme_use('clam' if platform.system() == 'Linux' else 'vista')
        
        # Configure styles
        self.style.configure('Modern.TFrame', background='#f0f0f0')
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 24, 'bold'), 
                           background='#f0f0f0',
                           foreground='#2c3e50')
        self.style.configure('Subtitle.TLabel', 
                           font=('Segoe UI', 12),
                           background='#f0f0f0',
                           foreground='#7f8c8d')
        self.style.configure('Value.TLabel',
                           font=('Segoe UI', 36, 'bold'),
                           background='#ffffff',
                           foreground='#2980b9',
                           padding=20)
        self.style.configure('Name.TLabel',
                           font=('Segoe UI', 14),
                           background='#f0f0f0',
                           foreground='#2c3e50')
        self.style.configure('Modern.TButton',
                           font=('Segoe UI', 11),
                           padding=10)
        
        # Create main container
        self.main_frame = ttk.Frame(self.root, style='Modern.TFrame', padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title and instructions
        self.title_label = ttk.Label(
            self.main_frame,
            text="Key Code Detector",
            style='Title.TLabel'
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        self.instruction_label = ttk.Label(
            self.main_frame,
            text="Press any key to see its details",
            style='Subtitle.TLabel'
        )
        self.instruction_label.grid(row=1, column=0, columnspan=2, pady=(0, 30))
        
        # Create value displays with white background and border
        # Key Code Display
        self.code_container = tk.Frame(
            self.main_frame,
            background='#ffffff',
            borderwidth=1,
            relief='solid'
        )
        self.code_container.grid(row=2, column=0, padx=10, sticky='nsew')
        
        self.keycode_value = ttk.Label(
            self.code_container,
            text="0",
            style='Value.TLabel'
        )
        self.keycode_value.pack(pady=20, padx=20)
        
        self.keycode_label = ttk.Label(
            self.code_container,
            text="KEY CODE",
            style='Name.TLabel'
        )
        self.keycode_label.pack(pady=(0, 20))
        
        # Key Name Display
        self.name_container = tk.Frame(
            self.main_frame,
            background='#ffffff',
            borderwidth=1,
            relief='solid'
        )
        self.name_container.grid(row=2, column=1, padx=10, sticky='nsew')
        
        self.keyname_value = ttk.Label(
            self.name_container,
            text="-",
            style='Value.TLabel'
        )
        self.keyname_value.pack(pady=20, padx=20)
        
        self.keyname_label = ttk.Label(
            self.name_container,
            text="KEY NAME",
            style='Name.TLabel'
        )
        self.keyname_label.pack(pady=(0, 20))
        
        # Last pressed key info
        self.last_key_frame = ttk.Frame(self.main_frame, style='Modern.TFrame')
        self.last_key_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.last_key_label = ttk.Label(
            self.last_key_frame,
            text="Last Pressed: None",
            style='Subtitle.TLabel'
        )
        self.last_key_label.pack()
        
        # Create quit button with hover effect
        self.style.configure('Quit.TButton',
                           font=('Segoe UI', 11),
                           padding=10,
                           background='#e74c3c')
        
        self.quit_button = ttk.Button(
            self.main_frame,
            text="Exit",
            style='Modern.TButton',
            command=self.root.quit
        )
        self.quit_button.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        
        # Set focus to the main window
        self.root.focus_force()
        
        # Store the last pressed key info
        self.last_pressed = None
        
        # Add visual feedback for key press
        self.original_bg = self.code_container['background']
    
    def flash_background(self):
        """Create a visual feedback flash effect"""
        # Flash both containers
        self.code_container['background'] = '#e8f0fe'
        self.name_container['background'] = '#e8f0fe'
        
        # Schedule return to original color
        self.root.after(100, self.reset_background)
    
    def reset_background(self):
        """Reset the background color after flash"""
        self.code_container['background'] = self.original_bg
        self.name_container['background'] = self.original_bg
    
    def on_key_press(self, event):
        """Handle key press events and update the display"""
        # Update key code
        self.keycode_value.config(text=str(event.keycode))
        
        # Update key name
        key_name = event.keysym
        if key_name == 'space':
            key_name = 'SPACE'
        elif len(key_name) == 1:
            key_name = key_name.upper()
        self.keyname_value.config(text=key_name)
        
        # Update last pressed key
        self.last_key_label.config(
            text=f"Last Pressed: {key_name} (code: {event.keycode})"
        )
        
        # Show visual feedback
        self.flash_background()
    
    def run(self):
        """Start the application"""
        # Center the window on the screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.root.mainloop()

if __name__ == "__main__":
    app = KeyCodeDetector()
    app.run()