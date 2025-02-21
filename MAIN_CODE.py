import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from openpyxl import Workbook

menu = {"pizza": 10, "burger": 5, "fries": 3, "soda": 2}

def save_order(order, table_no):
    wb = Workbook()
    ws = wb.active
    ws.append(["Item", "Quantity"])
    for item, quantity in order.items():
        ws.append([item, quantity])
    wb.save(f"orders_table_{table_no}.xlsx")

def show_menu(root):
    order = {}
    
    def add_to_order():
        selected_index = menu_listbox.curselection()
        if selected_index:
            selected_item = menu_listbox.get(selected_index)
            item, price = selected_item.split(': ')
            quantity_value = quantity_var.get()
            if quantity_value.strip():
                try:
                    quantity = int(quantity_value)
                    if quantity > 0:
                        order[item] = quantity
                        order_listbox.insert(tk.END, f"{item}: {quantity}")
                    else:
                        messagebox.showinfo("Invalid Quantity", "Please enter a valid quantity greater than 0.")
                except ValueError:
                    messagebox.showinfo("Invalid Quantity", "Please enter a valid integer quantity.")
            else:
                messagebox.showinfo("Invalid Quantity", "Please enter a valid quantity.")
        else:
            messagebox.showinfo("No Item Selected", "Please select an item from the menu.")
    
    def on_done_click():
        if not order:
            messagebox.showinfo("No Order", "Please add items to your order.")
            return
        total_price = sum(menu[item] * quantity for item, quantity in order.items())
        result = messagebox.askyesno("Order Summary", f"{'Nepali Fast Food NITJ':^80}\n\nYour order:\n\n{order}\n\nTotal: ₹{total_price}\n\nTable No: {table_no_var.get()}\n\nConfirm order?")
        if result:
            save_order(order, table_no_var.get())
            messagebox.showinfo("Order Confirmation", "Your order has been saved.")
    
    root.withdraw()
    window = tk.Toplevel(root)
    window.title("Order Menu")
    window.geometry("500x350")
    restaurant_name_label = tk.Label(window, text="THE NITJ RESTAURANT", font=("Arial", 16, "bold"), fg="dark green")
    restaurant_name_label.pack(side=tk.TOP, pady=(10, 5))
    table_frame = tk.Frame(window)
    table_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
    table_no_label = tk.Label(table_frame, text="Table No:")
    table_no_label.pack(side=tk.LEFT)
    table_no_var = tk.StringVar()
    table_no_entry = tk.Entry(table_frame, textvariable=table_no_var)
    table_no_entry.pack(side=tk.LEFT)
    menu_frame = tk.Frame(window, bg="whitesmoke")
    menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
    order_frame = tk.Frame(window, bg="whitesmoke")
    order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
    menu_label = tk.Label(menu_frame, text="Menu:", font=("Arial", 12, "bold"), fg="black", bg="white")
    menu_label.pack(side=tk.TOP, pady=(10, 5))
    order_label = tk.Label(order_frame, text="Order:", font=("Arial", 12, "bold"), fg="black", bg="white")
    order_label.pack(side=tk.TOP, pady=(10, 5))
    menu_listbox = tk.Listbox(menu_frame)
    menu_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    order_listbox = tk.Listbox(order_frame)
    order_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    quantity_label = tk.Label(order_frame, text="Quantity:", bg="white", fg="black")
    quantity_label.pack(side=tk.TOP)
    quantity_var = tk.StringVar()
    quantity_entry = tk.Entry(order_frame, textvariable=quantity_var)
    quantity_entry.pack(side=tk.TOP)
    for item, price in menu.items():
        menu_listbox.insert(tk.END, f"{item}: ₹{price}")
    add_button = ttk.Button(menu_frame, text="Add to Order", command=add_to_order, style="Red.TButton")
    add_button.pack(side=tk.BOTTOM, pady=5)
    done_button = ttk.Button(order_frame, text="Done", command=on_done_click, style="Red.TButton")
    done_button.pack(side=tk.BOTTOM, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    show_menu(root)
    root.mainloop()
