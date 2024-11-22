Keyboard Interrupt Handler Script
Description
This Python script demonstrates how to use the keyboard library to capture key presses and releases, and execute a custom interrupt handler function whenever a key event occurs. The script logs information about key events using the raphlel logger.

Requirements
Python 3.x

keyboard library (pip install keyboard)

raphlel library for logging

Installation
git clone https://github.com/HackingHusky/interrupt-handler
cd interrupt-handler

Install the required libraries:
pip install keyboard raphlel

Usage
python keyboard_interrupt_handler.py

Customize the Interrupt Handler:

Modify the my_interrupt_handler function to perform different actions when a key event occurs.

Notes
Ensure you have the necessary permissions to capture keyboard events on your system.

This script runs indefinitely, listening for key events. Use Ctrl + C to terminate the script.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
keyboard library documentation for providing key event handling functionality.

raphlel library documentation for logging capabilities.
