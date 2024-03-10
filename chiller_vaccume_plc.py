from flask import Flask, render_template, jsonify
import time
from Reading import read_plc_tag, update_circle_color, update_alarm_tags_all_pumps
from pylogix import PLC
app = Flask(__name__)

from flask import Flask, render_template, jsonify
import time
import random

app = Flask(__name__)

def simulate_plc_data():
    # Simulate pump vacuum data
   
    pump_vacuum_data = [random.randint(0, 100) for _ in range(5)]
    
    # Simulate alarm status
    alarm_statuses = [random.choice([True, False]) for _ in range(5)]
    
    # Simulate separator pressure data
    separator_pressure_data = [random.uniform(0, 10) for _ in range(5)]
    
    return pump_vacuum_data, alarm_statuses, separator_pressure_data

@app.route('/')
def index():
    return render_template('chiller_vacuum_ui.html')

# Routes for pump 1
@app.route('/get_pump1vacuum_data')
def get_pump1vacuum_data():
    
    pump_vacuum_data, _, _ = simulate_plc_data()
    return jsonify({'pump1vacuum': pump_vacuum_data[0]})

@app.route('/get_pump1vacuum_alarm_status')
def get_pump1vacuum_alarm_status():
   
    _, alarm_statuses, _ = simulate_plc_data()
    return jsonify({'alarm_status': alarm_statuses[0]})

@app.route('/get_VACUUM_1_SEPARATOR_PRESSURE_data')
def get_VACUUM_1_SEPARATOR_PRESSURE_data():
  
    _, _, separator_pressure_data = simulate_plc_data()
    return jsonify({'seperator1_psi': separator_pressure_data[0]})

# Routes for pump 2
@app.route('/get_pump2vacuum_data')
def get_pump2vacuum_data():
   
    pump_vacuum_data, _, _ = simulate_plc_data()
    return jsonify({'pump2vacuum': pump_vacuum_data[1]})

@app.route('/get_pump2vacuum_alarm_status')
def get_pump2vacuum_alarm_status():
  
    _, alarm_statuses, _ = simulate_plc_data()
    return jsonify({'alarm_status': alarm_statuses[1]})

@app.route('/get_VACUUM_2_SEPARATOR_PRESSURE_data')
def get_VACUUM_2_SEPARATOR_PRESSURE_data():
   
    _, _, separator_pressure_data = simulate_plc_data()
    return jsonify({'seperator2_psi': separator_pressure_data[1]})

# Routes for pump 3 (similar structure as pump 2)

# Routes for pump 4 (similar structure as pump 2)

# Routes for pump 5 (similar structure as pump 2)


'''Utilities'''
@app.route('/get_circle_color')
def get_circle_color():
    circle_colors_tuple = update_circle_color()
    circle_colors = circle_colors_tuple[0]
    

@app.route('/check_animation_status')
def check_animation_status():
   
    results = []
    circle_colors_tuple = update_circle_color()
    circle_colors = circle_colors_tuple[0]
    if circle_colors['pump1color'] == 'green':
        print("updating pump 1 status to green")
        results.append({'status': 'Animation 1 started'})
    elif circle_colors['pump1color'] != 'green':
        results.append({'status': 'Animation 1 stopped'})
        print("updating pump 1 status to red")
    if circle_colors['pump2color'] == 'green':
        results.append({'status': 'Animation 2 started'})
        print("updating pump 2 status to green")
    elif circle_colors['pump2color'] != 'green':
        results.append({'status': 'Animation 2 stopped'})
        print("updating pump 2 status to red")
    if circle_colors['pump3color'] == 'green':
        print("updating pump 3 status to green")
        results.append({'status': 'Animation 3 started'})
    elif circle_colors['pump3color'] != 'green':
        results.append({'status': 'Animation 3 stopped'})
        print("updating pump 3 status to red")
    if circle_colors['pump4color'] == 'green':
        results.append({'status': 'Animation 4 started'})
        print("updating pump 4 status to green")
    elif circle_colors['pump4color'] != 'green':
        results.append({'status': 'Animation 4 stopped'})
        print("updating pump 4 status to red") 
    if circle_colors['pump5color'] == 'green':
        results.append({'status': 'Animation 5 started'})
        print("updating pump 5 status to green")
    elif circle_colors['pump5color'] != 'green':
        results.append({'status': 'Animation 5 stopped'})
        print("updating pump 5 status to red")   
    return jsonify(results, circle_colors)
if __name__ == '__main__':
    plc_ip_address = '172.16.21.12'
    app.run(debug=True)

#The Graveyard
'''@app.route('/get_plc_data')
def get_plc_data():
    data_with_datatypes = plc_comm.read_tags_with_datatypes(tags_to_read)
    formatted_data = [{'name': entry['name'], 'value': entry['value'], 'datatype': entry['datatype']} for entry in data_with_datatypes]
    return jsonify(formatted_data)'''


'''add lead lag states to text,
display state as yellow when not alarmed but pump stopped,
only display red as alarmed,
configure pump inlet valves,
make exceptions for fail to connect to plc,
add ui for failure to connect
COMMENT,,VPUMP_1_N13,"Pump 1 Lead/Lag Status | 0=Lead, 1=Lag1, 2=Lag2",,"VPUMP_1_N13[21]"
COMMENT,,VPUMP_1_B10,"Pump Inlet Valve Temp Control Latch (ON to Enable Open)",,"VPUMP_1_B10[3].0"
COMMENT,,VPUMP_1_B10,"Pump Inlet Valve Vac Control Latch (ON to Enable Open)",,"VPUMP_1_B10[3].1"
COMMENT,,VPUMP_1_B10,"Pump Inlet Valve Sep Back PSI Control Latch (ON to Enable Open)",,"VPUMP_1_B10[3].2"
'''