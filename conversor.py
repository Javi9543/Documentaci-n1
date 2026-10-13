if __name__ == "__main__":
    print("Conversor de temperatura")
    celsius = float(input("Introduzca la temperatura el celsius: "))
    conversion = (celsius *9/5) + 32;
    print(f'{celsius} ºC equivalen a {conversion} ºF');
