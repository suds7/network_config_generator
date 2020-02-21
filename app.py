from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
	name = request.form['name']
	vlan = request.form['vlan']
	id = request.form['id']
	return render_template('pass.html', n=name,v=vlan,i=id )


if __name__ == '__main__':
	app.run(debug=True)	