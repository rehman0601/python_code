import sys

def print_command_line_args():
    # sys.argv contains the list of command-line arguments
    print("Command-line arguments:")
    for arg in sys.argv:
        print(arg)

# This function will print the command-line arguments passed to the script.
print_command_line_args()
