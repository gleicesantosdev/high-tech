from flask import Flask, render_template, request, jsonify
import requests

app = Flask(_name_)

# API key para o Google Places API
GOOGLE_API_KEY = 'sua-google-api-key-aqui'

# Função para buscar estúdios de tatuagem próximos
def buscar_estudios(lat, lng, estilo):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=tattoo_shop&key={GOOGLE_API_KEY}"
    response = requests.get(url)
    resultados = response.json()

    estudios = []
    for lugar in resultados['results']:
        nome = lugar['name']
        endereco = lugar['vicinity']
        
        # Simulação de estilos baseados em dados fictícios
        estilos = ['realismo', 'old school', 'aquarela', 'minimalista', 'geométrico']
        
        # Para fins de exemplo, estúdios são atribuídos aleatoriamente a estilos
        if estilo in estilos:
            estudios.append({
                'nome': nome,
                'endereco': endereco,
                'estilo': estilo
            })
    
    return estudios

# Rota para exibir o formulário de pesquisa
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar a pesquisa
@app.route('/buscar', methods=['POST'])
def buscar():
    lat = request.form['lat']
    lng = request.form['lng']
    estilo = request.form['estilo']

    estudios = buscar_estudios(lat, lng, estilo)
    
    return render_template('resultado.html', estudios=estudios, estilo=estilo)

if _name_ == '_main_':
    app.run(debug=True)