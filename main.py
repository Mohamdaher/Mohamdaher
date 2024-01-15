import tkinter as tk
from tkinter import messagebox

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class CashierSystem:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return True
        return False

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for item in self.items:
                file.write(f"{item.name},{item.price},{item.quantity}\n")

    def load_data(self, filename):
        self.items = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.add_item(Item(name, float(price), int(quantity)))
        except FileNotFoundError:
            pass

class CashierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cashier System")

        self.cashier_system = CashierSystem()
        self.cashier_system.load_data('items.txt')

        self.item_name_var = tk.StringVar()
        self.item_price_var = tk.DoubleVar()
        self.item_quantity_var = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Item Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.item_name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Item Price:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.item_price_var).grid(row=1, column=1)

        tk.Label(self.root, text="Item Quantity:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.item_quantity_var).grid(row=2, column=1)

        tk.Button(self.root, text="Add Item", command=self.add_item).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Remove Item", command=self.remove_item).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Show Total", command=self.show_total).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Save Data", command=self.save_data).grid(row=6, column=0, pady=10)
        tk.Button(self.root, text="Load Data", command=self.load_data).grid(row=6, column=1, pady=10)

    def add_item(self):
        name = self.item_name_var.get()
        price = self.item_price_var.get()
        quantity = self.item_quantity_var.get()

        item = Item(name, price, quantity)
        self.cashier_system.add_item(item)

        messagebox.showinfo("Success", "Item added successfully!")

    def remove_item(self):
        name = self.item_name_var.get()

        if self.cashier_system.remove_item(name):
            messagebox.showinfo("Success", f"{name} removed successfully!")
        else:
            messagebox.showwarning("Error", f"{name} not found!")

    def show_total(self):
        total = self.cashier_system.calculate_total()
        messagebox.showinfo("Total", f"Total: ${total:.2f}")

    def save_data(self):
        self.cashier_system.save_data('items.txt')
        messagebox.showinfo("Success", "Data saved successfully!")

    def load_data(self):
        self.cashier_system.load_data('items.txt')
        messagebox.showinfo("Success", "Data loaded successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CashierGUI(root)
    root.mainloop()
