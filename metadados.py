import sys

def get_image_type(nome_arquivo: str):
    boolSucesso = False
    strTipArq = None
    strErro = None

    try:
        with open(nome_arquivo, 'rb') as conteudo
    except:
        strErro = sys.exc_info()[0]
    else:
        if conteudo.read(2) == b'\xFF\xD8':
            strTipArq = 'jpg'
            boolSucesso = True
        elif conteudo.read(8) == b'\x89PNG\r\n\x1a\n':
            strTipArq = 'png'
            boolSucesso = True

    return boolSucesso, strTipArq, strErro

strNomeArq = '20231002_152653.jpg'
retTipoArq = get_image_type(strNomeArq)