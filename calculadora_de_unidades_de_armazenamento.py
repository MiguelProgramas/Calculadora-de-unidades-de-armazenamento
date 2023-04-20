valorComum = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

#Bit-byte

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    print(bytesCalculado)
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    print(bitsCalculado)
    return bitsCalculado

#Byte-Kilobyte

def byteParaKilobyte(bytesCalculado):
    print('Valor convertido de byte para kilobyte')
    kilobytescalculado = bytesCalculado / valorComum
    print(kilobytescalculado)
    return kilobytescalculado

def KilobyteParaByte(kilobytescalculado):
    print('Valor convertido de kilobyte para byte')
    bytescalculado2 = kilobytescalculado * valorComum
    print(bytescalculado2)
    return bytescalculado2

#Kilobyte-Megabyte

def KilobyteParaMegabyte(kilobytescalculado):
    print('Valor convertido de kilobyte para megabyte')
    MegasCalculado = kilobytescalculado / valorComum
    print(MegasCalculado)
    return MegasCalculado

def MegabyteParaKilobyte(MegasCalculado):
    print('Valor convertido de megabyte para kilobyte')
    kilobytescalculado2 = MegasCalculado * valorComum
    print(kilobytescalculado2)
    return kilobytescalculado2

#Megabyte-Gigabyte

def MegabyteParaGigabyte(MegasCalculado):
    print('Valor convertido de megabyte para gigabyte')
    GigasCalculado = MegasCalculado / valorComum
    print(GigasCalculado)
    return GigasCalculado

def GigabyteParaMegabyte(GigasCalculado):
    print('Valor convertido de gigabyte para megabyte')
    MegasCalculado2 = GigasCalculado * valorComum
    print(MegasCalculado2)
    return MegasCalculado2

#Gigabyte-Terabyte

def GigabyteParaTerabyte(GigasCalculado):
    print('Valor convertido de gigabyte para terabyte')
    TerasCalculado = GigasCalculado / valorComum
    print(TerasCalculado)
    return TerasCalculado

def TerabyteParaGigabyte(TerasCalculado):
    print('Valor convertido de terabyte para gigabyte')
    GigasCalculado2 = TerasCalculado * valorComum
    print(GigasCalculado2)
    return GigasCalculado2

#Terabyte-Pentabyte

def TerabyteParaPentabyte(TerasCalculado):
    print('Valor convertido de terabyte para pentabyte')
    PentasCalculado = TerasCalculado / valorComum
    print(PentasCalculado)
    return PentasCalculado

def PentabyteParaTerabyte(PentasCalculado):
    print('Valor convertido de pentabyte para terabyte')
    TerasCalculado2 = PentasCalculado * valorComum
    print(TerasCalculado2)
    return TerasCalculado2





