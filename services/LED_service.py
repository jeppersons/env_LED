import smbus2 as smbus
import qwiic_led_stick
import time

# Initialize I2C bus
bus = smbus.SMBus(1)

# Function to select the mux channel
def select_mux_channel(channel):
    mux_address = 0x70
    bus.write_byte(mux_address, 1 << channel)

# Function to control the LED stick
def control_led_stick(channel):
    select_mux_channel(channel)  # Select the specified channel
    stick_address = 0x23  # Address of the LED stick
    stick = qwiic_led_stick.QwiicLEDStick(address=stick_address)
    
    if stick.begin() == False:
        print(f"LED Stick on channel {channel} isn't connected.")
        return False

    num_leds = 10  # Adjust based on your LED stick

    # Example: Light up LEDs in a color
    for i in range(num_leds):
        stick.set_single_LED_color(i, 255, 0, 0)  # Red color
        time.sleep(0.5)

    stick.set_all_LED_color(0, 0, 0)  # Turn off all LEDs

    return True

# Control LED sticks on channels 0 and 3
control_led_stick(0)  # Control stick on channel 0
time.sleep(10)  # Wait some time before switching to the next stick
control_led_stick(3)  # Control stick on channel 3
