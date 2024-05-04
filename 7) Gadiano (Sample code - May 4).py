# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:57:45 2024

@author: jezreel m. gadiano
"""

import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.linspace(0, 10, 100)
true_slope = 2
true_intercept = 1
true_sigma = 0.5
y = true_slope * x + true_intercept + np.random.normal(scale=true_sigma, size=len(x))


with pm.Model() as linear_model:
    
    slope = pm.Normal('slope', mu=0, sigma=10)
    intercept = pm.Normal('intercept', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    
    mu = slope * x + intercept
    
    
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
    
    
    trace = pm.sample(1000, tune=1000)
    
    
pm.traceplot(trace)
plt.show()
