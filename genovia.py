import sys

def encontrar_evento_cumbre(eventos, inicio, fin):
    # Caso base: Si el segmento tiene 3 elementos, comprueba si hay evento cumbre
    if fin - inicio == 2:
        if eventos[inicio] < eventos[inicio + 1] > eventos[fin]:
            return eventos[inicio + 1]
        return None
    # Si el segmento se reduce a menos de 3 elementos, no puede tener evento cumbre
    if fin - inicio < 2:
        return None
    
    medio = inicio + (fin - inicio) // 2

    # Comprobar si hay evento cumbre en la mitad
    if eventos[medio] > eventos[medio - 1] and eventos[medio] > eventos[medio + 1]:
        return eventos[medio]
    
    # Si el elemento a la izquierda del medio es mayor, busca en el subsegmento izquierdo
    if eventos[medio - 1] > eventos[medio]:
        return encontrar_evento_cumbre(eventos, inicio, medio)
    # Si no, busca en el subsegmento derecho
    return encontrar_evento_cumbre(eventos, medio, fin)

if __name__ == "__main__":
    for line in sys.stdin:
        eventos = list(map(float, line.strip().split()))
        evento_cumbre = encontrar_evento_cumbre(eventos, 0, len(eventos) - 1)
        if evento_cumbre is not None:
            print(f'{evento_cumbre}')
        else:
            print('No hay evento cumbre')

            
