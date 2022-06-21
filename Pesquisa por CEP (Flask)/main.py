
# Importação de módulos essenciais
from flask import Flask, redirect, url_for, request, make_response, Response, render_template
import requests # Para fazer requisição na API viacep

# Cria uma instância Flask
app = Flask(__name__, template_folder='templates')

# Cria uam rota para a página principal (https://localhost:5000)
@app.route('/')
def index():
    # Carrega o arquivo index.html na pasta template e retorna seu conteúdo
    # para ser renderizado pelo navegador web
    return render_template("index.html")


# Cria uma rota para a pesquisa por CEP (https://localhost:5000/cep)
@app.route('/cep',methods = ['POST'])   # Usa o método POST para as requisições
def pesquisa_por_cep():
   if request.method == 'POST': # Se a reqquisição for do tipo POST
      cep = request.form["cep"]    # Captura o valor do CEP do formulário

      url = f"https://viacep.com.br/ws/{cep}/json/" # Gera URL para requisição
      
      # Efetua a requisição na API viacep e captura a resposta
      req = requests.request("GET", url)

      content = req.content.decode("utf-8") # Recupera o conteúdo da resposta
      req.close() # Encerra a reqquisição da API viacep

      # Cria resposta para o frontend
      resp = Response(content)
      # Estabelece o cabeçalho da resposta
      resp.headers["Access-Control-Allow-Origin"] = "*"
      resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"

      # Retorna a resposta para o frontend com sucesso
      return resp, 201

# Executa a função principal
if __name__ == "__main__":
    app.run(debug=True)     # Habilita o modo debug do Flask
