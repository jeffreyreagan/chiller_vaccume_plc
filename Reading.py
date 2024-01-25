# Connect to the PLC
from pylogix import PLC
import time


# Function to read the PLC tag and return the value
def read_plc_tag():
        try:
            with PLC() as comm:
                comm.IPAddress = '172.16.21.12'  # Replace with your PLC's IP address
                comm.ProcessorSlot = 0  # Replace with your processor slot if needed

        # Define the tag to read
                tags = ['VACUUM_AT_PUMP_1','VACUUM_AT_PUMP_2']
                pump1vacuum = None
                pump2vacuum = None
            
            # Read the value of the tag
                results = comm.Read(tags)
                print(results)
                for result in results:
                    if result.Status == 'Success':
                        if result.TagName == 'VACUUM_AT_PUMP_1':
                            result.Value *= 0.1
                            pump1vacuum_formatted = "{:.2f}".format(result.Value)
                            pump1vacuum = str(pump1vacuum_formatted) + " Hg"
                            
                        elif result.TagName == 'VACUUM_AT_PUMP_2':
                            result.Value *= 0.1
                            pump2vacuum_formatted = "{:.2f}".format(result.Value)
                            pump2vacuum = str(pump2vacuum_formatted) + " Hg"
                            
                return pump1vacuum, pump2vacuum
            # Check if the read was successful
                
        except Exception as e:
                    print(f"An error occurred: {e}")

                   
        

    # Read the values of the tags and specific bits within them



if __name__ == "__main__":
    plc_ip_address = "172.16.21.12"



'''Still figuring out array data formatting     for tag in tags:
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