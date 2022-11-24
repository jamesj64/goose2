#flask run --app myServer run --host=0.0.0.0 
#flask run --app myServer run

from flask import Flask
from flask import render_template, make_response
from flask import redirect, request, jsonify, url_for
#import RPi.GPIO as GPIO
import os

Buzzer_Pin = 17

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")
@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        content = request.form
        print(content['buzzer'])
        bState = True if content['buzzer'] else False
        #GPIO.output(Buzzer_Pin, bState)
        return ""
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)