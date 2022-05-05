"""
ロケットの種々の計算
"""
import math
from earth import Earth
from rocket import Rocket
from engine import Engine

def ex_3_1(engine, earth):
	engine.pc = earth.pressure * math.pow((1 + 0.5*(engine.k-1)*(engine.mach_exit**2)), engine.k/(engine.k-1))
	print("燃焼室圧 pc = %f MPa" %engine.pc)
	
	num = 1+(engine.k-1)/2*(engine.mach_exit**2)
	dem = 1+(engine.k-1)/2*(engine.mach_throat**2)
	pow_num = (engine.k+1)/(engine.k-1)
	engine.ratio_area_throat_exit = engine.mach_throat/engine.mach_exit*math.sqrt((num/dem)**pow_num)
	print("面積比（スロート/出口）A1/A2 = %f" %engine.ratio_area_throat_exit)

if __name__ == '__main__':
	earth = Earth()
	rocket = Rocket()

	ex_3_1(rocket.engine, earth)