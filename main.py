from fibonacci import fibonacci

def main():
    try:
        position = int(input("Ingrese la posición en la secuencia de Fibonacci: "))
        if position <= 0:
            print("Por favor, ingrese un número entero positivo mayor que cero.")
            return
        result = fibonacci(position)[-1]
        print(f"El valor en la posición {position} de la secuencia de Fibonacci es: {result}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
