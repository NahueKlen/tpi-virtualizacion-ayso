# Programa de prueba ejecutado en Linux dentro de VirtualBox
# Solicita tres notas entre 0 y 10 y calcula su promedio

print ("=== Calculadora de promedio ===")

# Lista donde se guadan las notas ingresadas
notas = []

# Se solicita una nota en cada vuelta del ciclo.
for numero in range(1,4):
	while True:
		try:
			entrada = input (f"Ingrese la nota {numero} (0 al 10:) ")
			nota = float (entrada.replace(",", "."))

			#Solo se aceptan notas dentro del rango indicado
			if 0 <= nota <= 10:
				notas.append(nota)
				break

			print("La nota debe estar entre 0 y 10")
		except ValueError:
			print ("Ingrese un número válido")

# Se muestrael promedio y se muestra con dos decimales.
promedio = sum(notas) / len(notas)
print (f"Promedio final: {promedio:.2f}")
