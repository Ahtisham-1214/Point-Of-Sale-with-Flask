from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hell():
    return render_template('login.html')  # ✅ Renders the HTML page


if __name__ == '__main__':
    app.run(debug=True)
