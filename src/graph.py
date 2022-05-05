"""
グラフ描画
"""
import matplotlib.pyplot as plt
import numpy as np

from rocket import Rocket

def graph_delta_v(rocket):
	x = list(range(50))
	y = list(range(50))
	for i in range(50):
		rocket.mass_ratio = 0.02*(i+1)
		rocket.set_mass()
		rocket.calc_delta_v_multiple()
		x[i] = 1.0/rocket.mass_ratio
		y[i] = rocket.delta_v
	plt.plot(x, y)
	plt.xlabel("1/MR")
	plt.ylabel("ΔV m/s")
	plt.savefig("DeltaV-MR.png")
	plt.show()

if __name__ == '__main__':
	rocket = Rocket()
	graph_delta_v(rocket)