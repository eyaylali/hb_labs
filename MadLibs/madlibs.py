from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def index():
    return render_template("hello.html")

# route to begin playing game
@app.route('/game')
def show_game_form():
    user_choice = request.args.get("choice")
    if user_choice == "no":
        return redirect('/goodbye')
    else:
        return render_template("game.html", choice = user_choice)

@app.route('/goodbye')
def bye():
    return render_template("goodbye.html")

# madlib route to play game
@app.route('/madlib')
def show_madlib():
    name = request.args.get("username")
    person = request.args.get("person")
    color = request.args.get("color")
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")
    justin = request.args.get("justin")
    direction = request.args.get("direction")
    feelings = request.args.get("feelings")
    verb = request.args.get("verb")

    return render_template("madlib.html", username = name, person = person, noun = noun, adjective = adjective, color = color, justin = justin, direction = direction, feelings = feelings, verb = verb)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)