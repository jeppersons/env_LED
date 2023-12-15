import smbus2 as smbus
import qwiic_led_stick
import time

# Initialize I2C bus
bus = smbus.SMBus(1)

# Function to select the mux channel
def select_mux_channel(channel):
    mux_address = 0x70
    bus.write_byte(mux_address, 1 << channel)

# Control the LED stick on channel 0
def control_led_stick(stick_address):
    select_mux_channel(0)  # Select channel 0
    stick = qwiic_led_stick.QwiicLEDStick(address=stick_address)
    if stick.begin() == False:
        print("LED Stick on channel 0 isn't connected.")
        return False

    num_leds = 10  # Number of LEDs on your stick

    # Example: Turn on each LED in red, one by one
    for i in range(num_leds):
        stick.set_single_LED_color(i, 255, 0, 0)  # Set LED at index i to red color
        time.sleep(0.5)

    # Turn off all LEDs at the end
    stick.set_all_LED_color(0, 0, 0)  # Turn off all LEDs (set color to black)

    return True

# Replace 0x23 with the actual I2C address of your LED stick
control_led_stick(0x23)
