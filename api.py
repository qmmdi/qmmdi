from flask import Flask, render_template, request, redirect, url_for
from datetime import date, datetime
import constants
import csv

app = Flask(__name__)


@app.route('/')
def california():
    hourly_data = []
    hourly_dict = {}
    dates = []
    max_deaths = []

    with open(constants.HOME_PATH) as csv_file:
        csv_file = csv.reader(csv_file, delimiter=',')

        for row in csv_file:
            hourly_data.append(','.join(row))
        
        for i in hourly_data:
            deaths = i.split(',')[2]
            date = i.split(',')[0][5:]
            
            if date[0] == '0':
                date = date[1:]

            if date in hourly_dict:
                if hourly_dict[date] < deaths:
                    hourly_dict[date] = deaths
            else:
                hourly_dict[date] = deaths
    
    for date, deaths in hourly_dict.items():
        dates.append(date)
        max_deaths.append(deaths)
    
    print(hourly_dict)
    return render_template('california.html', labels = dates, values = max_deaths,
     updated_time = hourly_data[-1].split(',')[1], updated_day = hourly_data[-1].split(',')[0])


@app.route('/timer', methods =['POST', 'GET'])
def timer():
    if request.method == 'POST':
        try:
            start = request.form['start']
            day = start[3:5]
            month = start[0:2]
            year = start[6:]
            start = date(int(year), int(month), int(day))
            today = date.today()
            if start > today:
                return redirect(url_for('california'))
            delta = today - start
            return render_template('days.html', days = delta.days)
        except ValueError:
            return redirect(url_for('california'))

    return render_template('days.html')



if __name__ == "__main__":
	app.run()
