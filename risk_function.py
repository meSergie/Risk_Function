
# coding: utf-8

# In[40]:

# при абсолютном штрафе функция риска R = M(|tettaBN - tetta|)
# Тогда R = M(tettaBN - tetta), либо R = -M(tettaBN - tetta), т.е. R = |M(tettaBN - tetta)|
# M(tettaBN - tetta) = M(tettaBN) - tetta = M(tettaAN * sqrt(N)/(1+sqrt(N)) + 0.5/(1+sqrt(N))) - tetta = 
# = sqrt(N)/(1+sqrt(N)) * M(tettaAN) + 0.5/(1+sqrt(N))) - tetta, а M(tettaAN) = tetta
# Тогда R = |(0.5 - tetta)/(1+sqrt(N))|


get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

# задаем значения параметра tetta
tetta_values = np.linspace(0,1,101)
N =10 # значение N для графика ф.р. от тетта

# Значения тетта и N для графика ф.р. от N
tetta = [0.1, 0.25, 0.7]
N_max = 101 # максимальное значение N
N_values = np.arange(1, N_max)

def risk_func(tetta, N):
    R = np.abs((0.5 - tetta)/(1+np.sqrt(N)))
    return R

fig = plt.figure(figsize=(5,6))
ax1 = fig.add_subplot(2,1,1)
R_tetta = risk_func(tetta_values,N)
ax1.plot(tetta_values, R_tetta)
ax1.set_xlabel('tetta')
ax1.set_ylabel('R')
ax1.set_ylim([0, 0.2])
ax1.text('0.45','0.15','N={}'.format(N))

ax2 = fig.add_subplot(2,1,2)
ax2.set_xlabel('N')
ax2.set_ylabel('R')
ax2.set_ylim([0, 0.3])
ax2.text('{}'.format(N_max*0.45),'0.25','N={}'.format(N_max))
for t in tetta:
    R_N = risk_func(t, N_values)
    ax2.plot(N_values, R_N)
    ax2.legend(tetta)

