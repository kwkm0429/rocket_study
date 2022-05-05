"""
ロケット機体に関する計算
"""

import math

from engine import Engine
from simulator import Simulator

class Rocket:
	def __init__(self):
		## 打ち上げ場所パラメータ
		self.launch_site_latitude = 0
		self.launch_site_longitude = 0

		## 機体形態
		self.num_stages = 2 #機体段数
		
		# 質量に関するパラメータ
		self.mass_payload = 275 #[kg] ペイロード質量, mpl
		self.mass_prop = list(range(self.num_stages)) #[kg] 推進薬質量, mp
		self.mass_inert = list(range(self.num_stages)) #[kg] イナート質量, m0-mp-ml
		self.mass_total = 4500 #[kg] 充填済み初期機体質量, m0
		self.mass_cur = 0 #[kg] 時刻tにおける全体質量
		self.mass_ratio = 0.88 # self.mass_prop/self.mass_total # 質量割合, MR
		self.ratio_structure = 1-self.mass_ratio #構造効率, xi

		# 速度パラメータ
		self.ratio_payload = 0 
		self.vel_init = 0
		self.vel_last = 0
		self.vel_cur = 0
		self.vel_loss = 0
		self.delta_v = 0

		self.engine = Engine()

	def set_mass(self):
		self.mass_total = 4500
		self.mass_payload =275
		for i in range(self.num_stages):
			self.mass_prop[i] = (self.mass_total*(1-self.mass_ratio)-self.mass_payload)/self.num_stages
			self.mass_inert[i] = (self.mass_total*self.mass_ratio-self.mass_payload)/self.num_stages

	def calc_delta_v_single(self, mi, mpl, mp, ith):
		m0 = mi + mpl + mp
		delta_v = - self.engine.c_bar * math.log((m0-mp)/m0)
		print("ΔV%d = %f m/s" %(ith, delta_v))
		return delta_v

	def calc_delta_v_multiple(self):
		self.delta_v = 0
		for i in range(self.num_stages):
			self.delta_v += self.calc_delta_v_single(self.mass_inert[i], self.mass_payload, self.mass_prop[i], i) 
		print("ΔV = %f m/s" %self.delta_v)

	def update_mass(self, sim):
		# 質量流量一定の場合
		self.mass_cur = self.mass_total - self.mass_prop / engine.time_combustion * sim.time_cur

if __name__ == '__main__':
	rocket = Rocket()
	rocket.set_mass()
	rocket.calc_delta_v_multiple()
	print(vars(rocket))