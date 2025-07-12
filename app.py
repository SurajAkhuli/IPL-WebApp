# from flask import Flask,render_template,request
# import requests

# app = Flask(__name__)

# @app.route('/')
# def home():
#     response = requests.get('http://127.0.0.1:5000/api/teams')
#     teams = response.json()['teams']
#     return render_template('index.html',teams = sorted(teams))

# @app.route('/teamvteam')
# def team_vs_team():
#     team1 = request.args.get('team1')
#     team2 = request.args.get('team2')

#     response = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
#     response = response.json()

#     response1 = requests.get('http://127.0.0.1:5000/api/teams')
#     teams = response1.json()['teams']

#     return render_template('index.html',result = response,teams = sorted(teams))

# app.run(debug=True,port=7000)




from flask import Flask, render_template, request
import requests
import json
import pandas as pd

app = Flask(__name__)

BASE_URL = 'http://127.0.0.1:5000'

def get_batsmen():
    try:
        response = requests.get(f'{BASE_URL}/api/all-batsmen')
        return response.json().get('batsmen', [])
    except:
        return []

def get_bowlers():
    try:
        response = requests.get(f'{BASE_URL}/api/all-bowlers')
        return response.json().get('bowlers', [])
    except:
        return []


@app.route('/')
def home():
    teams = get_teams()
    batsmen = get_batsmen()
    bowlers = get_bowlers()
    return render_template('index.html', teams=sorted(teams), batsmen=batsmen, bowlers=bowlers)


@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    teams = get_teams()
    batsmen = get_batsmen()
    bowlers = get_bowlers()

    result = requests.get(f'{BASE_URL}/api/teamvteam', params={'team1': team1, 'team2': team2}).json()
    return render_template('index.html', teams=sorted(teams), result=result, batsmen=batsmen, bowlers=bowlers)

@app.route('/team-record')
def team_record():
    team = request.args.get('team')
    teams = get_teams()
    batsmen = get_batsmen()
    bowlers = get_bowlers()

    response = requests.get(f'{BASE_URL}/api/team-record', params={'team': team})
    record = json.dumps(response.json(), indent=4)
    return render_template('index.html', teams=sorted(teams), team_record=record, batsmen=batsmen, bowlers=bowlers)


@app.route('/batting-record')
def batting_record():
    batsman = request.args.get('batsman')
    teams = get_teams()
    batsmen = get_batsmen()
    bowlers = get_bowlers()

    response = requests.get(f'{BASE_URL}/api/batting-record', params={'batsman': batsman})
    record = json.dumps(response.json(), indent=4)
    return render_template('index.html', teams=sorted(teams), batsman_record=record, batsmen=batsmen, bowlers=bowlers)


@app.route('/bowling-record')
def bowling_record():
    bowler = request.args.get('bowler')
    teams = get_teams()
    batsmen = get_batsmen()
    bowlers = get_bowlers()


    response = requests.get(f'{BASE_URL}/api/bowling-record', params={'bowler': bowler})
    record = json.dumps(response.json(), indent=4)
    return render_template('index.html', teams=sorted(teams), bowler_record=record, batsmen=batsmen, bowlers=bowlers)

def get_teams():
    try:
        response = requests.get(f'{BASE_URL}/api/teams')
        return response.json().get('teams', [])
    except:
        return []

app.run(debug=True, port=7000)
