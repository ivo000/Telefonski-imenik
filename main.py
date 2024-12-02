# main.py

import tkinter as tk
from gui import TelefonskiImenikGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TelefonskiImenikGUI(root)
    root.mainloop()
