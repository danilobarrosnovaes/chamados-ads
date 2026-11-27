from flask import Flask, request

app = Flask(__name__)

"""
Variáveis para salvar os dados do chamado ---TEMPORÁRIO
"""
chamados = []
proximo_id = 1

"""
ROTAS APLICAÇÃO
"""

@app.get("/")
def inicio():
    """"Rota inicial apalicação"""
    return {
        "mensagem": "API de chamados em funcionamento"
    }

@app.post("/chamados")
def criar_chamados():
    """"Salva o Chamado"""

    # declara as variáveis globais
    global chamados
    global proximo_id

    #obtem conteúdo enviado via POST ---> lembrar de importar request
    chamado = request.get_json()

    # adiciona um id ao chamado
    chamado["id"] = proximo_id

    # adiciona o novo chamado a nossa lista de chamados
    chamados.append(chamado)

    # incrementa o proximo_id
    proximo_id += 1

    return{
        "message": "Chamado criado",
        "chamado": chamado
    }, 200

@app.get("/chamados")
def get_chamados():
    global chamados
    return chamados

    
@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    """"Retorna o chamado que tem id == chamado_id"""
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado, 200
    return {"message": "Chamado não encontrando"}, 404
