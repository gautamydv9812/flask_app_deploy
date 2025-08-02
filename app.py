from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/userdata')
def userdata():
    return render_template('userdata.html')

if __name__ == "__main__":
    app.run(debug=True)
