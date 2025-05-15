from flask import Flask
from datetime import datetime #時間模組
app = Flask(__name__)

#首頁-------
@app.route('/')
def home():
	return '''
	<h1>🏠Home Page</h1>
	<p>Welcome to the Flask site with Docker page!</p>
	<a href="/about"> 🔗Go to ABOUT </a>
	<a href="/contact"> 📬Here is Contact </a>
	'''

#ABOUT分頁
@app.route('/about')
def about():
        return "🧠 This is the ABOUT page."

#Contact分頁
@app.route('/contact')
def contact():
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #格式化當前時間
	#return "✅ Hi here is the Contact page."
	return f'''
	<h1>📬 Contact Page </h1>
	<p>You can reach us at contact@example.com </p>
	<p>🕒 Current server time: {now}</p>
	'''
#啟動Flask Server---------
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

