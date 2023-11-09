import tkinter as tk

class ATM(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Welcome message
        self.welcome_label = tk.Label(self, text="WELCOME TO ATM MACHINE", font=("Arial", 16, "bold"))
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username and password
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.password_label = tk.Label(self, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login, font=("Arial", 12))
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Current amount
        self.current_amount_label = tk.Label(self, text="Current amount:", font=("Arial", 12))
        self.current_amount_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.current_amount_entry = tk.Entry(self, state="disabled", font=("Arial", 12))
        self.current_amount_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # Options
        self.options_label = tk.Label(self, text="Options:", font=("Arial", 12))
        self.options_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.options_frame = tk.Frame(self)
        self.options_frame.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        self.add_money_button = tk.Button(self.options_frame, text="Add money", command=self.add_money, state="disabled", font=("Arial", 12))
        self.add_money_button.grid(row=0, column=0, pady=5)

        self.withdraw_money_button = tk.Button(self.options_frame, text="Withdraw money", command=self.withdraw_money, state="disabled", font=("Arial", 12))
        self.withdraw_money_button.grid(row=1, column=0, pady=5)

        self.check_balance_button = tk.Button(self.options_frame, text="Check balance", command=self.check_balance, state="disabled", font=("Arial", 12))
        self.check_balance_button.grid(row=2, column=0, pady=5)

        self.logout_button = tk.Button(self.options_frame, text="Logout", command=self.logout, state="disabled", font=("Arial", 12))
        self.logout_button.grid(row=3, column=0, pady=5)

        self.current_amount = 0

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simulated login for demonstration purposes
        if username == "user" and password == "password":
            print("Login successful")
            self.current_amount_entry.config(state="normal")
            self.add_money_button.config(state="normal")
            self.withdraw_money_button.config(state="normal")
            self.check_balance_button.config(state="normal")
            self.logout_button.config(state="normal")
        else:
            print("Invalid username or password")

    def add_money(self):
        amount = 0
        try:
            amount = int(self.add_money_entry.get())
        except ValueError:
            print("Please enter a valid amount")
            return

        self.current_amount += amount
        print("New amount:", self.current_amount)

    def withdraw_money(self):
        amount = 0
        try:
            amount = int(self.withdraw_money_entry.get())
        except ValueError:
            print("Please enter a valid amount")
            return

        if self.current_amount >= amount:
            self.current_amount -= amount
            print("New amount:", self.current_amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.current_amount)

    def logout(self):
        print("Goodbye!")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ATM Machine")
    root.geometry("400x300")
    atm = ATM(root)
    atm.pack(fill="both", expand=True, padx=20, pady=10)
    root.mainloop()
  