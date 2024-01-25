from flask import Flask, render_template, jsonify
import time
from Reading import read_plc_tag
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

@app.route('/get_pump2vacuum_data')
def get_pump2vacuum_data():
    pump2vacuum = read_plc_tag()[1]
    return jsonify({'pump2vacuum': pump2vacuum})

'''@app.route('/get_plc_data')
def get_plc_data():
    data_with_datatypes = plc_comm.read_tags_with_datatypes(tags_to_read)
    formatted_data = [{'name': entry['name'], 'value': entry['value'], 'datatype': entry['datatype']} for entry in data_with_datatypes]
    return jsonify(formatted_data)'''

if __name__ == '__main__':
    plc_ip_address = '172.16.21.12'
    app.run(debug=True)
