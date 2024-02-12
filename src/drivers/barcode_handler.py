import os
from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
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

        return path_from_tag
