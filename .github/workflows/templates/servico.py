from flask import Flask, request
app = Flask(__name__)


@app.route('/index',methods=['POST'])
def calculadora():
    n1=request.form['n1']
    n2=request.form['n2']
    total = n1+n2
    return str(total)

    
if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)
