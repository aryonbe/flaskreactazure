from flask import Flask, render_template
import time

app = Flask(__name__,static_folder='../build',static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/test')
def test():
    return render_template("test.html")
    
#if __name__ == "__main__":
#    app.run(host="0.0.0.0")