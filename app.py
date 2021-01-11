from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "hello flask" #app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/test')
def test():
    return render_template("test.html")
    
#if __name__ == "__main__":
#    app.run(host="0.0.0.0")