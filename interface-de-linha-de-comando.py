from calculadora_de_unidades_de_armazenamento import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKilobyte, KilobyteParaByte, KilobyteParaMegabyte, MegabyteParaKilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPentabyte, PentabyteParaTerabyte

print (' -Escreva 1 para bit Para Byte \n - Escreva 2 para byte Para Bit \n - Escreva 3 byte Para kilobyte \n - Escreva 4 para kilobyte Para byte \n - Escreva 5 kilobyte Para megabyte \n - Escreva 6 megabyte Para kilobyte \n - Escreva 7 megabyte Para gigabyte \n - Escreva 8 gigabyte Para megabyte \n - Escreva 9 gigabyte Para terabyte \n - Escreva 10 terabyte Para gigabyte \n - Escreva 11 terabyte Para pentabyte \n - Escreva 12 pentabyte Para terabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    print("Você escolheu a opção 1: 'Bit para Byte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print("Você escolheu a opção 2: 'Byte para Bit'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print("Você escolheu a opção 3: 'Byte para Kilobyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaKilobyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    print("Você escolheu a opção 5: 'Kilobyte para Byte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KilobyteParaByte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    print("Você escolheu a opção 5: 'Kilobyte para Megabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KilobyteParaMegabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    print("Você escolheu a opção 6: 'Megabyte para Kilobyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MegabyteParaKilobyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print("Você escolheu a opção 7: 'MegabyteParaGigabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MegabyteParaGigabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print("Você escolheu a opção 8: 'Gigabyte para Megabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GigabyteParaMegabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print("Você ecolheu a opção 9: 'Gigabyte para Terabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GigabyteParaTerabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print("Você escolheu a opção 10: 'Terabyte para Gigabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TerabyteParaGigabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print("Você escolheu a opção 11: 'Terabyte para Pentabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TerabyteParaPentabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print("Você escolheu a opção 12: 'Pentabyte para Terabyte'")
    entradaDoTecladovalorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PentabyteParaTerabyte(entradaDoTecladovalorASerConvertido)
    print(valorConvertido)