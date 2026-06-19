"""
Restaurant Food Ordering System - Main Application

This module provides a command-line interface for the restaurant food ordering system.
It allows users to place orders, view orders, and generate bills.
"""

from database import create_database, place_order, view_orders, generate_bill


def display_menu():
    """
    Display the main menu options for the Restaurant Food Ordering System.
    """
    print("\n" + "=" * 40)
    print("RESTAURANT FOOD ORDERING SYSTEM")
    print("=" * 40)
    print("1. Place Order")
    print("2. View All Orders")
    print("3. View Specific Order")
    print("4. Generate Bill")
    print("5. Exit")
    print("=" * 40)


def place_order_menu():
    """
    Handle the place order menu option.
    
    Prompts the user for customer name, table number, and multiple food items
    with quantities. Validates input and places the order using the database function.
    """
    print("\n--- Place Order ---")
    
    try:
        # Get customer name
        customer_name = input("Enter customer name: ").strip()
        if not customer_name:
            print("Error: Customer name cannot be empty.")
            return
        
        # Get table number with validation
        while True:
            table_input = input("Enter table number: ").strip()
            try:
                table_number = int(table_input)
                if table_number <= 0:
                    print("Error: Table number must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid integer for table number.")
        
        # Get menu items and quantities
        items = []
        print("\nEnter menu items (enter 'done' when finished):")
        print("Available items: Burger, Pizza, Ice Cream")
        
        while True:
            item_name = input("  Item name (or 'done' to finish): ").strip()
            
            # Check if user wants to finish adding items
            if item_name.lower() == 'done':
                if not items:
                    print("Error: At least one item must be added to place an order.")
                    continue
                break
            
            if not item_name:
                print("Error: Item name cannot be empty.")
                continue
            
            # Get quantity with validation
            while True:
                quantity_input = input(f"  Quantity for {item_name}: ").strip()
                try:
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Error: Quantity must be a positive integer.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid integer for quantity.")
            
            # Add item to the list as a tuple
            items.append((item_name, quantity))
            print(f"  Added: {item_name} x{quantity}")
        
        # Place the order
        order_id = place_order(customer_name, table_number, items)
        
        if order_id:
            print(f"\nSuccess: Order placed successfully with Order ID: {order_id}")
        else:
            print("\nError: Failed to place order. Please try again.")
    
    except KeyboardInterrupt:
        print("\n\nOrder placement cancelled by user.")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {e}")


def view_specific_order_menu():
    """
    Handle the view specific order menu option.
    
    Prompts the user for an Order ID and displays the details of that specific order.
    Validates the Order ID input.
    """
    print("\n--- View Specific Order ---")
    
    try:
        # Get Order ID with validation
        while True:
            order_id_input = input("Enter Order ID: ").strip()
            try:
                order_id = int(order_id_input)
                if order_id <= 0:
                    print("Error: Order ID must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid integer for Order ID.")
        
        # View the specific order
        view_orders(order_id)
    
    except KeyboardInterrupt:
        print("\n\nView order cancelled by user.")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {e}")


def generate_bill_menu():
    """
    Handle the generate bill menu option.
    
    Prompts the user for an Order ID and generates a bill for that order.
    Validates the Order ID input.
    """
    print("\n--- Generate Bill ---")
    
    try:
        # Get Order ID with validation
        while True:
            order_id_input = input("Enter Order ID: ").strip()
            try:
                order_id = int(order_id_input)
                if order_id <= 0:
                    print("Error: Order ID must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid integer for Order ID.")
        
        # Generate the bill
        bill = generate_bill(order_id)
        
        if bill:
            print(f"\nSuccess: Bill generated for Order ID: {order_id}")
        else:
            print(f"\nError: Failed to generate bill for Order ID: {order_id}")
    
    except KeyboardInterrupt:
        print("\n\nBill generation cancelled by user.")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {e}")


def main():
    """
    Main function to run the Restaurant Food Ordering System.
    
    Initializes the database and runs the main menu loop until the user
    chooses to exit. Uses match-case for menu option handling.
    """
    # Initialize the database
    print("Initializing Restaurant Food Ordering System...")
    create_database()
    print("System initialized successfully.\n")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        # Handle menu selection using match-case
        match choice:
            case "1":
                place_order_menu()
            case "2":
                print("\n--- View All Orders ---")
                view_orders()
            case "3":
                view_specific_order_menu()
            case "4":
                generate_bill_menu()
            case "5":
                print("\nThank you for using Restaurant Food Ordering System")
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
