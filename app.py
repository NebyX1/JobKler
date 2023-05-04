from flask import Flask, render_template

app = Flask(__name__)

Jobs = [
{
'id':1,
'position':'Full Stack Developer',
'city':'Montevideo',
'salary':'UYU 30.000'
},
{
'id':2,
'position':'Data Scientist',
'city':'Maldonado',
'salary':'UYU 28.000'
},
{
'id':3,
'position':'Data Scientist',
'city':'Minas',
'salary':'UYU 21.106'
},
{
'id':4,
'position':'Business Analyst',
'city':'Ciudad de la Costa',
'salary':'UYU 27.000'
},
]

@app.route("/")
def home():
	return render_template('home.html', Jobs = Jobs)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=3500, debug=True)