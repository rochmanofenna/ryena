import os  # Importing the os module for interacting with the operating system

class BrainBank:
    def __init__(self, base_path='brainbank/'):
        # Initialize the BrainBank class
        # Create a list of folders in the current directory that are directories
        self.base_path = base_path
        self.folders = [f for f in os.listdir('.') if os.path.isdir(f)]
        # Path to the instructions text file
        self.instructions_path = os.path.join(self.base_path, 'instructions.txt')
        self.folders = [f for f in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, f))]

    def run(self):
        self.show_instructions()
        # Main method to run the BrainBank functionality
        if not self.folders:
            # Check if there are no folders; prompt user to create one
            print("No folders found. Please create a folder before using BrainBank.")
            return  # Exit the run method if no folders are found
        
        create_folder = input('Do you want to create a new folder? (y/n)')
        if create_folder == 'y':
            folder_name = input('Enter the name of the new folder')
            self.create_folder(folder_name)

        self.folders = [f for f in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, f))]
        
        # Display available folders to the user
        print("Folders available under brainbank:")
        for folder in self.folders:
            print(f"- {folder}")  # Print each folder name
        
        # Prompt user to enter a folder name or request instructions
        command = input("Enter a folder name or 'instructions' to see how to use BrainBank: ")
        
        if command == 'instructions':
            self.show_instructions() # If the user requests instructions, show them
        elif command in self.folders:
            self.use_brainbank(folder=command) # If the command matches a folder name, use that folder
        else:
            print("Invalid folder name.") # If the input is invalid (not a folder or 'instructions'), notify the user

    def create_folder(self, folder_name):
        """Create a new folder in the brainbank directory."""
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder '{folder_name}' created successfully.")
        except Exception as e:
            print(f"Error creating folder: {e}")

    def show_instructions(self):
        # Method to display instructions from the instructions file
        if os.path.exists(self.instructions_path):
            # Check if the instructions file exists
            with open(self.instructions_path, 'r') as file:
                instructions = file.read()  # Read the content of the file
                print("\nInstructions:\n") 
                print(instructions)  # Print the instructions to the user
        else:
            # Notify the user if the instructions file is not found
            print("Instructions file not found.")

    def use_brainbank(self, folder):
        print(f"You are now in the '{folder}' folder. You can now input your question (q/?), comment (c/#), or idea(i/$).")
        

