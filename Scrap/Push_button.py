import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# def button_callback(channel):
#     print("Button was pushed!")
    
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 7 to be an input pin and set initial value to be pulled low (off)
# GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback) # Setup event on pin 7 rising edge
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up

""" HSG NightLight Step 1 - First experience with GPIOs
"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals


class ButtonTrial:
    """ The HSG NightLight class.
    Features provided:
    - The red LED is enabled while the button is pressed
    - The green LED toggles enabled state when the button is pressed
    - The blue LED blinks continuously
    - A long-press stops the program
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """
        # state
        self._keep_running = True  
        self._setup_hardware()

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """
        self._button = gpiozero.Button(7,hold_time=2,hold_repeat=False,pull_up=True)
        self._button.when_pressed = self._on_button_press

    def _on_button_press(self):
        """ Event handler, called when the button is pressed. """
        print("Button was pressed")
        
    def run(self):
        """ Run the main loop, periodically checking for events.
        This function only exits at device shutdown.
        """
        print("Entered main loop")
        while self._keep_running:

        # we're stopping, do some cleanup

        print("Leaving main loop")

# Main entry point
if __name__ == "__main__":
    buttontry = ButtonTrial()

    # run the instance
    buttontry.run()