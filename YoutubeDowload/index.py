from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
	filename = request.args.get('filename')
	return render_template('index.html', filename=filename)

@app.route('/submit', methods=['POST'])
def post_submit():
	
	url = request.form.get('url')
	yt = YouTube(url)
	yt.streams.first().download()
	filename=yt.title
	thumbnail = yt.thumbnail_url
	decription = yt.description
	length = yt.length

	print('視頻標題：',yt.title)
	print('視頻說明：',yt.description)
	print('視頻長度/秒',yt.length)
	return render_template('index.html',filename=filename,thumbnail = thumbnail,decription=decription,length=length)
	

if __name__ == '__main__':
	app.run(debug=True)