import requests
import tkinter as tk
from tkinter import messagebox

class ChatClient:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.root = tk.Tk()
        self.root.title("Chat Client")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        self.title_label = tk.Label(self.root, text="Chat Client", font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
        self.title_label.pack(pady=20)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(pady=10)

        self.send_button = tk.Button(self.root, text="Send Message", command=self.send_message, bg="#00cc66", fg="white")
        self.send_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app, bg="#ff4d4d", fg="white")
        self.exit_button.pack(pady=10)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            url = f'http://{self.ip_address}:5000/api/message'
            try:
                response = requests.post(url, json={'message': message})  # Ensure this is a POST request
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Message sent successfully!")
                else:
                    messagebox.showerror("Error", f"Failed to send message: {response.text}")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Message cannot be empty.")

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    client = ChatClient("127.0.0.1")  # Replace with your server's IP address if needed
    client.root.mainloop()