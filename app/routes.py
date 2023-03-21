from app import app

from flask import render_template

@app.route('/')
def homePage():
    fav_season = 'Summer'
    return render_template('index.html', f = fav_season)

@app.route('/favorite')
def favoritesPage():
    favs = [
        {
        'favorite' : 'SAUNA',
        'style' : 'portable infered heat',
        'duration' : 'daily for 30-50 min'
        },
        {
        'favorite' : 'RED LIGHT THERAPY',
        'style' : 'in the sauna or daily before bed',
        'duration' : 'daily for 30-50 min'
        },
        {
        'favorite' : 'ICE COLD SHOWERS',
        'style' : '2 min cold shower after sauna session',
        'duration' : 'daily'
        },
        {
        'favorite' : 'WALKING',
        'style' : 'listening to podcast/audio book',
        'duration' : 'daily for 1 hour'
        },
        {
        'favorite' : 'MORNING SUNLIGHT',
        'style' : 'first thing everymorning, sunshine in the naked eye',
        'duration' : 'daily for at least 15 min'
        }
    ]
    return render_template('favorite.html', favs=favs)
