from flask import Flask

app = Flask(__name__)

stores = [

    {
    
    'name' : 'My Wonderful Store',
    'items' : [
    
            {
        
                'name' : 'My Item',
                'price' : 15.99
        
        
            }
        
        ]
    

    
    
    
    }


]

@app.route("/") # 'https://www.yoursite.com/"

# POST - used to receive data
# GET - send data back only to the browser

@app.route("/store", methods=["POST"])
def create_store():
    pass
    
    
@app.route("/store/<string:name>")
def get_store(name):
    pass
    

@app.route("/store")
def get_store():
    pass

 
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass
 
    
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass
    
    
app.run(port=8080)

	



