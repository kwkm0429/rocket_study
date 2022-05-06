"""
理想的な推進システムの仮定の元の計算
"""

class Engine:
	def __init__(self):
		self.k = 1.3 #比熱比
		self.mach_exit = 2.4 #出口のマッハ数
		self.mach_throat = 1.0 #スロートのマッハ数
		self.pc = 0 #燃焼室圧
		self.pt = 0 #スロート圧
		self.pe = 0 #出口圧
		self.ratio_area_throat_exit = 0 #スロートと出口の面積比
		self.time_combustion = 10 #燃焼時間
		self.c_ave = 3038 #[m/s] 平均有効排気速度,\bar{c}
		self.c_star = 0 #[m/s]