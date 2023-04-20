unidadesDeMedida = ["b", "B", "KB", "MB", "GB", "TB", "PB"]

print("Favor inserir a unidade de medida do número a ser convertido (b, B, KB, MB, GB, TB ou PB)")
unidadeAConverter = input()
print("Agora, a unidade de medida final.")
unidadeFinal = input()
print("Para finalizar, o valor numérico.")
valorNumérico = input()
valorNumérico = int(valorNumérico)

if unidadesDeMedida.index(unidadeAConverter) < unidadesDeMedida.index(unidadeFinal):
    conversões = int(unidadesDeMedida.index(unidadeFinal)) - int(unidadesDeMedida.index(unidadeAConverter))
else:
    conversões = int(unidadesDeMedida.index(unidadeAConverter)) - int(unidadesDeMedida.index(unidadeFinal))
print(conversões)

if unidadeAConverter == "b":
    valorNumérico /=8
    unidadeAConverter =  "B"

if int(unidadesDeMedida.index(unidadeAConverter)) < int(unidadesDeMedida.index(unidadeFinal)):
    for i in range(conversões):
        valorNumérico/=1024
    print("O total da conversão é de: " + str(valorNumérico) + ".")
elif int(unidadesDeMedida.index(unidadeAConverter)) > int(unidadesDeMedida.index(unidadeFinal)):
    if unidadeFinal == "b":
        for i in range(conversões - 1):
            valorNumérico*=1024
        valorNumérico*=8
        print("O total da conversão é de: " + str(valorNumérico) + ".")
else:
    for i in range(conversões):
        valorNumérico*=1024
    print("O total da conversão é de: " + str(valorNumérico) + ".")


