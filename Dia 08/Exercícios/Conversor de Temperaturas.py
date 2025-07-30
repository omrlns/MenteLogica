def celsiusParaFahrenheit(c):
    return c * 9/5 + 32

def FahrenheitParaCelsius(f):
    return (f - 32) * 5/9

def CelsiusParaKelvin(c):
    return c + 273.15

def KelvinParCelsius(k):
    return k - 273.15

temperatura = float(input('digite a temperatura: '))
unidade = str(input('digite a unidade atual (C, F, K): ')).strip().upper()[0]
converter = str(input('converter para (C, F, K): ')).strip().upper()[0]
if unidade == "C":
    if converter == "F":
        resultado = celsiusParaFahrenheit(temperatura)
    elif converter == "K":
        resultado = CelsiusParaKelvin(temperatura)
elif unidade == "F":
    if converter == "C":
        resultado = FahrenheitParaCelsius(temperatura)
    elif converter == "K":
        celsius = FahrenheitParaCelsius(temperatura)
    resultado = CelsiusParaKelvin(celsius)
elif unidade == "K":
    if converter == "C":
        resultado = KelvinParCelsius(temperatura)
    elif converter == "F":
        celsius = KelvinParCelsius(temperatura)
        resultado = celsiusParaFahrenheit(celsius)
else:
     resultado = 'unidade inválida.'
     
print('temperatura convertida: {} {}'.format(resultado, converter))