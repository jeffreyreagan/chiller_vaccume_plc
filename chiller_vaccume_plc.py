from flask import Flask, render_template, jsonify
import time
from Reading import read_plc_tag, update_circle_color, update_alarm_tags_all_pumps
from pylogix import PLC
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chiller_vacuum_ui.html')

'''pump 1'''
@app.route('/get_pump1vacuum_data')
def get_pump1vacuum_data():
    pump1vacuum = read_plc_tag()[0]
    return jsonify({'pump1vacuum': pump1vacuum})

@app.route('/get_pump1vacuum_alarm_status')
def get_pump1vacuum_alarm_status():
    pump1alarmstatus, pump1_active_alarms = update_alarm_tags_all_pumps()
    return jsonify({'pump1alarmstatus': pump1alarmstatus,'pump1_active_alarms':pump1_active_alarms})
    
@app.route('/get_VACUUM_1_SEPARATOR_PRESSURE_data')
def get_VACUUM_1_SEPARATOR_PRESSURE_data():
    seperator1_psi = read_plc_tag()[2]
    return jsonify({'seperator1_psi': seperator1_psi})

'''Utilities'''
@app.route('/get_circle_color')
def get_circle_color():
    circle_colors_tuple = update_circle_color()
    circle_colors = circle_colors_tuple[0]
    return jsonify(circle_colors)

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
    return jsonify(results)

@app.route('/get_pump2vacuum_data')
def get_pump2vacuum_data():
    pump2vacuum = read_plc_tag()[1]
    return jsonify(pump2vacuum = pump2vacuum)

if __name__ == '__main__':
    plc_ip_address = '172.16.21.12'
    app.run(debug=True)

#The Graveyard
'''@app.route('/get_plc_data')
def get_plc_data():
    data_with_datatypes = plc_comm.read_tags_with_datatypes(tags_to_read)
    formatted_data = [{'name': entry['name'], 'value': entry['value'], 'datatype': entry['datatype']} for entry in data_with_datatypes]
    return jsonify(formatted_data)'''