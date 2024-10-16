import argparse
import os
import sys
from ryena.brainbank import BrainBank

STATE_FILE = 'ryena_state.txt'

def load_state():
    ## Loading activation state from a file ##
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return f.read().strip() == 'True'
    return False

def save_state(is_activated):
    ## Save activation state to a file ##
    with open(STATE_FILE, 'w') as f:
        f.write(str(is_activated))

is_activated = load_state()

active_services = {} ## Dictionary to track active services ##

def show_help():
    commands = [
            'activate   - Activate ryena',
            'brainbank  - Start the BrainBank Service',
            'help       - Shows Lists of Commands',
            'exit       - Exit ryena'
            ]

    print('available commands:')
    for command in commands:
        print(f' {command}')

def main():
    global is_activated

    parser = argparse.ArgumentParser(description='ryena CLI Interface')
    parser.add_argument('command', nargs='?', type=str, help='Command to run')
    args = parser.parse_args()

    if args.command is None:
        print('Welcome to ryena')
        print('')
        show_help()
        return

    if args.command == 'activate':
        is_activated = True
        save_state(is_activated)
        print("\033[92m<ryena>\033[0m")
        print(f"Is activated: {is_activated}")
    elif args.command == 'brainbank':
        print(f"Is activated: {is_activated}")
        if not is_activated:
            print("ryena must be activated first. Call 'ryena activate'.")
        else:
            BrainBank().run()

    elif args.command == 'help':
        show_help()

    else:
        print("Command was not recognized. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    main()
