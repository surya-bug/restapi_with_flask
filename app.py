from flask import Flask

app = Flask(__name__)

@app.route("/") # 'https://www.yoursite.com/"

def home():
    return "Hello World !"
    
    
    
app.run(port=8080)

	



