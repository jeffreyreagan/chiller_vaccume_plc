from flask import Flask, render_template, jsonify
import time
from Reading import read_plc_tag, update_circle_color, read_alarm_tags_all_pumps, update_alarm_tags_all_pumps
from pylogix import PLC
app = Flask(__name__)

    
#tags_to_read = ['tag1', 'tag2', 'tag3']

@app.route('/')
def index():
    return render_template('index2.html')


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


@app.route('/get_circle_color')
def get_circle_color():
    circle_color = update_circle_color()
    return circle_color
    


@app.route('/check_animation_status')
def scheck_animation_status():
    circle_color = update_circle_color()
    if circle_color == 'green':
        # Here you can return some data if needed
        print("blah blah blah")
        return jsonify({'status': 'Animation started'})
    else:
        print('nahhhhhhhhhhhh')
        return jsonify({'status': 'Pump 1 is not running, animation cannot be started'}), 403

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