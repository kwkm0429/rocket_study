"""
地球のパラメータに関する計算
"""
import math

class Earth:
	def __init__(self):
		self.radius = 6378*1e3 #[m] 半径
		self.pressure = 0.1013 #[Pa] 大気圧
		self.graivty = 9.80665 #[m/s^2] 重力
		self.height = 100*1e3 #[m] 高さ
		self.vel_esc = 0 #[m/s] 脱出速度
		self.vel_orb = 0 #[m/s] 軌道速度

	def set_vel(self):
		# 高度による重力の変化を考慮 g=g0*(R0/(R0+h))
		# 軌道速度（第一宇宙速度）
		self.vel_orb = self.radius * math.sqrt(self.graivty/(self.radius+self.height))
		print("orbital velocity = %f m/s" %self.vel_orb)
		# 脱出速度（第二宇宙速度）
		self.vel_esc = self.radius * math.sqrt(2*self.graivty/(self.radius+self.height))
		print("escape velocity = %f m/s" %self.vel_esc)

if __name__ == '__main__':
	earth = Earth()
	earth.set_vel()