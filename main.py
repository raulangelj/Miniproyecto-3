"""
Miniproyecto 3 - Generando Variables Aleatorias Discretas y Continuas
Raul Jimenez 19017
Donaldo Garcia 19683
"""
#%%
import numpy as np
import numpy_financial as nf

# %%
# Ejercicio 3.1
def valor_presente_neto(iterations):
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
		h7 = np.random.uniform(2000, 8440)
		#saca probabilidad de centro comercial CC
		cc1 = np.random.normal(-600, 50)
		cc2 = np.random.normal(-200, 50)
		cc3 = np.random.normal(-600, 100)
		cc4 = np.random.normal(250, 150)
		cc5 = np.random.normal(350, 150)
		cc6 = np.random.normal(400, 150)
		cc7 = np.random.uniform(1600, 6000)
		rh = nf.npv(0.1, [-800, h1, h2, h3, h4, h5, h6, h7])
		rcc = nf.npv(0.1,[-900, cc1, cc2, cc3, cc4, cc5, cc6, cc7])
		resh += rh
		rescc += rcc
	promedioh = resh/iterations
	promediocc = rescc/iterations
	print(f'========================= Los resultados con {iterations} iteraciones son =========================')
	print("Promedio de hoteles: ",promedioh)
	print("Promedio de Centro Comercial: ",promediocc)

valor_presente_neto(100)
valor_presente_neto(1000)
valor_presente_neto(10000)
# %%
