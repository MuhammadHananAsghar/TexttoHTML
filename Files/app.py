from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def page():
	return render_template("index.html")

@app.route("/convert", methods=['POST','GET'])
def convert():
	if request.method == 'POST':
		name = request.form['text']
		lst = []
		if name == 'html':
			lst = ['html']
		elif name == 'div':
			lst = ['div']
		elif name == 'title':
			lst = ['title']
		elif name == 'body':
			lst = ['body']
		elif name == 'head':
			lst = ['head']
		else:
			lst = name.split(".")
			lst = [i.strip() for i in lst]
		if 'html' in lst:
			HTMLCode = '<html></html>'
		if 'head' in lst:
			HTMLCode = '<html><head></head></html>'
		if 'title' in lst:
			HTMLCode = '<html><head><title></title></head></html>'
		if 'body' in lst:
			HTMLCode = '<html><head><title></title></head><body></body></html>'
		if 'div' in lst:
			HTMLCode = '<html><head><title></title></head><body><div></div></body></html>'
	return render_template("index.html",value=HTMLCode);


if __name__ == "__main__":
	app.run(debug=True)