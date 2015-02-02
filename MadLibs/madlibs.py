from flask import Flask, render_template, request, redirect
from random import choice, sample

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
@app.route('/madlib', methods=['GET', 'POST'])
def show_madlib():
    if request.method == 'GET':
        name = request.args.get("username")
        person = request.args.get("person")
        color = request.args.get("color")
        adjective = request.args.get("adjective")
        noun1 = request.args.get("noun1")
        noun2 = request.args.get("noun2")
        justin = request.args.get("justin")
        direction = request.args.get("direction")
        d = request.args
        feelings = d.getlist("feelings")
        feeling = choice(feelings)
        pastverb1 = request.args.get("pastverb1")
        pastverb2 = request.args.get("pastverb2")
        presentverb1 = request.args.get("presentverb1")
        presentverb2 = request.args.get("presentverb2")
    else:
        name = request.form.get("username")
        person = request.form.get("person")
        color = request.form.get("color")
        adjective = request.form.get("adjective")
        noun1 = request.form.get("noun1")
        noun2 = request.form.get("noun2")
        justin = request.form.get("justin")
        direction = request.form.get("direction")
        d = request.form
        feelings = d.getlist("feelings")
        feeling = choice(feelings)
        pastverb1 = request.form.get("pastverb1")
        pastverb2 = request.form.get("pastverb2")
        presentverb1 = request.form.get("presentverb1")
        presentverb2 = request.form.get("presentverb2")

    if justin == "Justin Timberlake":
        html_choice = choice(["madlib-timberlake2.html", "madlib-timberlake.html"])
    else:
        html_choice = choice(["madlib-bieber2.html", "madlib-bieber.html"])

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliments = sample(AWESOMENESS, 3)

    return render_template(html_choice, username = name, person = person, noun1 = noun1, noun2 = noun2, adjective = adjective, color = color, justin = justin, direction = direction, feelings = feeling, presentverb1 = presentverb1, presentverb2 = presentverb2, pastverb1 = pastverb1, pastverb2 = pastverb2, compliments = compliments )


def greet_person():
    player = request.args.get("person")



    return render_template("compliment.html", person=player, compliment=compliment)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)