from flask import *
import onoff
import colors
import brightness
import effects

onoff = onoff.onoff()
colors = colors.colors()
brightness = brightness.brightness()
effects = effects.effects()

#Create flask app
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/onoff/on", methods=['POST'])
def on():
    print "LEDs ON"
    onoff.on()
    return ('', 204)

@app.route("/onoff/off", methods=['POST'])
def off():
    print "LEDs OFF"
    onoff.off()
    return ('', 204)

@app.route("/brightness/updown/up", methods=['POST'])
def up():
    print "LEDs UP"
    brightness.up()
    return ('', 204)

@app.route("/brightness/updown/down", methods=['POST'])
def down():
    print "LEDs DOWN"
    brightness.down()
    return ('', 204)

@app.route("/colors/red", methods=['POST'])
def red():
    print "LEDs RED"
    colors.red()
    return ('', 204)

@app.route("/colors/blue", methods=['POST'])
def blue():
    print "LEDs BLUE"
    colors.blue()
    return ('', 204)

@app.route("/colors/green", methods=['POST'])
def green():
    print "LEDs GREEN"
    colors.green()
    return ('', 204)

@app.route("/colors/white", methods=['POST'])
def white():
    print "LEDs WHITE"
    colors.white()
    return ('', 204)

@app.route("/brightness/user/", methods=['POST'])
def userBrightness():
    userBrightness = int(request.args.get('B'))
    print 'LEDs USER BRIGHTNESS : [{0}]'.format(userBrightness)
    brightness.user(userBrightness)
    return ('', 204)

@app.route("/colors/user/", methods=['POST'])
def color():
    blue = int(request.args.get('B'))
    red = int(request.args.get('R'))
    green = int(request.args.get('G'))
    print 'LEDs USER COLORS. RED : [{0}] GREEN : [{1}] BLUE : [{2}]'.format(red, green, blue)
    colors.user(blue, red, green)
    return ('', 204)

@app.route("/effects/smooth", methods=['POST'])
def smooth():
    print 'LEDs SMOOTH'
    effects.smooth()
    return ('', 204)

@app.route("/effects/fade", methods=['POST'])
def fade():
    print 'LEDs FADE'
    effects.fade()
    return ('', 204)

@app.route("/effects/strobe", methods=['POST'])
def strobe():
    print 'LEDs STROBE'
    effects.strobe()
    return ('', 204)

@app.route("/effects/flash", methods=['POST'])
def flash():
    print 'LEDs Flash'
    effects.flashcolors()
    return ('', 204)

@app.route("/js/index.js", methods=['GET'])
def js():
    return  send_from_directory('templates/js/', 'index.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
