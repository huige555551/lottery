# coding: utf-8
from flask import Flask,render_template
import lottery2

app = Flask(__name__)

@app.route("/")
def index():
	lists = lottery2.main()
	return render_template('index.html', lists=lists)
if __name__ == "__main__":
	app.run(debug=True)