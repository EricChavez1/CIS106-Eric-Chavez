def get_input():
    """Prompt the user to enter a line of comma-separated values."""
    return input("Enter a line of comma-separated values: ")

def parse_csv(line):
    """Parse the CSV line into individual items, removing leading/trailing spaces."""
    items = line.split(',')
    return [item.strip() for item in items]

def display_items(items):
    """Print each item on a separate line."""
    print("Parsed Items:")
    for item in items:
        print(item)

def main():
    """Main function to tie all subroutines together."""
    csv_line = get_input()
    parsed_items = parse_csv(csv_line)
    display_items(parsed_items)


main()
