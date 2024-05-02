import spidev
import time

# Define SPI bus and CE pin for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read ADC channel
def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        # Read analog input from MQ7 sensor connected to CH0 of MCP3008
        mq7_level = read_adc(0)
        # Convert ADC value to voltage (assuming 3.3V)
        voltage = mq7_level * 3.3 / 1023
        # Print ADC value and voltage
        print("MQ7 ADC Value: {}, Voltage: {:.2f}V".format(mq7_level, voltage))
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Ctrl+C pressed, exit cleanly
    spi.close()
