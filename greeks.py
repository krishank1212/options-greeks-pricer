import numpy as np
import scipy.stats as stats
import analytics

def delta_analytical(S0, K, r, sigma, T):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return stats.norm.cdf(d1)

def delta_numerical(S0, K, r, sigma, T, h=0.01):
    price_up = analytics.black_scholes(S0 + h, K, r, sigma, T)
    price_down = analytics.black_scholes(S0 - h, K, r, sigma, T)
    return (price_up - price_down) / (2 * h)

def gamma_numerical(S0, K, r, sigma, T, h=0.01):
    price_up = analytics.black_scholes(S0 + h, K, r, sigma, T)
    price_down = analytics.black_scholes(S0 - h, K, r, sigma, T)
    price_center = analytics.black_scholes(S0, K, r, sigma, T)
    return (price_up - 2 * price_center + price_down) / (h ** 2)

def vega_numerical(S0, K, r, sigma, T, h=0.001):
    price_up = analytics.black_scholes(S0, K, r, sigma + h, T)
    price_down = analytics.black_scholes(S0, K, r, sigma - h, T)
    return (price_up - price_down) / (2 * h)

def theta_numerical(S0, K, r, sigma, T, h=1/365):
    price_up = analytics.black_scholes(S0, K, r, sigma, T + h)
    price_down = analytics.black_scholes(S0, K, r, sigma, T - h)
    return -(price_up - price_down) / (2 * h)

def rho_numerical(S0, K, r, sigma, T, h=0.001):
    price_up = analytics.black_scholes(S0, K, r + h, sigma, T)
    price_down = analytics.black_scholes(S0, K, r - h, sigma, T)
    return (price_up - price_down) / (2 * h)