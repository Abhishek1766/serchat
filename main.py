import tkinter as tk
from tkinter import messagebox
from src import client_mode, server_mode, ask_ip, ask_mode
import threading

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("SerChat")
        self.master.geometry("400x300")
        self.master.configure(bg="#1e1e1e")

        self.title_label = tk.Label(master, text="Ser Chat", font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
        self.title_label.pack(pady=20)

        self.start_mode_button = tk.Button(master, text="Select Mode", command=self.select_mode, width=20, bg="#007acc", fg="white")
        self.start_mode_button.pack(pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app, width=20, bg="#ff4d4d", fg="white")
        self.exit_button.pack(pady=10)

    def select_mode(self):
        mode = ask_mode.ask_user_mode()  # Function to ask user for mode
        if mode == "client":
            ip_address = ask_ip.ask_user_ip()  # Function to ask for IP address
            if ip_address:
                client = client_mode.ChatClient(ip_address)
                client.run()
        elif mode == "server":
            server = server_mode.ChatServer()
            # Start the server in a new thread
            server_thread = threading.Thread(target=server.run)
            server_thread.start()
        else:
            messagebox.showerror("Error", "Invalid mode selected!")

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()