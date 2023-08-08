from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Robert',
        'cocktail': 'magherita',
        'ingredients': 'tequila, lime orange',
        'date_posted': 'August 07, 2023'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
