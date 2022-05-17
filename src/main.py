"""
ロケットの種々の計算
"""
import math
from earth import Earth
from rocket import Rocket
from engine import Engine
from graph import graph_plot

def ex_3_1(engine, earth):
	engine.pc = earth.pressure * math.pow((1 + 0.5*(engine.k-1)*(engine.mach_exit**2)), engine.k/(engine.k-1))
	print("燃焼室圧 pc = %f MPa" %engine.pc)
	
	num = 1+(engine.k-1)/2*(engine.mach_exit**2)
	dem = 1+(engine.k-1)/2*(engine.mach_throat**2)
	pow_num = (engine.k+1)/(engine.k-1)
	engine.ratio_area_throat_exit = engine.mach_throat/engine.mach_exit*math.sqrt((num/dem)**pow_num)
	print("面積比（スロート/出口）A1/A2 = %f" %engine.ratio_area_throat_exit)

def ex_3_2(engine, earth):
	engine.pc = 2.068*1e6
	engine.tc = 2222
	engine.mass_dot = 1
	earth.pressure = 0.1013*1e6
	engine.k = 1.3
	engine.cp = 0.359
	engine.R = 345.7

	size = 51
	pres = list(range(size))
	vol = list(range(size))
	temp = list(range(size))
	vel = list(range(size))
	area = list(range(size))
	mach = list(range(size))
	for i in range(size):
		pres[i] = engine.pc*(i+1)/(size+1)
		vol[i]  = engine.R*engine.tc/pres[i]
		temp[i] = engine.tc*(pres[i]/engine.pc)**((engine.k-1)/engine.k)
		vel[i]  = math.sqrt((2*engine.k*engine.R*engine.tc)/(engine.k-1)*(1-(pres[i]/engine.pc)**((engine.k-1)/engine.k)))
		area[i] = engine.mass_dot*vol[i]/vel[i]
		mach[i] = vel[i]/math.sqrt(engine.k*engine.R*temp[i])

	graph_plot(pres, area, "Pressure", "Area", "figs/Ex3_2-P-Area.png")
	graph_plot(pres, vol, "Pressure", "Volume", "figs/Ex3_2-P-Vol.png")
	graph_plot(pres, temp, "Pressure", "Temperature", "figs/Ex3_2-P-Temp.png")
	graph_plot(pres, vel, "Pressure", "Velocity", "figs/Ex3_2-P-Vel.png")
	graph_plot(pres, mach, "Pressure", "Mach", "figs/Ex3_2-P-M.png")

def Q_5_1():
	# ΔV = - c * log(MR)
	delta_v = 1600
	c = 2000
	ans = math.exp(-delta_v/c)
	print("MR = %f" %ans)

def Q_5_2():
	xi = (1-1/5)/1
	print("xi = %f" %xi)

def Q_5_3():
	c = 2209
	xi = 0.57
	MR = 1-xi
	tp = 5.0
	delta_v = - c * math.log(MR)
	print("vf = %f" %delta_v)
	#print("h = %f" %())

if __name__ == '__main__':
	earth = Earth()
	rocket = Rocket()

	ex_3_1(rocket.engine, earth)
	ex_3_2(rocket.engine, earth)
	Q_5_1()
	Q_5_2()
	Q_5_3()