def conv(c):
    #calculod de celsius a fahrenheit 
    return (celsius * 9 / 5) + 32;

if __name__ == "__main__":
    print("Conversor de temperatura")
    try: 

        #pido al usuario la temperatura en celsius
        celsius = float(input("Introduzca la temperatura el celsius: "))

        #llamo a la funcion y convierto los ºCelsius a ºFahrenheit
        conversion = conv(celsius)

        #devuelvo la temperatura.
        print(f'{celsius} ºC equivalen a {conversion} ºF')
    except ValueError:
        print("El numero introducido no es valido.")
    
