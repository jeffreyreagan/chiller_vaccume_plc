from pylogix import PLC
import time
# Function to read the PLC tags for vacuum and seperator pressure and return the values in a readable format

print("Does this print once?")

def read_plc_tag():
        try:
            with PLC() as comm:
                comm.IPAddress = '172.16.21.12' 
                comm.ProcessorSlot = 0  
                tags = ['VACUUM_1_VACUUM','VACUUM_1_SEPARATOR_PRESSURE','VACUUM_2_VACUUM','VACUUM_2_SEPARATOR_PRESSURE','VACUUM_3_VACUUM','VACUUM_3_SEPARATOR_PRESSURE','VACUUM_4_VACUUM','VACUUM_4_SEPARATOR_PRESSURE','VACUUM_5_VACUUM','VACUUM_5_SEPARATOR_PRESSURE']
                pump1vacuum = None
                pump2vacuum = None
                pump3vacuum = None
                pump4vacuum = None
                pump5vacuum = None
                seperator1_psi = None
                seperator2_psi = None
                seperator3_psi = None
                seperator4_psi = None
                seperator5_psi = None
                time.sleep(1)
                results = comm.Read(tags)
                for result in results:
                    if result.Status == 'Success':
                        if result.TagName == 'VACUUM_1_VACUUM':
                            result.Value *= 0.1
                            pump1vacuum_formatted = "{:.2f}".format(result.Value)
                            pump1vacuum = str(pump1vacuum_formatted) + " Hg"
                        if result.TagName == 'VACUUM_1_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator1_psi_formatted = "{:.2f}".format(result.Value)
                            seperator1_psi = str(seperator1_psi_formatted) + " PSI"
                        if result.TagName == 'VACUUM_2_VACUUM':
                            result.Value *= 0.1
                            pump2vacuum_formatted = "{:.2f}".format(result.Value)
                            pump2vacuum = str(pump2vacuum_formatted) + " Hg"
                        if result.TagName == 'VACUUM_2_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator2_psi_formatted = "{:.2f}".format(result.Value)
                            seperator2_psi = str(seperator2_psi_formatted) + " PSI"
                        if result.TagName == 'VACUUM_3_VACUUM':
                            result.Value *= 0.1
                            pump3vacuum_formatted = "{:.2f}".format(result.Value)
                            pump3vacuum = str(pump3vacuum_formatted) + " Hg"
                        if result.TagName == 'VACUUM_3_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator3_psi_formatted = "{:.2f}".format(result.Value)
                            seperator3_psi = str(seperator3_psi_formatted) + " PSI"
                        if result.TagName == 'VACUUM_4_VACUUM':
                            result.Value *= 0.1
                            pump4vacuum_formatted = "{:.2f}".format(result.Value)
                            pump4vacuum = str(pump4vacuum_formatted) + " Hg"
                        if result.TagName == 'VACUUM_4_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator4_psi_formatted = "{:.2f}".format(result.Value)
                            seperator4_psi = str(seperator4_psi_formatted) + " PSI"
                        if result.TagName == 'VACUUM_5_VACUUM':
                            result.Value *= 0.1
                            pump5vacuum_formatted = "{:.2f}".format(result.Value)
                            pump5vacuum = str(pump5vacuum_formatted) + " Hg"
                        if result.TagName == 'VACUUM_5_SEPARATOR_PRESSURE':
                            result.Value *= 0.1
                            seperator5_psi_formatted = "{:.2f}".format(result.Value)
                            seperator5_psi = str(seperator5_psi_formatted) + " PSI"
                        
                return pump1vacuum, seperator1_psi, pump2vacuum, seperator2_psi, pump3vacuum, seperator3_psi, pump4vacuum, seperator4_psi, pump5vacuum, seperator5_psi
        except Exception as e:
                    print(f"An error occurred: {e}")
import random

def read_alarm_tags_all_pumps(tag_names):
    try:
        # Simulate reading tag values
        tag_values = {tag: random.choice([0, 1]) for tag in tag_names}
        return tag_values
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_alarm_tags_all_pumps():
    pump1_alarm_tags = ['VPUMP_1_B10[2].{}'.format(i) for i in range(16)]
    pump2_alarm_tags = ['VPUMP_2_B10[2].{}'.format(i) for i in range(16)]
    pump3_alarm_tags = ['VPUMP_3_B10[2].{}'.format(i) for i in range(16)]
    pump4_alarm_tags = ['VPUMP_4_B10[2].{}'.format(i) for i in range(16)]
    pump5_alarm_tags = ['VPUMP_5_B10[2].{}'.format(i) for i in range(16)]
    
    # Simulate reading alarm tags for all pumps
    pump1_alarm_tag_list = read_alarm_tags_all_pumps(pump1_alarm_tags)
    pump2_alarm_tag_list = read_alarm_tags_all_pumps(pump2_alarm_tags)
    pump3_alarm_tag_list = read_alarm_tags_all_pumps(pump3_alarm_tags)
    pump4_alarm_tag_list = read_alarm_tags_all_pumps(pump4_alarm_tags)
    pump5_alarm_tag_list = read_alarm_tags_all_pumps(pump5_alarm_tags)

    # Simulate determining active alarms for each pump
    pump1_active_alarms = [tag for tag, value in pump1_alarm_tag_list.items() if value == 1]
    pump2_active_alarms = [tag for tag, value in pump2_alarm_tag_list.items() if value == 1]
    pump3_active_alarms = [tag for tag, value in pump3_alarm_tag_list.items() if value == 1]
    pump4_active_alarms = [tag for tag, value in pump4_alarm_tag_list.items() if value == 1]
    pump5_active_alarms = [tag for tag, value in pump5_alarm_tag_list.items() if value == 1]

    # Simulate determining alarm status for each pump
    pump1_alarm_status = bool(pump1_active_alarms)
    pump2_alarm_status = bool(pump2_active_alarms)
    pump3_alarm_status = bool(pump3_active_alarms)
    pump4_alarm_status = bool(pump4_active_alarms)
    pump5_alarm_status = bool(pump5_active_alarms)

    # Construct pump master status dictionary
    pumpmasterstatus = {
        'pump1status': {'alarm_status': pump1_alarm_status, 'active_alarms': pump1_active_alarms},
        'pump2status': {'alarm_status': pump2_alarm_status, 'active_alarms': pump2_active_alarms},
        'pump3status': {'alarm_status': pump3_alarm_status, 'active_alarms': pump3_active_alarms},
        'pump4status': {'alarm_status': pump4_alarm_status, 'active_alarms': pump4_active_alarms},
        'pump5status': {'alarm_status': pump5_alarm_status, 'active_alarms': pump5_active_alarms}
    }
    
    return pumpmasterstatus

# Example usage
simulated_data = update_alarm_tags_all_pumps()
print(simulated_data)

import random
import time

def update_circle_color():
    circle_colors = {'pump1color': '', 'pump2color': '', 'pump3color': '', 'pump4color': '', 'pump5color': ''}  # Initialize colors
   
    try:
        time.sleep(5)
        # Simulate reading tag values
        pump_1_status_value = random.randint(2, 3)
        pump_2_status_value = random.randint(2, 3)
        pump_3_status_value = random.randint(2, 3)
        pump_4_status_value = random.randint(2, 3)
        pump_5_status_value = random.randint(2, 3)
        
        # Update circle colors based on simulated tag values
        if pump_1_status_value == 3:
            circle_colors['pump1color'] = 'green'              
        elif pump_1_status_value == 2:
            circle_colors['pump1color'] = 'red'
            
        if pump_2_status_value == 3:
            circle_colors['pump2color'] = 'green'
        elif pump_2_status_value == 2:
            circle_colors['pump2color'] = 'red'
            
        if pump_3_status_value == 3:
            circle_colors['pump3color'] = 'green'
        elif pump_3_status_value == 2:
            circle_colors['pump3color'] = 'red'
            
        if pump_4_status_value == 3:
            circle_colors['pump4color'] = 'green'
        elif pump_4_status_value == 2:
            circle_colors['pump4color'] = 'red'
            
        if pump_5_status_value == 3:
            circle_colors['pump5color'] = 'green'
        elif pump_5_status_value == 2:
            circle_colors['pump5color'] = 'red'
            
        time.sleep(1)
        print("Returning pump statuses")
        return circle_colors, pump_1_status_value, pump_2_status_value, pump_3_status_value, pump_4_status_value, pump_5_status_value
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


    plc_ip_address = "172.16.21.12"

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