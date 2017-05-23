from flask import *
from pyA20.gpio import gpio
from pyA20.gpio import port

#Create flask app
app = Flask(__name__, template_folder='templates')

#initialize the gpio module
gpio.init()

#set gpio pin
LED=port.PA14
 
gpio.setcfg(LED,gpio.OUTPUT)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/onoff/on", methods=['POST'])
def on():
    print "LEDs ON"
    gpio.output(LED,gpio.LOW)
    return ('', 204)

@app.route("/onoff/off", methods=['POST'])
def off():
    print "LEDs OFF"
    gpio.output(LED,gpio.HIGH)
    return ('', 204)

@app.route("/js/index.js", methods=['GET'])
def js():
    return  send_from_directory('templates/js/', 'index.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
