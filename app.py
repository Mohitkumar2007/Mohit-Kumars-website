from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Billing-Software"
}, {
    "id": 2,
    "title": "SGPA-Calculator"
}, {
    "id": 3,
    "title": "Downloader"
}, {
    "id": 4,
    "title": "X-Y Calculator"
}]


@app.route('/')
def hello_Mohit():
   return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
