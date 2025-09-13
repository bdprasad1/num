import tkinter as tk
from tkinter import messagebox
import random
import string

class AlphabetRecognitionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Alphabet Recognition A to Z")
        self.root.config(bg="#FFFDE7")

        # Use all uppercase alphabets A-Z
        self.alphabets = list(string.ascii_uppercase)
        self.current_letter = random.choice(self.alphabets)

        self.prompt_label = tk.Label(root, text="Guess the letter shown below:", font=("Comic Sans MS", 24, "bold"), bg="#FFFDE7")
        self.prompt_label.pack(pady=20)

        # Letter display label (big font)
        self.letter_label = tk.Label(root, text=self.current_letter, font=("Comic Sans MS", 150, "bold"), fg="#1E88E5", bg="#FFFDE7")
        self.letter_label.pack(pady=40)

        # Entry for kid to enter the displayed letter
        self.answer_entry = tk.Entry(root, font=("Comic Sans MS", 36), justify="center", bd=5, relief=tk.RIDGE)
        self.answer_entry.pack(ipadx=60, ipady=10)
        self.answer_entry.focus()
        self.answer_entry.bind("<Return>", lambda event: self.check_and_next())

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Comic Sans MS", 24, "bold"), bg="#FFFDE7")
        self.feedback_label.pack(pady=20)

        # Buttons to check and go next
        self.check_button = tk.Button(root, text="Check", font=("Comic Sans MS", 24, "bold"), bg="#43A047", fg="white", command=self.check_answer)
        self.check_button.pack(side="left", padx=50, pady=10)

        self.next_button = tk.Button(root, text="Next Letter", font=("Comic Sans MS", 24, "bold"), bg="#1976D2", fg="white", command=self.next_letter, state=tk.DISABLED)
        self.next_button.pack(side="right", padx=50, pady=10)

    def check_answer(self):
        guess = self.answer_entry.get().strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            self.feedback_label.config(text="Please enter a single letter!", fg="red")
            self.answer_entry.delete(0, tk.END)
            return False
        if guess == self.current_letter:
            self.feedback_label.config(text="🎉 Correct! Well done! 🎉", fg="green")
            self.check_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
            return True
        else:
            self.feedback_label.config(text="Try again!", fg="red")
            self.answer_entry.delete(0, tk.END)
            return False

    def check_and_next(self):
        if self.check_answer():
            self.next_letter()

    def next_letter(self):
        self.current_letter = random.choice(self.alphabets)
        self.letter_label.config(text=self.current_letter)
        self.feedback_label.config(text="")
        self.answer_entry.config(state=tk.NORMAL)
        self.answer_entry.delete(0, tk.END)
        self.check_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.answer_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlphabetRecognitionGame(root)
    root.mainloop()
