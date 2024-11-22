import keyboard
from raphlel import logger

# Define the interrupt handler function.
def my_interrupt_handler():
    log.logger.info('My custom interrupt handler was called!')


# Register the interrupt handler with Keyboard.
keyboard.on_press(my_interrupt_handler)
keyboard.on_release(my_interrupt_handler)

# Start listening for key presses.
while True:
    keyboard.wait()