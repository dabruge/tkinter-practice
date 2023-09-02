import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        self.label_text = tk.StringVar()
        self.label_text.set("Choose one:")
        self.label = tk.Label(self, textvar=self.label_text) # Must use textvar here instead of just text
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        hello_button = tk.Button(self, text="Say hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self, text="Say goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
    
    def say_hello(self):
        self.label_text.set("Hello World!")
    
    def say_goodbye(self):
        self.label_text.set("Goodbye! \n (Closing in 2 seconds)")
        self.after(2000, self.destroy)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
