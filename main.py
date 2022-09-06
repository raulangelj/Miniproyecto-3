"""
Miniproyecto 3 - Generando Variables Aleatorias Discretas y Continuas
Raul Jimenez 19017
Donaldo Garcia 19683
"""
#%%
import random
from unittest.util import unorderable_list_difference
import numpy as np
import numpy_financial as nf

# %%
# Ejercicio 3.1
def normal(mues, sigmas):
	"""
	Obtenemos una lista de valores aleatorios con distribucion normal
	"""
	return [np.random.normal(mues[i], sigmas[i]) for i in range(len(mues))]

def valor_presente_neto(iterations):
	"""
	Genera una lista de valores presentes netos
	"""
	resh = 0
	rescc = 0
	for _ in range(iterations):
		#saca probabilidad de hotel
		h1 = np.random.normal(-800, 50)
		h2 = np.random.normal(-800, 100)
		h3 = np.random.normal(-700, 150)
		h4 = np.random.normal(300, 200)
		h5 = np.random.normal(400, 200)
		h6 = np.random.normal(500, 200)
		h7 = np.random.uniform(200, 8440)
		#saca probabilidad de centro comercial CC
		cc1 = np.random.normal(-600, 50)
		cc2 = np.random.normal(-200, 50)
		cc3 = np.random.normal(-600, 100)
		cc4 = np.random.normal(250, 150)
		cc5 = np.random.normal(350, 150)
		cc6 = np.random.normal(400, 150)
		cc7 = np.random.uniform(1600, 6000)
		# sacamos el net present value de cada uno
		rh = nf.npv(0.1, [-800, h1, h2, h3, h4, h5, h6, h7])
		rcc = nf.npv(0.1,[-900, cc1, cc2, cc3, cc4, cc5, cc6, cc7])
		resh += rh
		rescc += rcc
	# obtenemos el promedio de cada uno
	promedioh = resh/iterations
	promediocc = rescc/iterations
	print(f'========================= Los resultados con {iterations} iteraciones son =========================')
	print("Promedio de hoteles: ",promedioh)
	print("Promedio de Centro Comercial: ",promediocc)

# nuestros mues y sigmas
mues_hoteles = [-800, -800, -700, 300, 400, 500, 2000]
sigmas_hoteles = [50, 100, 150, 200, 200, 200, 8440]
mues_cc = [-600, -200, -600, 250, 350, 400, 1600]
sigmas_cc = [50, 50, 100, 150, 150, 150, 6000]
# obtenemos los datos
valor_presente_neto(100)
valor_presente_neto(1000)
valor_presente_neto(10000)
# %%
# sabe que el 30% de los días le piden 9,el40%delosdíaslepiden10yel30%delosdíasle
# piden 11 periódicos. Si usted compra los periódicos para luego venderlos, y paga $1.50 por periódico, lo vende a
# $2.50 y por cada periódico no vendido se le reembolsa $0.50.
# 1. ¿Cuál es la cantidad que más le conviene comprar todos los días? Simule para un mes, un año y diez años

# creamos nuestro arrey con las posibilidades
posible = [9, 10, 11]
# creamos el array de probabilidades
probabilities = [0.3, 0.4, 0.3]

def buy_papers(posibilities, probabilities, iterations):
	average = 0
	bought = 9
	price_bought = 1.5
	price_sold = 2.5
	price_not_sold = 0.5
	# ganancia 
	revenue = 0
	# total de ventas
	total_sales = 0
	# dinero devoliciones
	refund = 0
	# cantidad que tuvimos que devolver
	quantity_refund = 0
	# ganancia total
	total = 0
	# perdida por no cubrir
	loss = 0
	# cantidad de ventas que no hicimos
	quantity_loss = 0
	# lo que gaste
	total_cost = 0

	# para cuando compro 9 periodicos
	print(f'========================= Para {iterations} dias =========================')
	while bought <= 11:
		for _ in range(iterations):
			# obtenemos la cantidad que gastamos por comprar periodicos
			total_cost += bought * price_bought
			# obtenemos el valor
			papers_asked = random.choices(posibilities, weights=probabilities, k=1)[0]
			# obtenemos las ganancias de los que me pidieron y se vendieron
			revenue += papers_asked * price_sold
			# revenue += papers_asked * (price_sold - price_bought) if papers_asked <= bought else bought * (price_sold - price_bought)
			total_sales += papers_asked if papers_asked <= bought else bought
			# print('revenue', revenue)
			# obtenemos las devoluciones de los que no se vendieron
			refund += ((bought - papers_asked) * price_not_sold) if papers_asked < bought else 0
			quantity_refund += bought - papers_asked if papers_asked < bought else 0
			# refund += ((bought - papers_asked) * price_not_sold) if papers_asked <= bought else 0
			# quantity_refund += bought - papers_asked if papers_asked <= bought else 0
			# print('refund', refund)
			# obtenemos la perdida por no cubrir si se pidieron mas de los que se compraron
			# loss += (papers_asked - bought) * price_bought if papers_asked > bought else 0
			# # si lo que pidieron es menor a lo que se compro sumamos a loss el valor de lo que se pidio
			# loss += papers_asked * (price_bought - price_not_sold) if papers_asked < bought else 0
			# loss += abs((papers_asked - bought) * (price_bought - price_not_sold))
			quantity_loss += papers_asked - bought if papers_asked > bought else 0
			loss += (papers_asked - bought) * price_sold if papers_asked > bought else 0
			# loss += (papers_asked - bought) * (price_bought - price_not_sold) if papers_asked > bought else 0
			# quantity_loss += papers_asked - bought if papers_asked > bought else 0
			# print('loss', loss)
		print(f'============== cuando compro {bought} periodicos ==============')
		print('Ganancias', revenue)
		print('Devoluciones', refund)
		print('Perdida por no cubrir', loss)
		print('Total de ventas', total_sales)
		print('Cantidad de devoluciones', quantity_refund)
		print('Cantidad que gaste', total_cost)
		print('Total de perdidas', quantity_loss)
		# obtenemos la ganancia total
		total += (total_sales * price_sold) - total_cost + quantity_refund * price_not_sold - quantity_loss * (price_sold - price_bought)
		# total += revenue - total_cost + quantity_refund * price_not_sold - quantity_loss * (price_sold - price_bought)
		# total += revenue + refund - loss 
		print('\tGanancia total (Gancias menos los costos de compra + los rembolsos):', total)
		# reiniciamos los valores
		revenue = 0
		refund = 0
		total = 0
		loss = 0
		quantity_loss = 0
		total_sales = 0
		quantity_refund = 0
		total_cost = 0

		bought += 1

	# papers_asked = 9
	# print(papers_asked)
	# # obtenemos las ganancias de los que me pidieron y se vendieron
	# revenue = papers_asked * (price_sold - price_bought) if papers_asked <= bought else bought * (price_sold - price_bought)
	# print('revenue', revenue)
	# # obtenemos las devoluciones de los que no se vendieron
	# refund = (bought - papers_asked) * price_not_sold if papers_asked <= bought else 0
	# print('refund', refund)
	# # obtenemos la perdida por no cubrir
	# loss = abs((papers_asked - bought) * (price_bought - price_not_sold))
	# print('loss', loss)
	# # obtenemos la ganancia total
	# total = revenue + refund - loss
	# print('total', total)

	# papers_asked = 10
	# print(papers_asked)
	# # obtenemos las ganancias de los que me pidieron y se vendieron
	# revenue = papers_asked * (price_sold - price_bought) if papers_asked <= bought else bought * (price_sold - price_bought)
	# print('revenue', revenue)
	# # obtenemos las devoluciones de los que no se vendieron
	# refund = (bought - papers_asked) * price_not_sold if papers_asked <= bought else 0
	# print('refund', refund)
	# # obtenemos la perdida por no cubrir
	# loss = abs((papers_asked - bought) * (price_bought - price_not_sold))
	# print('loss', loss)
	# # obtenemos la ganancia total
	# total = revenue + refund - loss
	# print('total', total)

	# papers_asked = 11
	# print(papers_asked)
	# # obtenemos las ganancias de los que me pidieron y se vendieron
	# revenue = papers_asked * (price_sold - price_bought) if papers_asked <= bought else bought * (price_sold - price_bought)
	# print('revenue', revenue)
	# # obtenemos las devoluciones de los que no se vendieron
	# refund = (bought - papers_asked) * price_not_sold if papers_asked <= bought else 0
	# print('refund', refund)
	# # obtenemos la perdida por no cubrir
	# loss = abs((papers_asked - bought) * (price_bought - price_not_sold))
	# print('loss', loss)
	# # obtenemos la ganancia total
	# total = revenue + refund - loss
	# print('total', total)

	# # asumir que todos los dias compro 10 luego 9 luego 11 y ver cual es el mejor
	# while bought <= 11:
	# 	for _ in range(iterations):
	# 		# obtenemos el valor
	# 		choice = random.choices(posibilities, weights=probabilities, k=1)[0]
	# 		# sumamos el valor
	# 		average += choice
	# 		# ver cuantos salen de cada unorderable_list_difference




	# obtenemos el promedio
	# average = average/iterations
	# print(f'========================= Los resultados con {iterations} iteraciones son =========================')
	# print("Promedio de periódicos comprados: ",average)

buy_papers(posible, probabilities, 30)
buy_papers(posible, probabilities, 365)
buy_papers(posible, probabilities, 3650)
# %%
