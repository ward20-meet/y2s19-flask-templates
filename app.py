from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	fruits = ["warak dawali", "raviolli", "spaggiti"]
	return render_template("index.html" ,fruits=fruits)





if __name__ == '__main__':
   app.run(debug = True)
