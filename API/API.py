from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

# Configuração da pasta de uploads e banco de dados
UPLOAD_FOLDER = 'C:/Users/geova/Downloads/API'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
db = SQLAlchemy(app)

# Modelo da Tabela de Arquivos
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

# Cria a tabela de arquivos no banco de dados
with app.app_context():
    db.create_all()

# Rota para upload de arquivos (POST)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo encontrado na requisição'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'Nenhum arquivo selecionado'}), 400

    # Salvando o arquivo
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    # Salvando os dados do arquivo no banco de dados
    file_size = os.path.getsize(file_path)
    new_file = File(filename=file.filename, size=file_size)
    db.session.add(new_file)
    db.session.commit()

    return jsonify({'message': 'Arquivo salvo com sucesso'}), 201

# Rota para gerar um relatório dos arquivos (GET)
@app.route('/report', methods=['GET'])
def generate_report():
    files = File.query.all()
    report = [{'filename': file.filename, 'size_kb': file.size / 1024, 'upload_date': file.upload_date} for file in files]
    
    return jsonify(report), 200


# Rota para listar arquivos (GET)
@app.route('/files', methods=['GET'])
def list_files():
    files = File.query.all()
    files_list = [{'id': file.id, 'filename': file.filename, 'size': file.size, 'upload_date': file.upload_date} for file in files]
    return jsonify(files_list), 200

@app.route('/files/<filename>', methods=['GET'])
def download_file(filename):
  # Verificar se o arquivo existe
  file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  if not os.path.exists(file_path):
    return jsonify({'message': 'Arquivo não encontrado'}), 404

  # Download do arquivo caso exista
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Rota para deletar arquivo (DELETE)
@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_record = File.query.filter_by(filename=filename).first()
    
    if file_record:
        # Remover arquivo físico
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Remover registro no banco de dados
        db.session.delete(file_record)
        db.session.commit()
        return jsonify({'message': 'Arquivo deletado com sucesso'}), 200
    else:
        return jsonify({'message': 'Arquivo não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
