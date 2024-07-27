def calculate_price(item_price, count, gst_rate):
    item_total = item_price * count
    gst = (item_total * gst_rate) / 100
    return item_total + gst

def get_order_details(item_name, item_price, gst_rate):
    print(f"***********{item_name.upper()} - {item_price}rs***********")
    count = int(input(f"How Many {item_name.capitalize()} : "))
    total_price = calculate_price(item_price, count, gst_rate)
    print(f"Total {item_name} price is {total_price} (Include GST)")
    return total_price

def main():
    print("# WELCOME TO KARTHI SUPER MARKET")
    your_order = input("Choose your Product (grocery, snacks): ").lower()

    if your_order == "grocery":
        grocery_items = {
            "rice": (120, 18),
            "wheat": (85, 16),
            "oil": (118, 12),
            "salt": (38, 15),
            "sugar": (57, 21)
        }
        grocery_order = input("Do You Want to Order (Yes or No): ").lower()
        if grocery_order == "yes":
            total_bill = 0
            for item, (price, gst) in grocery_items.items():
                total_bill += get_order_details(item, price, gst)
            print("****************** KARTHI SUPER MARKET *********************")
            print(f"Your Total Bill is {total_bill} (Include GST)")

    elif your_order == "snacks":
        snacks_items = {
            "biscuit": (25, 20),
            "ice cream": (45, 25),
            "chocolate": (65, 27)
        }
        snacks_order = input("Do You Want to Order (Yes or No): ").lower()
        if snacks_order == "yes":
            total_bill = 0
            for item, (price, gst) in snacks_items.items():
                total_bill += get_order_details(item, price, gst)
            print("****************** KARTHI SUPER MARKET *********************")
            print(f"Your Total Bill is {total_bill} (Include GST)")

    else:
        print("THANK YOU")

if __name__ == "__main__":
    main()