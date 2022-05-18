"""
理想的な推進システムの仮定の元の計算
"""

class Engine:
	def __init__(self):
		self.k = 1.3 #比熱比
		self.cp = 0 
		self.R = 0
		# 圧力
		self.pc = 0 #燃焼室圧
		self.pt = 0 #スロート圧
		self.pe = 0 #出口圧
		# 温度
		self.tc = 0 #燃焼室温度
		self.tt = 0 #スロート温度
		self.te = 0 #出口温度
		self.mass_dot = 0 #燃料消費率
		# 面積
		self.area_t = 0 #スロート面積
		self.area_e = 0 #出口面積
		self.ratio_area_throat_exit = 0 #スロートと出口の面積比
		# 比容積
		self.vol_t = 0 #スロート比容積
		self.vol_t = 0 #燃焼室比容積
		self.vol_e = 0 #出口比容積
		# 速度
		self.vel_t = 0 # スロート速度
		self.vel_e = 0 # 出口速度
		self.mach_exit = 2.4 #出口マッハ数
		self.mach_throat = 1.0 #スロートマッハ数

		self.time_combustion = 10 #燃焼時間
		self.c_ave = 3038 #[m/s] 平均有効排気速度,\bar{c}
		self.c_star = 0 #[m/s]
		self.thrust = 0 #[N] 推力
