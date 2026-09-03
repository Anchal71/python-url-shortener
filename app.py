from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)

url_database = {}


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        long_url = request.form.get("url")

        if long_url:
            short_code = generate_short_code()

            while short_code in url_database:
                short_code = generate_short_code()

            url_database[short_code] = long_url

            short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):
    long_url = url_database.get(short_code)

    if long_url:
        return redirect(long_url)

    return "URL not found", 404


if __name__ == "__main__":
    app.run(debug=True)
        
