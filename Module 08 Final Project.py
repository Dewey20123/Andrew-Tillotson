import tkinter as tk
from tkinter import messagebox

# Function to handle Income Window
def open_income_window():
    income_window = tk.Toplevel(root)
    income_window.title("Income Window")
    
    # Income input fields
    tk.Label(income_window, text="Enter income amount:").pack()
    income_entry = tk.Entry(income_window)
    income_entry.pack()
    
    tk.Label(income_window, text="Income source:").pack()
    source_entry = tk.Entry(income_window)
    source_entry.pack()

    def add_income():
        income = income_entry.get()
        source = source_entry.get()
        
        if not income or not source:
            messagebox.showwarning("Input Error", "Please fill in both fields.")
            return
        
        try:
            income = float(income)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for income.")
            return
        
        # Store income data in a list or database
        messagebox.showinfo("Income Added", f"Income of ${income} from {source} added!")
        income_window.destroy()

    # Add Income button
    tk.Button(income_window, text="Add Income", command=add_income).pack()

# Function to handle Expense Window
def open_expense_window():
    expense_window = tk.Toplevel(root)
    expense_window.title("Expense Window")
    
    # Expense input fields
    tk.Label(expense_window, text="Enter expense amount:").pack()
    expense_entry = tk.Entry(expense_window)
    expense_entry.pack()

    tk.Label(expense_window, text="Expense description:").pack()
    description_entry = tk.Entry(expense_window)
    description_entry.pack()

    def add_expense():
        expense = expense_entry.get()
        description = description_entry.get()
        
        if not expense or not description:
            messagebox.showwarning("Input Error", "Please fill in both fields.")
            return
        
        try:
            expense = float(expense)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for expense.")
            return
        
        #Store expense data in a list or database
        messagebox.showinfo("Expense Added", f"Expense of ${expense} for {description} added!")
        expense_window.destroy()

    # Add Expense button
    tk.Button(expense_window, text="Add Expense", command=add_expense).pack()

# Function to display Summary Window
def show_summary():
    summary_window = tk.Toplevel(root)
    summary_window.title("Summary Window")
    
    #calculate totals from saved data
    total_income = 1000  
    total_expenses = 500  
    remaining_budget = total_income - total_expenses
    
    tk.Label(summary_window, text=f"Total Income: ${total_income}").pack()
    tk.Label(summary_window, text=f"Total Expenses: ${total_expenses}").pack()
    tk.Label(summary_window, text=f"Remaining Budget: ${remaining_budget}").pack()

# Function to exit the program
def exit_program():
    root.quit()

# Main window setup
root = tk.Tk()
root.title("The Budgeter")
root.geometry("500x500")

# Add title to main window
tk.Label(root, text="Welcome to The Budgeter", font=("Helvetica", 16, "bold")).pack(pady=10)

# Main window buttons
tk.Button(root, text="Add Income", command=open_income_window).pack(pady=10)
tk.Button(root, text="Add Expense", command=open_expense_window).pack(pady=10)
tk.Button(root, text="Show Summary", command=show_summary).pack(pady=10)
tk.Button(root, text="Exit", command=exit_program).pack(pady=10)

root.mainloop()
