from flask import Flask, request
from flask.wrappers import Response
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

class Cryptography(Resource):
    def get(self):
        option = ['modifikasi']
        response = {"msg": option}
        return response
    
    def post(self):
        # BEGIN::Modifikasi encrypt function
        def modifikasi_encryptor(raw_text, key):
            processed_text = raw_text + ' encrypted with Modifikasi alg (key: {})'.format(key)
            return processed_text
        # END::Modifikasi encrypt function



        # BEGIN::Modifikasi decrypt function
        def modifikasi_decryptor(raw_text, key):
            processed_text = raw_text + ' decrypted with Modifikasi alg (key: {})'.format(key)
            return processed_text
        # END::Modifikasi decrypt function




        # BEGIN::Encryptor function
        def encryptor(raw_text, key, option):
            if option == 'modifikasi':
                processed_text = modifikasi_encryptor(raw_text, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak tersedia'
        # END::Encryptor function

        # BEGIN::Decryptor function
        def decryptor(raw_text, key, option):
            if option == 'modifikasi':
                processed_text = modifikasi_decryptor(raw_text, key)
                return processed_text
            else:
                return 'Jenis algoritma tidak diketahui'
        # END::Decryptor function
            
        # BEGIN::Checker function
        def checker(raw_text, key, option, type):
            if type == 'decrypt':
                processed_text = decryptor(raw_text,option)
                return processed_text
            elif type == 'encrypt':
                processed_text = encryptor(raw_text, option)
                return processed_text
            else:
                return 'Hanya dapat melakukan enkripsi dan dekripsi'
        # END::Checker function




        type = request.json['type']
        option = request.json['option']
        raw_text = request.json['raw_text']
        key = request.json['key']
        processed_text = checker(raw_text, key, option, type)

        response = {"msg": processed_text}
        return response

api.add_resource(Cryptography, "/api/cryptography", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)