#!/bin/bash

# Check the user's shell
if [ "$SHELL" = "/bin/bash" ]; then
    CONFIG_FILE="$HOME/.bashrc"
elif [ "$SHELL" = "/bin/zsh" ]; then
    CONFIG_FILE="$HOME/.zshrc"
else
    echo "Unsupported shell. Please add the following alias manually:"
    echo "alias ryena='python3 -m ryena.cli_logic'"
    exit 1
fi

# Add the alias to the appropriate config file
echo "alias ryena='python3 -m ryena.cli_logic'" >> "$CONFIG_FILE"
echo "Alias added to $CONFIG_FILE. Please run 'source $CONFIG_FILE' to apply the changes."

# Optionally inform the user
echo "Setup complete! You can now use the 'ryena' command."

