import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        self.name_text = tk.StringVar()
        self.label_text = tk.StringVar()
        self.label_text.set("My name is:")

        self.label = tk.Label(self, textvar=self.label_text) # Must use textvar here instead of just text
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self, text="Say hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self, text="Say goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
    
    def say_hello(self):
        message = f"Hello, {self.name_entry.get()}"
        msgbox.showinfo("Hello", message)
    
    def say_goodbye(self):
        if msgbox.askyesno("Close window?", "Would you like to close this window?"):
            self.label_text.set(f"Window will close in 2 seconds. Goodbye, {self.name_text.get()}!")
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open.")

if __name__ == "__main__":
    window = Window()
    window.mainloop()
