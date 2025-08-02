from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/userdata', methods=['GET', 'POST'])
def userdata():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        education = request.form['education']
        skills = request.form['skills']
        message = request.form['message']

        print("Received Bio Data:")
        print(name, dob, address, phone, email, education, skills, message)

        flash("✅ Bio data submitted successfully!")
        return redirect('/userdata')

    return render_template('userdata.html')

if __name__ == "__main__":
    app.run(debug=True)
