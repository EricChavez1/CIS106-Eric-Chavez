def format_name():
    try:
        
        name_input = input("Enter a first and last name ( Firstname Lastname): ").strip()
        
        
        name_parts = name_input.split()
        
        
        if len(name_parts) != 2:
            raise ValueError("Input must contain exactly one first name and one last name.")
        
        first_name, last_name = name_parts
        
        
        formatted_name = f"{last_name}, {first_name[0].upper()}."
        print(f"Formatted Name: {formatted_name}")
    
    except ValueError as e:
        print(f"Error: {e}")


format_name()
