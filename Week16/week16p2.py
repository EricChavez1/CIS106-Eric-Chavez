def get_input():
    """Get a line of text from the user."""
    return input("Enter a line of text: ")

def clean_text(text):
    """Remove leading, trailing, and duplicate spaces from the text."""
    return ' '.join(text.split())

def reverse_text(text):
    """Reverse the cleaned text."""
    return text[::-1]

def display_output(text):
    """Display the processed text."""
    print(f"Processed Text: {text}")

def main():
    """Main function to tie all subroutines together."""
    user_input = get_input()
    cleaned_text = clean_text(user_input)
    reversed_text = reverse_text(cleaned_text)
    display_output(reversed_text)



main()
