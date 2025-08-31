import tkinter as tk
import random

# Level easy/medium
# Can make it harder by adding more colours etc 
# Adding more features - theme feature, updating the UI 

class CaptionGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Caption Generator 📸")

        # Entry for user to type their own caption
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Type your own caption...")

        # Button to display custom caption
        self.custom_btn = tk.Button(root, text="Show My Caption", command=self.show_caption)
        self.custom_btn.pack(pady=5)

        # Button to get a random caption
        self.random_btn = tk.Button(root, text="Random Caption 🎲", command=self.random_caption)
        self.random_btn.pack(pady=5)

        # Label to display the caption
        self.caption_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="center")
        self.caption_label.pack(pady=20)

        # My captions
        self.captions = [
            "Just vibes ✨",
            "Coffee first ☕",
            "Lost in Tokyo 🏮",
            "Weekend mood 🌸",
            "Do it for the plot 🎬",
            "Sunshine mixed with a little bit of sass ☀️",
            "Living my best life 💕",
            "Good vibes only 🌈",
            "Smiles are contagious 😄",
            "Adventure begins here 🌍"
        ]

    def show_caption(self):
        text = self.entry.get()
        self.caption_label.config(text=text)

    def random_caption(self):
        caption = random.choice(self.captions)
        self.caption_label.config(text=caption)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionGenerator(root)
    root.mainloop()
