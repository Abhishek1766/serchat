import tkinter as tk
from tkinter import simpledialog

def ask_user_ip():
    ip_address = simpledialog.askstring("Input", "Please enter the server IP address:")
    return ip_address