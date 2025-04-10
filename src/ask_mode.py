import tkinter as tk
from tkinter import simpledialog

def ask_user_mode():
    mode = simpledialog.askstring("Input", "Select mode (client/server):")
    return mode