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
    pumpmasterstatus = update_alarm_tags_all_pumps()
    return jsonify(pumpmasterstatus['pump1status'])
    
@app.route('/get_VACUUM_1_SEPARATOR_PRESSURE_data')
def get_VACUUM_1_SEPARATOR_PRESSURE_data():
    seperator1_psi = read_plc_tag()[1]
    return jsonify({'seperator1_psi': seperator1_psi})

'''pump2'''
@app.route('/get_pump2vacuum_data')
def get_pump2vacuum_data():
    pump2vacuum = read_plc_tag()[2]
    return jsonify(pump2vacuum = pump2vacuum)

@app.route('/get_pump2vacuum_alarm_status')
def get_pump2vacuum_alarm_status():
    pumpmasterstatus = update_alarm_tags_all_pumps()
    return jsonify(pumpmasterstatus['pump2status'])

@app.route('/get_VACUUM_2_SEPARATOR_PRESSURE_data')
def get_VACUUM_2_SEPARATOR_PRESSURE_data():
    seperator2_psi = read_plc_tag()[3]
    return jsonify({'seperator2_psi': seperator2_psi})

'''pump3'''
@app.route('/get_pump3vacuum_data')
def get_pump3vacuum_data():
    pump3vacuum = read_plc_tag()[4]
    return jsonify(pump3vacuum = pump3vacuum)

@app.route('/get_pump3vacuum_alarm_status')
def get_pump3vacuum_alarm_status():
    pumpmasterstatus = update_alarm_tags_all_pumps()
    return jsonify(pumpmasterstatus['pump3status'])

@app.route('/get_VACUUM_3_SEPARATOR_PRESSURE_data')
def get_VACUUM_3_SEPARATOR_PRESSURE_data():
    seperator3_psi = read_plc_tag()[5]
    return jsonify({'seperator3_psi': seperator3_psi})

'''pump4'''
@app.route('/get_pump4vacuum_data')
def get_pump4vacuum_data():
    pump4vacuum = read_plc_tag()[6]
    
    return jsonify(pump4vacuum = pump4vacuum)

@app.route('/get_pump4vacuum_alarm_status')
def get_pump4vacuum_alarm_status():
    pumpmasterstatus = update_alarm_tags_all_pumps()
    return jsonify(pumpmasterstatus['pump4status'])

@app.route('/get_VACUUM_4_SEPARATOR_PRESSURE_data')
def get_VACUUM_4_SEPARATOR_PRESSURE_data():
    seperator4_psi = read_plc_tag()[7]
    return jsonify({'seperator4_psi': seperator4_psi})


'''pump5'''
@app.route('/get_pump5vacuum_data')
def get_pump5vacuum_data():
    pump5vacuum = read_plc_tag()[8]
    return jsonify(pump5vacuum = pump5vacuum)

@app.route('/get_pump5vacuum_alarm_status')
def get_pump5vacuum_alarm_status():
    pumpmasterstatus = update_alarm_tags_all_pumps()
    return jsonify(pumpmasterstatus['pump5status'])

@app.route('/get_VACUUM_5_SEPARATOR_PRESSURE_data')
def get_VACUUM_5_SEPARATOR_PRESSURE_data():
    seperator5_psi = read_plc_tag()[9]
    return jsonify({'seperator5_psi': seperator5_psi})

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
    return jsonify(results)

if __name__ == '__main__':
    plc_ip_address = '172.16.21.12'
    app.run(debug=True)

#The Graveyard
'''@app.route('/get_plc_data')
def get_plc_data():
    data_with_datatypes = plc_comm.read_tags_with_datatypes(tags_to_read)
    formatted_data = [{'name': entry['name'], 'value': entry['value'], 'datatype': entry['datatype']} for entry in data_with_datatypes]
    return jsonify(formatted_data)'''