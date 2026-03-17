from flask import Flask, render_template, request
import calendar
app =Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    cal=""
    if request.method == 'POST':
        year=int(request.form['year'])
        month=int(request.form['month'])
        cal=calendar.month(year, month)
    return render_template('index.html', calendar=cal)
if __name__== "__main__":
    app.run(debug=True)