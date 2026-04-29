import streamlit as st
import numpy as np
import analytics
import greeks
import matplotlib.pyplot as plt
S0 = st.slider("Select a spot price: ", 50, 200, 100)  
K = st.slider("Select a strike price: ", 50, 200, 100)
r = st.slider("Select a risk-free rate: ", 0.01, 0.05, 0.03)
sigma = st.slider("Select a volatility: ", 0.1, 0.5, 0.2)
T = st.slider("Select a time to maturity (in years): ", 0.1, 2.0, 1.0)

st.metric("Option Price: ", analytics.black_scholes(S0, K, r, sigma, T))
col1,col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Delta: ", f"{greeks.delta_analytical(S0, K, r, sigma, T):.4f}")

with col2:
    st.metric("Gamma: ", f"{greeks.gamma_numerical(S0, K, r, sigma, T):.4f}")

with col3:
    st.metric("Vega: ", f"{greeks.vega_numerical(S0, K, r, sigma, T)/100:.4f}")
    
with col4:
    st.metric("Theta: ", f"{greeks.theta_numerical(S0, K, r, sigma, T)/365:.4f}")

with col5:
    st.metric("Rho: ", f"{greeks.rho_numerical(S0, K, r, sigma, T)/100:.4f}")

spot_range = np.linspace(50, 200)
sigma_range = np.linspace(0.1, 0.5)
t_range = np.linspace(0.1, 2.0)
r_range = np.linspace(0.01, 0.05)
delta_values = [greeks.delta_analytical(s, K, r, sigma, T) for s in spot_range]
gamma_values = [greeks.gamma_numerical(s, K, r, sigma, T) for s in spot_range]
vega_values = [greeks.vega_numerical(S0, K, r, s, T)/100 for s in sigma_range]
theta_values = [greeks.theta_numerical(S0, K, r, sigma, t)/365 for t in t_range]
rho_values = [greeks.rho_numerical(S0, K, r, sigma, T)/100 for r in r_range]
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
axes[0].plot(spot_range, delta_values)
axes[0].set_title("Delta")
axes[0].axvline(S0, color='red', linestyle='--')
axes[0].set_xlabel("Spot Price")
axes[1].plot(spot_range, gamma_values)
axes[1].set_title("Gamma")
axes[1].axvline(S0, color='red', linestyle='--')
axes[1].set_xlabel("Spot Price")
axes[2].plot(sigma_range, vega_values)
axes[2].set_title("Vega")
axes[2].axvline(sigma, color='red', linestyle='--')
axes[2].set_xlabel("Volatility")
axes[3].plot(t_range, theta_values)
axes[3].set_title("Theta")
axes[3].axvline(T, color='red', linestyle='--')
axes[3].set_xlabel("Time to Maturity")
axes[4].plot(r_range, rho_values)
axes[4].set_title("Rho")
axes[4].axvline(r, color='red', linestyle='--')
axes[4].set_xlabel("Risk-Free Rate")

st.pyplot(fig)