# Universidad del Valle de Guatemala
# Modelacion y Simulacion
# Miniproyecto # 8
# Integrantes: Diego Arredondo
#              Julio Herrera
#              Oscar Saravia
# Se uso como fuente el siguiente enlace: https://www.geeksforgeeks.org/genetic-algorithms/

# Librerias
import random

# Variables globales
OBJETIVO = input('Ingrese la frase que desea generar: ')
CARACTERES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TAMANO_POBLACION = 100

# Clase para generar un Elemento, el cual se utilizara en el proceso de seleccion
class Elemento(object):
	def __init__(self, cromosoma):
    # Se settean las variables correspondientes a el cromosoma y el valor de fitness
		self.cromosoma = cromosoma
		self.fitness = self.calcular_fitness()

	@classmethod
  # Devuelve un gene con una opcion aleatoria entre los caracteres
	def mutaciones(self):
		global CARACTERES
		gen = random.choice(CARACTERES)
		return gen

	@classmethod
  # Genera un genoma
	def generar_genoma(self):
		global OBJETIVO
		gnome_len = len(OBJETIVO)
		return [self.mutaciones() for i in range(gnome_len)]

	def generar(self, par2):
		cromosoma_hijo = []
		for gp1, gp2 in zip(self.cromosoma, par2.cromosoma):	
      # Genera un valor de probabilidad aleatoria
			probabilidad = random.random()

      # Se elige el genoma del padre 1
			if probabilidad < 0.45:
				cromosoma_hijo.append(gp1)
			# Se elige el genoma del padre 2
			elif probabilidad < 0.90:
				cromosoma_hijo.append(gp2)
			# Generar mutacion
			else:
				cromosoma_hijo.append(self.mutaciones())
		return Elemento(cromosoma_hijo)

	def calcular_fitness(self):
		global OBJETIVO
    # Se calcula el falor del fitness para el cromosoma
		fitness = 0
		for gs, gt in zip(self.cromosoma, OBJETIVO):
			if gs != gt: fitness+= 1
		return fitness

def main():
	global TAMANO_POBLACION
	generacion = 1
	terminado = False
	poblacion_a = []

	# Crear la poblacion inicial
	for i in range(TAMANO_POBLACION):
				gnome = Elemento.generar_genoma()
				poblacion_a.append(Elemento(gnome))

	while not terminado:
		poblacion_a = sorted(poblacion_a, key = lambda x:x.fitness)
		if poblacion_a[0].fitness <= 0:
			terminado = True
			break
		new_generation = []
		s = int((10*TAMANO_POBLACION)/100)
		new_generation.extend(poblacion_a[:s])
		s = int((90*TAMANO_POBLACION)/100)
		for _ in range(s):
			parent1 = random.choice(poblacion_a[:50])
			parent2 = random.choice(poblacion_a[:50])
			child = parent1.generar(parent2)
			new_generation.append(child)

		poblacion_a = new_generation

		print("Generacion # {}\tFrase: {}\tFitness: {}".\
			format(generacion,
			"".join(poblacion_a[0].cromosoma),
			poblacion_a[0].fitness))

		generacion += 1

	
	print("Generacion # {}\tFrase: {}\tFitness: {}".\
		format(generacion,
		"".join(poblacion_a[0].cromosoma),
		poblacion_a[0].fitness))

if __name__ == '__main__':
	main()
