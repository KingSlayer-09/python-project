from flask import Flask, render_template
from workouts import workouts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', workouts=workouts)

@app.route('/workout/<name>')
def workout_detail(name):
    workout = next((w for w in workouts if w["name"].lower() == name.lower()), None)
    return render_template('workout.html', workout=workout)

if __name__ == '__main__':
    app.run(debug=True)
