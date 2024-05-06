from flask import Flask,render_template
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/video')
def blog():
    return render_template('video.html')
 
app.run(host='0.0.0.0', port=5000)