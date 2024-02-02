from pylogix import PLC
import time
# Function to read the PLC tags for vacuum and seperator pressure and return the values in a readable format
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
                results = comm.Read(tags)
                print(results)
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
                        
                return pump1vacuum, pump2vacuum, pump3vacuum, pump4vacuum, pump5vacuum, seperator1_psi, seperator2_psi, seperator3_psi, seperator4_psi, seperator5_psi
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
    pump3_alarm_tags= ['VPUMP_3_B10[2].0', 'VPUMP_3_B10[2].1', 'VPUMP_3_B10[2].2', 'VPUMP_3_B10[2].3', 'VPUMP_3_B10[2].4', 'VPUMP_3_B10[2].5', 'VPUMP_3_B10[2].6', 'VPUMP_3_B10[2].7', 'VPUMP_3_B10[2].8', 'VPUMP_3_B10[2].9', 'VPUMP_3_B10[2].10', 'VPUMP_3_B10[2].11', 'VPUMP_3_B10[2].12', 'VPUMP_3_B10[2].13', 'VPUMP_3_B10[2].14', 'VPUMP_3_B10[2].15']
    pump4_alarm_tags= ['VPUMP_4_B10[2].0', 'VPUMP_4_B10[2].1', 'VPUMP_4_B10[2].2', 'VPUMP_4_B10[2].3', 'VPUMP_4_B10[2].4', 'VPUMP_4_B10[2].5', 'VPUMP_4_B10[2].6', 'VPUMP_4_B10[2].7', 'VPUMP_4_B10[2].8', 'VPUMP_4_B10[2].9', 'VPUMP_4_B10[2].10', 'VPUMP_4_B10[2].11', 'VPUMP_4_B10[2].12', 'VPUMP_4_B10[2].13', 'VPUMP_4_B10[2].14', 'VPUMP_4_B10[2].15']
    pump5_alarm_tags= ['VPUMP_5_B10[2].0', 'VPUMP_5_B10[2].1', 'VPUMP_5_B10[2].2', 'VPUMP_5_B10[2].3', 'VPUMP_5_B10[2].4', 'VPUMP_5_B10[2].5', 'VPUMP_5_B10[2].6', 'VPUMP_5_B10[2].7', 'VPUMP_5_B10[2].8', 'VPUMP_5_B10[2].9', 'VPUMP_5_B10[2].10', 'VPUMP_5_B10[2].11', 'VPUMP_5_B10[2].12', 'VPUMP_5_B10[2].13', 'VPUMP_5_B10[2].14', 'VPUMP_5_B10[2].15']
    pump1_alarm_comments={'VPUMP_1_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_1_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_1_B10[2].10':'test alarm active!'}
    pump2_alarm_comments={'VPUMP_2_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_2_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_2_B10[2].10':'test alarm active!'}
    pump3_alarm_comments={'VPUMP_3_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_3_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_3_B10[2].10':'test alarm active!'}
    pump4_alarm_comments={'VPUMP_4_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_4_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_4_B10[2].10':'test alarm active!'}
    pump5_alarm_comments={'VPUMP_5_B10[2].0':'Vacuum Xmtr Signal Failure Fault Latch','VPUMP_5_B10[2].1':'PSI Xmtr Signal Failure Fault Latch','VPUMP_5_B10[2].10':'test alarm active!'}
    
    pump1_alarm_tag_list = read_alarm_tags_all_pumps(pump1_alarm_tags)
    pump2_alarm_tag_list = read_alarm_tags_all_pumps(pump2_alarm_tags)
    pump3_alarm_tag_list = read_alarm_tags_all_pumps(pump3_alarm_tags)
    pump4_alarm_tag_list = read_alarm_tags_all_pumps(pump4_alarm_tags)
    pump5_alarm_tag_list = read_alarm_tags_all_pumps(pump5_alarm_tags)

    pump1_active_alarms = [pump1_alarm_comments[tag] for tag, value in pump1_alarm_tag_list.items() if value == 1]
    pump2_active_alarms = [pump2_alarm_comments[tag] for tag, value in pump2_alarm_tag_list.items() if value == 1]
    pump3_active_alarms = [pump3_alarm_comments[tag] for tag, value in pump3_alarm_tag_list.items() if value == 1]
    pump4_active_alarms = [pump4_alarm_comments[tag] for tag, value in pump4_alarm_tag_list.items() if value == 1]
    pump5_active_alarms = [pump5_alarm_comments[tag] for tag, value in pump5_alarm_tag_list.items() if value == 1]

    if any(value == 1 for value in pump1_alarm_tag_list.values()):
        print(pump1_active_alarms)
        print("ALARM ACTIVE")
        pump1alarmstatus = True 
    elif all(value == 0 for value in pump1_alarm_tag_list.values()):
        print("No alarm active")
        pump1alarmstatus = False
    if any(value == 1 for value in pump2_alarm_tag_list.values()):
        print(pump2_active_alarms)
        print("ALARM ACTIVE")
        pump2alarmstatus = True 
    elif all(value == 0 for value in pump2_alarm_tag_list.values()):
        print("No alarm active")
        pump2alarmstatus = False
    if any(value == 1 for value in pump3_alarm_tag_list.values()):
        print(pump3_active_alarms)
        print("ALARM ACTIVE")
        pump3alarmstatus = True 
    elif all(value == 0 for value in pump3_alarm_tag_list.values()):
        print("No alarm active")
        pump3alarmstatus = False
    if any(value == 1 for value in pump4_alarm_tag_list.values()):
        print(pump4_active_alarms)
        print("ALARM ACTIVE")
        pump4alarmstatus = True 
    elif all(value == 0 for value in pump4_alarm_tag_list.values()):
        print("No alarm active")
        pump4alarmstatus = False
    if any(value == 1 for value in pump5_alarm_tag_list.values()):
        print(pump5_active_alarms)
        print("ALARM ACTIVE")
        pump5alarmstatus = True 
    elif all(value == 0 for value in pump5_alarm_tag_list.values()):
        print("No alarm active")
        pump5alarmstatus = False
    else: 
         print("Error connecting to PLC, to be specific the alarm tags have not been fetched successfully")
         pump1alarmstatus = None
    pumpmasterstatus={
    'pump1status':{'alarm_status': pump1alarmstatus, 'active_alarms': pump1_active_alarms},
    'pump2status':{'alarm_status': pump2alarmstatus, 'active_alarms': pump2_active_alarms},
    'pump3status':{'alarm_status': pump3alarmstatus, 'active_alarms': pump3_active_alarms},
    'pump4status':{'alarm_status': pump4alarmstatus, 'active_alarms': pump4_active_alarms},
    'pump5status':{'alarm_status': pump5alarmstatus, 'active_alarms': pump5_active_alarms},
    }
    return pumpmasterstatus

def update_circle_color():
    circle_colors = {'pump1color': '','pump2color': '', 'pump3color': '','pump4color': '', 'pump5color': ''}  # Initialize colors
    try:
        with PLC() as comm:
            comm.IPAddress = '172.16.21.12' 
            comm.ProcessorSlot = 0  
            tags = ['VACUUM_1_STATUS','VACUUM_2_STATUS', 'VACUUM_3_STATUS','VACUUM_4_STATUS', 'VACUUM_5_STATUS']
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
                    if result.TagName == 'VACUUM_3_STATUS':
                        pump_3_status_value = result.Value
                        if pump_3_status_value == 3:
                            circle_colors['pump3color'] = 'green'
                        elif pump_3_status_value == 2:
                            circle_colors['pump3color'] = 'red'
                    if result.TagName == 'VACUUM_4_STATUS':
                        pump_4_status_value = result.Value
                        if pump_4_status_value == 3:
                            circle_colors['pump4color'] = 'green'
                        elif pump_4_status_value == 2:
                            circle_colors['pump4color'] = 'red'
                    if result.TagName == 'VACUUM_5_STATUS':
                        pump_5_status_value = result.Value
                        if pump_5_status_value == 3:
                            circle_colors['pump5color'] = 'green'
                        elif pump_5_status_value == 2:
                            circle_colors['pump5color'] = 'red'
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