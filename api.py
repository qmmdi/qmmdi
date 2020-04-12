from flask import Flask, render_template
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
            date = i.split(',')[0]
            deaths = i.split(',')[2]
            if date in hourly_dict:
                if hourly_dict[date] < deaths:
                    hourly_dict[date] = deaths
            else:
                hourly_dict[date] = deaths
    
    for date, deaths in hourly_dict.items():
        dates.append(date)
        max_deaths.append(deaths)
    
    return render_template('california.html', labels = dates, values = max_deaths,
     updated_time = hourly_data[-1].split(',')[1], updated_day = hourly_data[-1].split(',')[0])
                
if __name__ == "__main__":
	app.run()