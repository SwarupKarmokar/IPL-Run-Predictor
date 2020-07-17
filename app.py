from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
linear_model = pickle.load(open("ipl_run_predictor.pkl", 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        venue = request.form['venue']
        if venue == "venue_Eden Gardens":
            temp_array == temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "venue_Feroz Shah Kotla":
            temp_array == temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "venue_Holkar Cricket Stadium":
            temp_array == temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif venue == "venue_M Chinnaswamy Stadium":
            temp_array == temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif venue == "venue_MA Chidambaram Stadium, Chepauk":
            temp_array == temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif venue == "venue_Maharashtra Cricket Association Stadium":
            temp_array == temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif venue == "venue_Rajiv Gandhi International Stadium, Uppal":
            temp_array == temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif venue == "venue_Sawai Mansingh Stadium":
            temp_array == temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif venue == "venue_Wankhede Stadium":
            temp_array == temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1]

        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

        data = np.array([temp_array])
        my_prediction = int(linear_model.predict(data)[0])
        return render_template('index.html', prediction_text='Projected Score Will Be: {} Lakhs'.format(my_prediction))


if __name__ == '__main__':
    app.run(debug=True)