import os
from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter


app = Flask(__name__)


@app.route('/create_tag', methods=['POST'])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    # Crie o caminho completo para a pasta minha_tag
    minha_tag = os.path.join(os.getcwd(), 'minha_tag')

    # Certifique-se de que a pasta existe; se não, crie-a
    if not os.path.exists(minha_tag):
        os.makedirs(minha_tag)

    # Crie a instância do código de barras e defina o caminho de salvamento
    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = os.path.join(minha_tag, f'{product_code}')

    # Salve a imagem no caminho especificado
    tag.save(path_from_tag)

    return jsonify({"tag path": path_from_tag})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
