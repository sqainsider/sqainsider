from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    urls = [
        'http://www.w3schools.com',
        'http://techcrunch.com/',
        'https://www.fayerwayer.com/',
    ]
    return render_template('index.html', urls=urls)

if __name__ == "__main__":
    app.run(debug=True)