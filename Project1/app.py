from flask import Flask, render_template, request
# import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data =[]
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)

@app.route('/period')
def period():
        

    with open('main2.csv', mode="r") as csv_file:
        reader = csv.reader(csv_file) 

    for item in reader:
        print(item[1])# index is added to get a particular column

if __name__ == "__main__":
    app.run(debug=True)