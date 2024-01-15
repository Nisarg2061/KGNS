from flask import Flask, render_template, jsonify

app = Flask(__name__)

dict_vendors = [
    {
        'id': 1, 
        'name': 'SynfullSolutions',
        'email': 'info@synfullsolutions.tech',
        'phone': '000000'
    },
    {
        'id': 2, 
        'name': 'Aviant',
        'email': 'info@aviant.in',
        'phone': '000000'
    },
    {
        'id': 3, 
        'name': 'SynfullProblems',
        'email': 'info@synfullproblems.tech',
        'phone': '000000'
    }
]
Titles = ['Vendor List', 'Inventory', 'Bill Generator', 'History']

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/vendors")
def first():
    return render_template('vendors.html', vendors=dict_vendors, titles=Titles)

@app.route("/api/vendors_list")
def list_vendors():
    return jsonify(dict_vendors)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)