# --- Programa para calcular el promedio de un curso ---

# 1. Solicitar información inicial
nombre_curso = input("Ingresa el nombre del curso: ")
cantidad_notas = int(input("¿Cuántas notas deseas ingresar?: "))

# Variable para acumular la suma de las notas
suma_total = 0

# 2. Ciclo para solicitar cada nota
# El ciclo for recorrerá desde 0 hasta cantidad_notas - 1
for i in range(cantidad_notas):
    # Pedimos la nota (usamos i + 1 para que el mensaje diga "Nota 1", "Nota 2", etc.)
    nota = float(input(f"Ingresa la nota {i + 1}: "))
    suma_total += nota # Sumamos la nota al total

# 3. Calcular el promedio
# La fórmula matemática es:
# $$ \text{Promedio} = \frac{\sum \text{Notas}}{\text{Cantidad}} $$
promedio = suma_total / cantidad_notas

# 4. Mostrar el resultado
print("-" * 30)
print(f"En el curso {nombre_curso}, tu promedio final es: {promedio}")

#███████╗██╗███████╗██████╗ ██████╗  ██████╗ 
#██╔════╝██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗
#█████╗  ██║█████╗  ██████╔╝██████╔╝██║   ██║
#██╔══╝  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║
#██║     ██║███████╗██║  ██║██║  ██║╚██████╔╝
#╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝                                                
#██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗
#██╔══██╗██║   ██║██╔═══██╗██║   ██║██╔════╝
#██║  ██║██║   ██║██║   ██║██║   ██║█████╗  
#██║  ██║██║   ██║██║   ██║██║   ██║██╔══╝  
#██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗
#╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝
#         WWW.FIERRODUQUE.COM
