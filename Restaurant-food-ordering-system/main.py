"""
Restaurant Table Reservation & Food Pre-Ordering System
Main Module

This module provides the user interface for the restaurant reservation system.
It handles menu display, user input, and calls appropriate database functions.
"""

from database import (
    create_database,
    reserve_table,
    view_reservations,
    pre_order_food,
    generate_bill
)


def display_menu():
    """
    Display the main menu for the Table Reservation System.
    
    Shows all available options for the user to interact with the system.
    """
    print("\n" + "=" * 36)
    print("TABLE RESERVATION SYSTEM")
    print("=" * 36)
    print("1. Reserve Table")
    print("2. View Reservations")
    print("3. Pre-Order Food")
    print("4. Generate Bill")
    print("5. Exit")
    print("=" * 36)


def get_valid_input(prompt, input_type=str, validation_func=None):
    """
    Get validated input from the user.
    
    Args:
        prompt (str): The prompt message to display
        input_type (type): The type to convert input to (default: str)
        validation_func (function): Optional validation function
    
    Returns:
        The validated input of specified type, or None if cancelled
    """
    while True:
        try:
            user_input = input(prompt)
            converted_input = input_type(user_input)
            
            if validation_func and not validation_func(converted_input):
                print("Invalid input. Please try again.")
                continue
                
            return converted_input
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None


def validate_positive_number(value):
    """
    Validate that a number is positive.
    
    Args:
        value (int or float): The value to validate
    
    Returns:
        bool: True if value is positive, False otherwise
    """
    return value > 0


def reserve_table_menu():
    """
    Handle the table reservation process.
    
    Prompts the user for customer details and booking information,
    then calls the reserve_table function to create the reservation.
    """
    print("\n--- Reserve a Table ---")
    
    try:
        # Get customer name
        customer_name = get_valid_input("Enter customer name: ")
        if not customer_name:
            return
        
        # Get phone number
        phone_number = get_valid_input("Enter phone number: ")
        if not phone_number:
            return
        
        # Get table number
        table_number = get_valid_input(
            "Enter table number: ",
            input_type=int,
            validation_func=validate_positive_number
        )
        if table_number is None:
            return
        
        # Get booking date
        booking_date = get_valid_input("Enter booking date (YYYY-MM-DD): ")
        if not booking_date:
            return
        
        # Get booking time
        booking_time = get_valid_input("Enter booking time (HH:MM): ")
        if not booking_time:
            return
        
        # Call the reserve_table function
        booking_id = reserve_table(
            customer_name,
            phone_number,
            table_number,
            booking_date,
            booking_time
        )
        
        if booking_id:
            print(f"\nReservation successful! Your Booking ID is: {booking_id}")
        else:
            print("\nReservation failed. Please try again.")
            
    except Exception as e:
        print(f"\nAn error occurred during reservation: {e}")


def pre_order_food_menu():
    """
    Handle the food pre-ordering process.
    
    Prompts the user for booking ID and allows multiple food items to be ordered,
    then calls the pre_order_food function for each item.
    """
    print("\n--- Pre-Order Food ---")
    
    try:
        # Get booking ID
        booking_id = get_valid_input(
            "Enter Booking ID: ",
            input_type=int,
            validation_func=validate_positive_number
        )
        if booking_id is None:
            return
        
        # Allow multiple food items
        while True:
            print("\nEnter food item details (or type 'done' to finish):")
            
            # Get food item name
            food_name = get_valid_input("Enter food item name: ")
            if not food_name or food_name.lower() == 'done':
                break
            
            # Get quantity
            quantity = get_valid_input(
                "Enter quantity: ",
                input_type=int,
                validation_func=validate_positive_number
            )
            if quantity is None:
                continue
            
            # Call the pre_order_food function
            success = pre_order_food(booking_id, food_name, quantity)
            
            if success:
                print(f"Added {quantity} x {food_name} to your order.")
            else:
                print(f"Failed to add {food_name}. Please check if the item exists in the menu.")
        
        print("\nPre-order process completed.")
        
    except Exception as e:
        print(f"\nAn error occurred during pre-ordering: {e}")


def generate_bill_menu():
    """
    Handle the bill generation process.
    
    Prompts the user for booking ID and calls the generate_bill function
    to display the bill details.
    """
    print("\n--- Generate Bill ---")
    
    try:
        # Get booking ID
        booking_id = get_valid_input(
            "Enter Booking ID: ",
            input_type=int,
            validation_func=validate_positive_number
        )
        if booking_id is None:
            return
        
        # Call the generate_bill function
        generate_bill(booking_id)
        
    except Exception as e:
        print(f"\nAn error occurred during bill generation: {e}")


def main():
    """
    Main function to run the Table Reservation System.
    
    Initializes the database and runs the main menu loop using match-case
    for option selection. Continues until the user chooses to exit.
    """
    # Initialize database when application starts
    print("Initializing database...")
    create_database()
    
    # Main menu loop
    while True:
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        # Use match-case for option selection
        match choice:
            case "1":
                reserve_table_menu()
            
            case "2":
                view_reservations()
            
            case "3":
                pre_order_food_menu()
            
            case "4":
                generate_bill_menu()
            
            case "5":
                print("\nThank you for using Table Reservation System!")
                print("Goodbye!")
                break
            
            case _:
                print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
