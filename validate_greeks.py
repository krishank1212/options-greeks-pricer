import greeks
def validate_greeks():
    S0 = [80, 90, 100, 110, 120]
    K = 100
    r = 0.03
    sigma = 0.2
    T = 1
    for s in S0:
        print(f"S0: {s}")
        print (f"Delta Analytical: {greeks.delta_analytical(s, K, r, sigma, T):.4f}")
        print (f"Delta Numerical: {greeks.delta_numerical(s, K, r, sigma, T):.4f}")
        print (f"Gamma Numerical: {greeks.gamma_numerical(s, K, r, sigma, T):.4f}")
        print (f"Vega Numerical: {greeks.vega_numerical(s, K, r, sigma, T):.4f}")
        print (f"Theta Numerical: {greeks.theta_numerical(s, K, r, sigma, T):.4f}")
        print (f"Rho Numerical: {greeks.rho_numerical(s, K, r, sigma, T):.4f}")
        
        
validate_greeks()