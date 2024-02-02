from pylogix import PLC
import time
# Function to read the PLC tags for vacuum and seperator pressure and return the values in a readable format
def read_plc_tag():
        try:
            with PLC() as comm:
                comm.IPAddress = '172.16.21.12' 
                comm.ProcessorSlot = 0  
                tags = ['VACUUM_1_VACUUM','VACUUM_2_VACUUM','VACUUM_1_SEPARATOR_PRESSURE']
                pump1vacuum = None
                pump2vacuum = None
                seperator1_psi = None
                results = comm.Read(tags)
                print(results)
                for result in results:
                    if result.Status == 'Success':
                        if result.TagName == 'VACUUM_1_VACUUM':
                            result.Value *= 0.1
                            pump1vacuum_formatted = "{:.2f}".format(result.Value)
                            pump1vacuum = str(pump1vacuum_formatted) + " Hg"
                        elif result.TagName == 'VACUUM_2_VACUUM':
                            result.Value *= 0.1
                            pump2vacuum_formatted = "{:.2f}".format(result.Value)
                            pump2vacuum = str(pump2vacuum_formatted) + " Hg"
                        elif result.TagName == 'VACUUM_1_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator1_psi_formatted = "{:.2f}".format(result.Value)
                            seperator1_psi = str(seperator1_psi_formatted) + " PSI"
                return pump1vacuum, pump2vacuum, seperator1_psi
        except Exception as e:
                    print(f"An error occurred: {e}")

def read_alarm_tags_all_pumps(tag_names):
    try:
        with PLC() as comm:
            comm.IPAddress = '172.16.21.12'  # Replace with your PLC's IP address
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
def update_alarm_tags_all_pumps():
    pump1_alarm_tags = ['VPUMP_1_B10[2].0', 'VPUMP_1_B10[2].1', 'VPUMP_1_B10[2].2', 'VPUMP_1_B10[2].3', 'VPUMP_1_B10[2].4', 'VPUMP_1_B10[2].5', 'VPUMP_1_B10[2].6', 'VPUMP_1_B10[2].7', 'VPUMP_1_B10[2].8', 'VPUMP_1_B10[2].9', 'VPUMP_1_B10[2].10', 'VPUMP_1_B10[2].11', 'VPUMP_1_B10[2].12', 'VPUMP_1_B10[2].13', 'VPUMP_1_B10[2].14', 'VPUMP_1_B10[2].15']
    pump2_alarm_tags= ['VPUMP_2_B10[2].0', 'VPUMP_2_B10[2].1', 'VPUMP_2_B10[2].2', 'VPUMP_2_B10[2].3', 'VPUMP_2_B10[2].4', 'VPUMP_2_B10[2].5', 'VPUMP_2_B10[2].6', 'VPUMP_2_B10[2].7', 'VPUMP_2_B10[2].8', 'VPUMP_2_B10[2].9', 'VPUMP_2_B10[2].10', 'VPUMP_2_B10[2].11', 'VPUMP_2_B10[2].12', 'VPUMP_2_B10[2].13', 'VPUMP_2_B10[2].14', 'VPUMP_2_B10[2].15']
    pump1_alarm_comments={'VPUMP_1_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_1_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_1_B10[2].10':'test alarm active!'}
    pump1_alarm_tag_list = read_alarm_tags_all_pumps(pump1_alarm_tags)
    pump1_active_alarms = [pump1_alarm_comments[tag] for tag, value in pump1_alarm_tag_list.items() if value == 1]
    pump2_alarm_tag_list = read_alarm_tags_all_pumps(pump2_alarm_tags)
    '''print(pump2_alarm_tag_list, pump1_alarm_tag_list)'''
    if any(value == 1 for value in pump1_alarm_tag_list.values()):
        print(pump1_active_alarms)
        print("ALARM ACTIVE")
        pump1alarmstatus = True 
    elif all(value == 0 for value in pump1_alarm_tag_list.values()):
        print("No alarm active")
        pump1alarmstatus = False

    else: 
         print("Error connecting to PLC to be specific the alarm tags have not been fetched successfully")
         pump1alarmstatus = None
    return pump1alarmstatus, pump1_active_alarms


def update_circle_color():
    circle_colors = {'pump1color': '','pump2color': ''}  # Initialize colors
    try:
        with PLC() as comm:
            comm.IPAddress = '172.16.21.12' 
            comm.ProcessorSlot = 0  
            tags = ['VACUUM_1_STATUS','VACUUM_2_STATUS']
            results = comm.Read(tags)
            for result in results:
                if result.Status == 'Success':
                    if result.TagName == 'VACUUM_1_STATUS':
                        pump_1_status_value = result.Value
                        print(result.Value)
                        if pump_1_status_value == 3:
                            circle_colors['pump1color'] = 'green'
                            
                        elif pump_1_status_value == 2:
                            circle_colors['pump1color'] = 'red'
                    if result.TagName == 'VACUUM_2_STATUS':
                        pump_2_status_value = result.Value
                        if pump_2_status_value == 3:
                            circle_colors['pump2color'] = 'green'
                        elif pump_2_status_value == 2:
                            circle_colors['pump2color'] = 'red'
                else:
                    print(f"Failed to read tag '{result.TagName}'")
            time.sleep(1)
            print("returning pump colors")
            return circle_colors , pump_1_status_value, pump_2_status_value
              # Return colors after loop
    except Exception as e:
        print(f"An error occurred: {e}")
    
    



if __name__ == "__main__":
    plc_ip_address = "172.16.21.12"

# Function to read the tag and update SVG circle color





#The Graveyard
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

'''for alarms in pump1_alarm_tag_list:
    if pump1_alarm_tag_list.values == 1:
         print("ALARM ACTIVE")
         failed attempt!'''