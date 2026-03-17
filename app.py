from flask import Flask, render_template, request
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    cal = ""
    error = ""

    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            month = int(request.form['month'])

            if year < 1:
                error = "Enter a valid year"
            else:
                cal = calendar.month(year, month)

                # Highlight today's date
                today = datetime.today()
                if year == today.year and month == today.month:
                    day = str(today.day)
                    cal = cal.replace(f" {day} ", f"[{day}]")

        except ValueError:
            error = "Something went wrong. Please enter valid input."

    return render_template('index.html', calendar=cal, error=error)

if __name__ == "__main__":
    app.run(debug=True)