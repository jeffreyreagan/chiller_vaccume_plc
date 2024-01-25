# Connect to the PLC
from pylogix import PLC
import time
with PLC() as comm:

# Function to read the PLC tag and return the value
    def read_plc_tag():
        pump1vacuum = None  # Default value

        with PLC() as comm:
            comm.IPAddress = '172.16.21.12'  # Replace with your PLC's IP address
            comm.ProcessorSlot = 0  # Replace with your processor slot if needed

        # Define the tag to read
            tag = 'VACUUM_AT_PUMP_1'

            try:
            # Read the value of the tag
                result = comm.Read(tag)
                time.sleep(1)
                print(result)

            # Check if the read was successful
                if result.Status == 'Success':
                # Ensure the value is not None before storing
                    if result.Value is not None:
                        pump1vacuum = result.Value
                        pump1vacuum = pump1vacuum * .1  
                        pump1vacuum = str(pump1vacuum)+str(" Hg")
            except Exception as e:
                print(f"An error occurred: {e}")

        return pump1vacuum

    # Read the values of the tags and specific bits within them
    '''for tag in tags:
        for i in range(20):  # Assuming the array length is 20
            for bit in range(32):  # Assuming each integer has 32 bits
                element_tag = f"{tag}[{i}].{bit}"
                result = comm.Read(element_tag)
                if result.Status == 'Success':
                    value = result.Value
                    if value:
                        element_description = f"Element: {tag}[{i}].{bit}"
                        print(f"{element_description}, Value: {value}")
                else:
                    print(f"Failed to read tag: {element_tag}")'''


if __name__ == "__main__":
    plc_ip_address = "172.16.21.12"
    