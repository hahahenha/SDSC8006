# -*- coding: utf-8 -*-
# @Time : 2022/2/10 11:24
# @Author : Xiao Han
# @E-mail : hahahenha@gmail.com
# @Site :
# @project: regional traffic control code
# @File : main.py
# @Software: PyCharm

import sim_environment
import static_signalling
import lqf_algo
import qr_dqn
from matplotlib import pyplot as plt


# Static signalling
sim_environment.endis_sumo_guimode(1) # 1 for visualization, 0 for not show
Nruns = 150
static_signalling.static_signalling(Nruns)

print("finish 1")

# Longest Queue First (LQF) algorithm
sim_environment.endis_sumo_guimode(1)
Nruns = 150
lqf_algo.lqf(Nruns)

print("finish 2")

# Train the QR-DQN model
sim_environment.endis_sumo_guimode(0)
Nruns = 25
qr_dqn.qr_dqn_train(Nruns)

print("finish 3")

# Try out performance
sim_environment.endis_sumo_guimode(1)
Nruns = 150
use_saved_model = 0
qr_dqn.qr_dqn_live_noplots(Nruns, use_saved_model)

print("finish 4")

