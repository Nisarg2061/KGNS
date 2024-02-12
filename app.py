from flask import Flask, render_template, jsonify
from database import kgns_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/vendors")
def load_vendors():
    vendors = kgns_data()    
    return render_template('vendors.html', vendors=vendors)

@app.route("/api/vendors_list")
def list_vendors():
    return jsonify("Hello World!")

@app.route("/vendors/edit")
def edit_view_vendors():
    vendor = kgns_data()
    return render_template('add_vendor.html',vendor=vendor)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
