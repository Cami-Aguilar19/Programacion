
import random

def suma_digitos(n: int) -> int:
    return sum(int(d) for d in str(n))

def invertir_numero(n: int) -> int:
    return int(str(n)[::-1])

def es_camaleon(n: int) -> bool:
    s = suma_digitos(n)
    rev = invertir_numero(n)
    return (s % 2== 0) and (rev % 3 == 0)

def main():
    while True:
        try:
            cantidad = int(input("cantidad de numeros a validar:").strip())
            if cantidad <= 0:
                return ValueError
            break
        except ValueError:
            print("Ingrese un numero entero positivo:")

    numeros = [random.randint(100, 99_999) for _ in range(cantidad)]

    print(f"Números generados: {numeros}")

    print("Resultados")

    for n in numeros:
        s = suma_digitos(n)
        rev = invertir_numero(n)
        ok = es_camaleon(n)

        detalle_suma = "par" if s % 2 == 0 else "impar"
        detalle_rev = "divisible entre 3" if rev % 3 == 0 else "no divisible entre 3"
        decision = "si" if ok else "no"
        print(f"{n}: suma {s} ({detalle_suma}), inverso {rev} ({detalle_rev}) => camaleon: {decision}")

if __name__ == "__main__":
    main()
