def get_input():
    """Prompt the user for the required inputs."""
    text = input("Enter a line of text: ")
    char_per_line = int(input("Enter the number of characters per line: "))
    num_lines = int(input("Enter the number of lines to print: "))
    scroll_direction = input("Enter the scroll direction (left or right): ").strip().lower()
    return text, char_per_line, num_lines, scroll_direction

def format_text(text, char_per_line):
    """Duplicate the text as needed to fill the specified number of characters per line."""
    while len(text) < char_per_line:
        text += text
    return text[:char_per_line]

def scroll_line(line, direction):
    """Shift the line by one character in the specified direction."""
    if direction == "left":
        return line[1:] + line[0]
    elif direction == "right":
        return line[-1] + line[:-1]
    else:
        raise ValueError("Invalid direction. Use 'left' or 'right'.")

def print_scrolling_lines(text, num_lines, direction):
    """Print the requested number of lines, scrolling the text in the specified direction."""
    current_line = text
    for _ in range(num_lines):
        print(current_line)
        current_line = scroll_line(current_line, direction)

def main():
    """Main function to tie all subroutines together."""
    try:
       
        text, char_per_line, num_lines, scroll_direction = get_input()
        
       
        formatted_text = format_text(text, char_per_line)
        
        
        print_scrolling_lines(formatted_text, num_lines, scroll_direction)
    except ValueError as e:
        print(f"Error: {e}")


main()
