# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:35:05 2024
@author: jezreel m. gadiano
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style="darkgrid", palette="muted")

def simulate_linear_data(
    start, stop, N, beta_0, beta_1, eps_mean, eps_sigma_sq
):
      
    df = pd.DataFrame(
        {"x": 
            np.linspace(start, stop, num=N)
        }
    )
     
    df["y"] = beta_0 + beta_1*df["x"] + np.random.RandomState(s).normal(
        eps_mean, eps_sigma_sq, N
    )
    return df

def plot_simulated_data(df):
    
    sns.lmplot(x="x", y="y", data=df, height=10)
    plt.xlim(0.0, 1.0)
    plt.show()

if __name__ == "__main__":
    beta_0 = 1.0  
    beta_1 = 2.0  
   
    start = 0
    stop = 1
    N = 100
    eps_mean = 0.0
    eps_sigma_sq = 0.5
    s = 42

    df = simulate_linear_data(
        start, stop, N, beta_0, beta_1, eps_mean, eps_sigma_sq
    )
    plot_simulated_data(df)
    
    
    