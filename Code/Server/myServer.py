#flask run --app myServer run --host=0.0.0.0 
#flask run --app myServer run

from flask import Flask
from flask import render_template, make_response
from flask import redirect, request, jsonify, url_for
import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False) #
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)#
GPIO.setup(Buzzer_Pin,GPIO.OUT)#

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")
@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        content = request.form
        bState = True if content['buzzer'] == "0" else False
        if bState:#
            GPIO.output(Buzzer_Pin,GPIO.HIGH)#
        else:#
            GPIO.output(Buzzer_Pin,GPIO.LOW)#
        #GPIO.output(Buzzer_Pin, bState)
        return ""
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='192.168.137.106', port=5050, debug=True, use_reloader=False, threaded=False)
