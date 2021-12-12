from flask import Flask, request
from flask.wrappers import Response
from flask_restful import Resource, Api
from flask_cors import CORS
from CryptoHelper import decryptingFile, decryptingText, encryptingText, encryptingFile
import os

app = Flask(__name__)

api = Api(app)

CORS(app)

class Cryptography(Resource):
    def get(self):
        option = ['modifikasi']
        response = {"msg": option}
        return response
    
    def post(self):
        # BEGIN::Encryptor function
        def encryptor(raw_text, key, option):
            if option == 'modifikasi':
                processed_text = encryptingText(raw_text, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak tersedia'
        # END::Encryptor function

        # BEGIN::Decryptor function
        def decryptor(raw_text, key, option):
            if option == 'modifikasi':
                processed_text = decryptingText(raw_text, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak diketahui'
        # END::Decryptor function
            
        # BEGIN::Checker function
        def checker(raw_text, key, option, type):
            if type == 'decrypt':
                processed_text = decryptor(raw_text, key, option)
                return processed_text
            elif type == 'encrypt':
                processed_text = encryptor(raw_text, key, option)
                return processed_text
            else:
                return 'Hanya dapat melakukan enkripsi dan dekripsi'
        # END::Checker function

        # BEGIN::Encryptor function
        def fileEncryptor(file, key, option):
            if option == 'modifikasi':
                processed_text = encryptingFile(file, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak tersedia'
        # END::Encryptor function

        # BEGIN::Decryptor function
        def fileDecryptor(file, key, option):
            if option == 'modifikasi':
                processed_text = decryptingFile(file, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak diketahui'
        # END::Decryptor function

        # BEGIN::Checker function
        def fileChecker(file, key, option, type):
            if type == 'decrypt':
                processed_text = fileDecryptor(file, key, option)
                return processed_text
            elif type == 'encrypt':
                processed_text = fileEncryptor(file, key, option)
                return processed_text
            else:
                return 'Hanya dapat melakukan enkripsi dan dekripsi'
        # END::Checker function


        if 'file' not in request.files:
            type = request.form['type']
            option = request.form['option']
            raw_text = request.form['raw_text']
            key = request.form['key']
            processed_text = checker(raw_text, key, option, type)
        else:
            file = request.files['file']
            file.save(os.path.join('uploaded_file/raw', file.filename))
            option = request.form['option']
            type = request.form['type']
            key = request.form['key']
            processed_text = fileChecker(file, key, option, type)

        return processed_text
        type = request.json['type']
        option = request.json['option']
        raw_text = request.json['raw_text']
        key = request.json['key']
        processed_text = checker(raw_text, key, option, type)



api.add_resource(Cryptography, "/api/cryptography", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)