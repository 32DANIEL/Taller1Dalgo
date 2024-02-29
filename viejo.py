import sys
import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distancia_minima_div_conq(puntos):
    def distancia_min_rec(puntos_ordenados_x, puntos_ordenados_y):
        if len(puntos_ordenados_x) <= 3:
            return min(distancia(puntos_ordenados_x[i], puntos_ordenados_x[j]) for i in range(len(puntos_ordenados_x)) for j in range(i + 1, len(puntos_ordenados_x)))
        
        mitad = len(puntos_ordenados_x) // 2
        Qx = puntos_ordenados_x[:mitad]
        Rx = puntos_ordenados_x[mitad:]
        
        punto_medio = puntos_ordenados_x[mitad][0]
        Qy = list(filter(lambda p: p[0] <= punto_medio, puntos_ordenados_y))
        Ry = list(filter(lambda p: p[0] > punto_medio, puntos_ordenados_y))
        
        delta_q = distancia_min_rec(Qx, Qy)
        delta_r = distancia_min_rec(Rx, Ry)
        delta = min(delta_q, delta_r)
        
        banda = [p for p in puntos_ordenados_y if punto_medio - delta < p[0] < punto_medio + delta]
        min_dist_banda = delta
        for i in range(len(banda)):
            for j in range(i+1, min(i + 7, len(banda))):
                d = distancia(banda[i], banda[j])
                if d < min_dist_banda:
                    min_dist_banda = d
        
        return min_dist_banda
    
    puntos_ordenados_x = sorted(puntos, key=lambda p: p[0])
    puntos_ordenados_y = sorted(puntos, key=lambda p: p[1])
    return distancia_min_rec(puntos_ordenados_x, puntos_ordenados_y)

def main():
    while True:
        linea = sys.stdin.readline().strip()
        if not linea:
            break
        N = int(linea)
        if N == 0:
            break
        puntos = [tuple(map(float, sys.stdin.readline().strip().split())) for _ in range(N)]
        
        distancia_min = distancia_minima_div_conq(puntos)
        
        # Escribir el resultado a stdout
        if distancia_min < 10000:
            sys.stdout.write(f"{distancia_min:.4f}\n")
        else:
            sys.stdout.write("INFINITO\n")

if __name__ == "__main__":
    main()
