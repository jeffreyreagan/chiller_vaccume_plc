# Connect to the PLC
from pylogix import PLC
import time


# Function to read the PLC tags for vacuum pressure and return the value in a readable format
def read_plc_tag():
        try:
            with PLC() as comm:
                comm.IPAddress = '172.16.21.12' 
                comm.ProcessorSlot = 0  
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

def read_alarm_tags_all_pumps(tag_names):
    try:
        with PLC() as comm:
            comm.IPAddress = 'your_plc_ip_address'  # Replace with your PLC's IP address
            comm.ProcessorSlot = 0  # Replace with your processor slot if needed
            
            results = comm.Read(tag_names)

            tag_values = {}
            for result in results:
                if result.Status == 'Success':
                    tag_values[result.TagName] = result.Value
                else:
                    tag_values[result.TagName] = None

            return tag_values

    except Exception as e:
        print(f"An error occurred: {e}")

    return None

# Example usage:
pump1_alarm_tags = ['VPUMP_1_B10[2].0', 'VPUMP_1_B10[2].1', 'VPUMP_1_B10[2].2', 'VPUMP_1_B10[2].3', 'VPUMP_1_B10[2].4', 'VPUMP_1_B10[2].5', 'VPUMP_1_B10[2].6', 'VPUMP_1_B10[2].7', 'VPUMP_1_B10[2].8', 'VPUMP_1_B10[2].9', 'VPUMP_1_B10[2].10', 'VPUMP_1_B10[2].11', 'VPUMP_1_B10[2].12', 'VPUMP_1_B10[2].13', 'VPUMP_1_B10[2].14', 'VPUMP_1_B10[2].15']
pump2_alarm_tags= ['VPUMP_2_B10[2].0', 'VPUMP_2_B10[2].1', 'VPUMP_2_B10[2].2', 'VPUMP_2_B10[2].3', 'VPUMP_2_B10[2].4', 'VPUMP_2_B10[2].5', 'VPUMP_2_B10[2].6', 'VPUMP_2_B10[2].7', 'VPUMP_2_B10[2].8', 'VPUMP_2_B10[2].9', 'VPUMP_2_B10[2].10', 'VPUMP_2_B10[2].11', 'VPUMP_2_B10[2].12', 'VPUMP_2_B10[2].13', 'VPUMP_2_B10[2].14', 'VPUMP_2_B10[2].15']

pump1_alarm_tag_list = read_alarm_tags_all_pumps(pump1_alarm_tags)


        

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