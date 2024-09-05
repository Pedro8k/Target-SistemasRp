
def conta_as(texto):
    lista_as = 'aAàÀãÃáÁâÂ'
    contador = 0
    for letra in texto:
        if letra in lista_as:
            contador+=1
    print("A quantidade de a's é: ", str(contador))

conta_as('Azul')
conta_as('Fui à feira comprar um âmbar.')
conta_as('Não, mão')
