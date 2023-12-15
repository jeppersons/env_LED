import smbus2 as smbus
import time

# Initialize I2C bus
bus = smbus.SMBus(1)

# Function to select the mux channel
def select_mux_channel(channel):
    mux_address = 0x70
    bus.write_byte(mux_address, 1 << channel)

# Test each channel
for channel in range(4):  # Adjust the range if your multiplexer has a different number of channels
    select_mux_channel(channel)
    print(f"Testing channel {channel}")
    # Now manually run `i2cdetect -y 1` in the terminal to see if the LED stick appears on this channel
    time.sleep(5)  # Wait for 5 seconds before changing to the next channel
