import tkinter as tk
from tkinter import messagebox

# Function to show the second screen with price, warranty, and build quality buttons
def show_details_screen(appliance_name):
    # Create a new window
    details_window = tk.Toplevel(root)
    details_window.title(f"{appliance_name} Details")
    details_window.configure(bg='black')# Set the background color to black

    # Function to show the answer when a detail button is clicked
    def show_answer(detail_type):
        answers = {
            "TV": {
                "Brand":"Haier",
                "Price": "1200$",
                "Warranty": "The TV comes with a 1-year warranty.",
                "Build Quality": "The TV is made of steel with a slim and modern design.",
                "Size":"43 Inches"
            },
            "Fridge": {
                "Brand":"Samsung",
                "Price": "500$",
                "Warranty": "The fridge comes with a 5-year warranty.",
                "Build Quality": "The fridge is built with stainless steel, keeping the food in the right temprature.",
                "Size": "65x60x120 cm"
            },
            "Washing Machine": {
                "Brand": "Panasonic",
                "Price": "750$",
                "Warranty": "The washing machine comes with a 3-year warranty.",
                "Build Quality": "The washing machine is made with a rust-resistant body and shock-proof design.",
                "Size": "50X55X80 cm"
            },
            "Microwave": {
                "Brand":"Agaro",
                "Price":"100$",
                "Warranty":"The Microwave comes with a 2-year warranty.",
                "Build Quality":"Durable materials, solid construction, and reliable design ensure longevity and safety.",
                "Size":"30x20x25 cm"
             },
            "Dishwasher": {
                 "Brand":"Bosch",
                "Price":"400$",
                "Warranty":"The Dishwasher comes with a 15-year warranty.",
                "Build Quality":"Sturdy stainless steel interior, robust racks, and well-sealed door for durability and efficient cleaning.",
                "Size":"60x45x50cm"
            }
        }
        
        answer = answers[appliance_name][detail_type]
        # Show the answer in a messagebox with black background
        messagebox.showinfo(f"{appliance_name} {detail_type}", answer)

    # Create detail buttons
    button_brand = tk.Button(details_window, text="Brand",font=("Arial", 10), command=lambda: show_answer("Brand"),bg='#ffd100')
    button_price = tk.Button(details_window, text="Price",font=("Arial", 10), command=lambda: show_answer("Price"),bg='#ffd100')
    button_warranty = tk.Button(details_window, text="Warranty",font=("Arial", 10), command=lambda: show_answer("Warranty"),bg='#ffd100')
    button_build_quality = tk.Button(details_window, text="Build Quality",font=("Arial", 10), command=lambda: show_answer("Build Quality"),bg='#ffd100')
    button_size = tk.Button(details_window, text="Size",font=("Arial", 10), command=lambda: show_answer("Size"),bg='#ffd100')

    # Arrange buttons on the details window
    button_brand.pack(pady=10)
    button_price.pack(pady=10)
    button_warranty.pack(pady=10)
    button_build_quality.pack(pady=10)
    button_size.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Gadget Review System")
root.configure(bg='black')  # Set the background color to black
root.attributes("-fullscreen", True)
tk.Label(root, text="Gadget review system", font=("Arial", 50),bg='#ffd100').place(x=300,y=50)

# Create main buttons
button_tv = tk.Button(root, text="TV",font=("Arial", 25), command=lambda: show_details_screen("TV"),bg='#ffd100')
button_fridge = tk.Button(root, text="Fridge",font=("Arial", 25), command=lambda: show_details_screen("Fridge"),bg='#ffd100')
button_washing_machine = tk.Button(root, text="Washing Machine",font=("Arial", 25), command=lambda: show_details_screen("Washing Machine"),bg='#ffd100')
button_microwave = tk.Button(root, text="Microwave",font=("Arial", 25), command=lambda: show_details_screen("Microwave"),bg='#ffd100')
button_dishwasher = tk.Button(root, text="Dishwasher",font=("Arial", 25), command=lambda: show_details_screen("Dishwasher"),bg='#ffd100')

# Arrange main buttons on the window
button_tv.place(x=230, y=250)
button_fridge.place(x=560, y=250)
button_washing_machine.place(x=880, y=250)
button_microwave.place(x=370, y=450)
button_dishwasher.place(x=710, y=450)

# Start the main loop
root.mainloop()
