from flask import Flask, redirect, url_for, request, make_response, Response, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cep',methods = ['POST'])
def processa_cep():
   if request.method == 'POST':
      user = request.form["cep"]

      url = f"https://viacep.com.br/ws/{user}/json/"
      req = requests.request("GET", url)

      content = req.content.decode("utf-8")
      req.close()

      resp = Response(content)
      resp.headers["Access-Control-Allow-Origin"] = "*"
      resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"

      return resp, 201

if __name__ == "__main__":
    app.run(debug=True)
