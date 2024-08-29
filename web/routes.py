from flask import render_template, request
""" from models.model import predict_from_camera
 """
def configure_routes(app):
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    """ @app.route('/predict', methods=['POST'])
    def predict():
        # Pega a imagem da câmera enviada via requisição POST
        image = request.files['image']
        # Processa a imagem com o modelo de IA
        prediction = predict_from_camera(image)
        # Retorna o resultado da predição
        return {'prediction': prediction} """
