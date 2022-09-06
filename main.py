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
def valor_presente_neto(iterations):
	"""
	Genera una lista de valores presentes netos
	"""
	# seteamos nuestros promedios iniciales
	resh = 0
	rescc = 0
	# iteramos para el numero que nos dan
	for _ in range(iterations):
		#saca probabilidad de hotel (mue y sigma son de la hoja)
		h1 = np.random.normal(-800, 50)
		h2 = np.random.normal(-800, 100)
		h3 = np.random.normal(-700, 150)
		h4 = np.random.normal(300, 200)
		h5 = np.random.normal(400, 200)
		h6 = np.random.normal(500, 200)
		h7 = np.random.uniform(200, 8440)
		#saca probabilidad de centro comercial CC (mue y sigma son de la hoja)
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
		# sumamos los valores
		resh += rh
		rescc += rcc
	# obtenemos el promedio de cada uno
	promedioh = resh/iterations
	promediocc = rescc/iterations
	# imprimimos los resultados
	print(f'========================= Los resultados con {iterations} iteraciones son =========================')
	print("Promedio de hoteles: ",promedioh)
	print("Promedio de Centro Comercial: ",promediocc)


# obtenemos los datos 100 veces
valor_presente_neto(100)
# obtenemos los datos de 1000 veces
valor_presente_neto(1000)
# obtenemos los datos de 10000 veces
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
	# set our prices and costs
	bought = 9
	price_bought = 1.5
	price_sold = 2.5
	price_not_sold = 0.5
	# initialize our variables
	revenue = 0
	total_sales = 0
	refund = 0
	quantity_refund = 0
	total = 0
	loss = 0
	quantity_loss = 0
	total_cost = 0
	print(f'========================= Para {iterations} dias =========================')
	# iterate for 9, 10, 11 that simulate the number of papers we bought
	for bought in range(9, 12):
		# iterate for the number of days
		for _ in range(iterations):
			# get the number of papers we sold
			total_cost += bought * price_bought
			# get the number of papers that people want
			papers_asked = random.choices(posibilities, weights=probabilities, k=1)[0]
			revenue += papers_asked * price_sold
			# get the number of papers we sold
			total_sales += min(papers_asked, bought)
			# get the refun we get from the papers we didn't sell
			refund += (bought - papers_asked) * price_not_sold if papers_asked < bought else 0
			# get the number of papers we didn't sold
			quantity_refund += bought - papers_asked if papers_asked < bought else 0
			# get the loss we get from the papers we didn't sell
			quantity_loss += papers_asked - bought if papers_asked > bought else 0
			loss += (papers_asked - bought) * price_sold if papers_asked > bought else 0
		# print the results
		print(f'============== cuando compro {bought} periodicos ==============')
		print('Ganancias', revenue)
		print('Devoluciones', refund)
		print('Perdida por no cubrir', loss)
		print('Total de ventas', total_sales)
		print('Cantidad de devoluciones', quantity_refund)
		print('Cantidad que gaste', total_cost)
		print('Total de perdidas', quantity_loss)
		# get the total of money we get from the sales and the ones we didn't sell
		total += total_sales * price_sold - total_cost + quantity_refund * price_not_sold - quantity_loss * (price_sold - price_bought)
		# print the total of money we get
		print('\tGanancia total (Gancias menos los costos de compra + los rembolsos - las ventas que deje pasar):', total)
		# reset our variables
		revenue = 0
		refund = 0
		total = 0
		loss = 0
		quantity_loss = 0
		total_sales = 0
		quantity_refund = 0
		total_cost = 0
		# add one to the number of papers we bought
		bought += 1

# simultate for 30 days
buy_papers(posible, probabilities, 30)
# simultate for 365 days ( 1mes )
buy_papers(posible, probabilities, 365)
# simultate for 3650 days ( 10 años )
buy_papers(posible, probabilities, 3650)
# %%
