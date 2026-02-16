"""Sample ad.py file to demonstrate URL linking."""

def main():
    print("Hello from ad.py")

if __name__ == "__main__":
    main()
import tkinter as tk
import random

class KirthikaLoveApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Oii devi 💕")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFB6C1")
        self.root.resizable(False, False)
        self.page_num = 1
        self.show_page()
    
    def show_page(self):
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        if self.page_num == 1:
            self.page1()
        elif self.page_num == 2:
            self.page2_kfc()
    
    def page1(self):
        title = tk.Label(self.root, text="Oii devi\n can ubuy shwarma for me? 💖", 
                        font=("Lucida Handwriting", 24, "bold"), 
                        bg="#FFB6C1", fg="#FF1493")
        title.pack(pady=50)
        
        yes_btn = tk.Button(self.root, text="Yes 😍", font=("Arial", 16, "bold"),
                           bg="#90EE90", fg="white", width=12, height=2,
                           command=lambda: self.set_page(2))
        yes_btn.pack(pady=20)
        
        self.no_btn = tk.Button(self.root, text="No 😢", font=("Arial", 16, "bold"),
                               bg="#FF69B4", fg="white", width=12, height=2,
                               command=self.move_no)
        self.no_btn.pack(pady=10)
        
        self.no_x, self.no_y = 200, 250
        self.move_no()
    
    def move_no(self):
        new_x = random.randint(50, 350)
        new_y = random.randint(200, 350)
        self.no_x, self.no_y = new_x, new_y
        self.no_btn.place(x=self.no_x, y=self.no_y)
    
    def set_page(self, page):
        self.page_num = page
        self.show_page()
    
    def page2_kfc(self):
        # Fixed KFC page - no blocking canvas
        title = tk.Label(self.root, text="iknow ne yes solluvanu enaku therium❤️", 
                        font=("Comic Sans MS", 28, "bold"), 
                        bg="#FFB6C1", fg="#FF4500")
        title.pack(pady=50)
        
        love_msg = tk.Label(self.root, text="hahahaha 😍\nForever together 💕", 
                           font=("Lucida Handwriting", 20), 
                           bg="#FFB6C1", fg="#DC143C")
        love_msg.pack(pady=30)
        
        back_btn = tk.Button(self.root, text="Play Again 💕", font=("Arial", 14),
                            bg="#FFD700", fg="black", width=15,
                            command=lambda: self.set_page(1))
        back_btn.pack(pady=20)
        
        # Simple hearts without canvas blocking
        heart1 = tk.Label(self.root, text="💖", font=("Arial", 30), bg="#FFB6C1")
        heart1.place(x=100, y=100)
        heart2 = tk.Label(self.root, text="💖", font=("Arial", 30), bg="#FFB6C1")
        heart2.place(x=350, y=150)
    
    def run(self):
        self.root.mainloop()

app = KirthikaLoveApp()
app.run()