import wikipedia as wiki

wiki.set_lang('pt')

pesquisa = wiki.summary('Dom Casmurro')

alfabeto = str('abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ ')
pos = []

Mode_Encrypt = True
Mode_Decrypt = False

palavra = str(pesquisa.replace(" ", "*"))


def cifra(msg, chave, modo):

    if modo:
        for p in msg:
            pos.append(alfabeto.find(p))
        for n in pos:
            print(f'{alfabeto[n+chave]}', end='')

    if not modo:
        for p in msg:
            pos.append(alfabeto.find(p))
        for n in pos:
            print(f'{alfabeto[n-chave]}', end='')


cifra(palavra, 7, Mode_Encrypt)
cifra(palavra, 7, Mode_Decrypt)
