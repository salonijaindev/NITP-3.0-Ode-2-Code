from flask import Flask, render_template
from flask import request
import numpy as np
import suppcode1

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fertility',methods=['GET'])
def fertility():
    return render_template("fertility.html")

@app.route('/',methods=['POST'])
def get_data():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    ans = suppcode1.hello(final_features)
    return render_template("result.html", s=ans)

@app.route('/recommend/', methods=['GET','POST'])
def recommend():
    return render_template('recommend.html')

@app.route('/about/', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/cinfo/', methods=['GET','POST'])
def cinfo():
    return render_template('cinfo.html')

@app.route('/soil/', methods=['GET','POST'])
def soil():
    return render_template('soil.html')

@app.route('/irrigation/', methods=['GET','POST'])
def irrigation():
    return render_template('irrigation.html')

@app.route('/fertilizers/', methods=['GET','POST'])
def fertilizers():
    return render_template('fertilizers.html')

@app.route('/crops/', methods=['GET','POST'])
def crops():
    return render_template('crops.html')

if __name__ == "__main__":
    app.run(debug=True)