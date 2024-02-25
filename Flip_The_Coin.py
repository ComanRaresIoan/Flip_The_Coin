import tkinter as tk
import random

class CoinFlipApp:
    def __init__(self, master):
        self.master = master
        master.title("Coin Flip")

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.result_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.result_label.pack()

        self.flip_button = tk.Button(master, text="Flip Coin", command=self.flip)
        self.flip_button.pack()

        # Coordinates for the center of the coin
        self.coin_center = (100, 100)

    def draw_coin(self, result):
        self.canvas.delete("all")
        if result == "Heads":
            self.canvas.create_oval(50, 50, 150, 150, fill="gold", outline="black", width=2)
            self.canvas.create_text(100, 100, text="H", font=("Helvetica", 24, "bold"))
        else:
            self.canvas.create_oval(50, 50, 150, 150, fill="silver", outline="black", width=2)
            self.canvas.create_text(100, 100, text="T", font=("Helvetica", 24, "bold"))

    def flip(self):
        self.flip_button.config(state=tk.DISABLED)  # Disable the button during animation
        self.animate_flip()

    def animate_flip(self, frames=20, delay=50):
        outcomes = ["Heads", "Tails"]
        result = random.choice(outcomes)
        for _ in range(frames):
            self.master.after(delay, self.draw_coin, random.choice(outcomes))
            self.master.update()
        self.result_label.config(text=result)
        self.draw_coin(result)
        self.flip_button.config(state=tk.NORMAL)  # Enable the button after animation

def main():
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
