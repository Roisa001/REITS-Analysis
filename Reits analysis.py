#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: robertisaksen
"""

# Import necessary libraries
import numpy as np

# Load the adjusted closings for SBRA using np.genfromtxt
sbra_data = np.genfromtxt('SBRA.csv', delimiter=',', skip_header=1)  # Skip the header row
sbra_adj_closings = sbra_data[:, 5]  # 'Adj Close' is at row 6 so index 5

# Load the adjusted closings for EQR using np.genfromtxt
eqr_data = np.genfromtxt('EQR.csv', delimiter=',', skip_header=1)  # Skip the header row
eqr_adj_closings = eqr_data[:, 5]  # ' 'Adj Close' is at row 6 so index 5


# Define the function for calculating the daily rate of return
def rate_of_return(adj_closings):
    # Use np.diff() to calculate the difference between consecutive values
    daily_simple_ror = np.diff(adj_closings) / adj_closings[:-1]
    
    # Return the daily simple rate of return
    return daily_simple_ror

# Calculate daily rate of return for SBRA and EQR
sbra_daily_ror = rate_of_return(sbra_adj_closings)
eqr_daily_ror = rate_of_return(eqr_adj_closings)



# Calculate Average Daily Return for SBRA
average_daily_return_sbra = np.mean(sbra_daily_ror)

# Calculate Average Daily Return for EQR
average_daily_return_eqr = np.mean(eqr_daily_ror)


# Compare the results
if average_daily_return_sbra > average_daily_return_eqr:
    print("SBRA has a higher average daily return.")
elif average_daily_return_sbra < average_daily_return_eqr:
    print("EQR has a higher average daily return.")
else:
    print("Average daily return is the same for both SBRA and EQR.")


# Define the function for calculating the daily log returns
def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns

# Calculate daily log returns for SBRA and EQR
daily_log_returns_sbra = log_returns(sbra_adj_closings)
daily_log_returns_eqr = log_returns(eqr_adj_closings)


# Define the function for calculating the annualized daily log return
def annualize_log_return(daily_log_returns):
    average_daily_log_returns = np.mean(daily_log_returns)
    annualized_log_return = average_daily_log_returns * 252 #252 trading days in a year and not 365
    return annualized_log_return

# Calculate annualized daily log return for SBRA and EQR
annualized_log_return_sbra = annualize_log_return(daily_log_returns_sbra)
annualized_log_return_eqr = annualize_log_return(daily_log_returns_eqr)


# Compare the results
if annualized_log_return_sbra > annualized_log_return_eqr:
    print("SBRA has a higher annualized daily log return.")
elif annualized_log_return_sbra < annualized_log_return_eqr:
    print("EQR has a higher annualized daily log return.")
else:
    print("Annualized daily log return is the same for both SBRA and EQR.")
    
    
# Calculate Variance of Daily Log Return for SBRA
daily_variance_sbra = np.var(daily_log_returns_sbra)

# Calculate Variance of Daily Log Return for EQR
daily_variance_eqr = np.var(daily_log_returns_eqr)


# Compare the results
if daily_variance_sbra > daily_variance_eqr:
    print("SBRA is riskier based on the variance of daily log return.")
elif daily_variance_sbra < daily_variance_eqr:
    print("EQR is riskier based on the variance of daily log return.")
else:
    print("The risk level is the same for both SBRA and EQR based on the variance of daily log return.")


# Calculate Daily Standard Deviation for SBRA
daily_sd_sbra = np.std(daily_log_returns_sbra)

# Calculate Daily Standard Deviation for EQR
daily_sd_eqr = np.std(daily_log_returns_eqr)


# Compare the results
if daily_sd_sbra > daily_sd_eqr:
    print("SBRA is riskier based on the daily standard deviation.")
elif daily_sd_sbra < daily_sd_eqr:
    print("EQR is riskier based on the daily standard deviation.")
else:
    print("The risk level is the same for both SBRA and EQR based on the daily standard deviation.")
    
    
# Calculate the Correlation between SBRA and EQR
corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra, daily_log_returns_eqr)[0, 1]

# Print the correlation result
print("Correlation between SBRA and EQR:", corr_sbra_eqr)

# Interpretation of Correlation
if corr_sbra_eqr > 0:
    print("There is a positive correlation between SBRA and EQR.")
elif corr_sbra_eqr < 0:
    print("There is a negative correlation between SBRA and EQR.")
else:
    print("There is no correlation between SBRA and EQR.")

# Explanation of Correlation Strength
if abs(corr_sbra_eqr) >= 0.7:       # Chose to use 0.7, 0.5 and under as the parameters, could be changed. 
    print("The correlation strength is strong.")
elif 0.5 <= abs(corr_sbra_eqr) < 0.7:
    print("The correlation strength is moderate.")
else:
    print("The correlation strength is weak.")
    

profitability_sbra = average_daily_return_sbra  # You may replace this with other profitability metrics
profitability_eqr = average_daily_return_eqr  # You may replace this with other profitability metrics

risk_sbra = daily_sd_sbra  # You may replace this with other risk metrics
risk_eqr = daily_sd_eqr  # You may replace this with other risk metrics

correlation_strength = abs(corr_sbra_eqr)

# Decision-making
if profitability_sbra > profitability_eqr and risk_sbra < risk_eqr:
    decision = "Invest in SBRA for higher profitability and lower risk."
elif profitability_sbra < profitability_eqr and risk_sbra > risk_eqr:
    decision = "Invest in EQR for higher profitability and lower risk."
elif correlation_strength < 0.5:
    decision = "Consider investing in both SBRA and EQR for diversification benefits."
else:
    decision = "Further analysis is recommended. Evaluate your investment goals and risk tolerance."

# Print the decision
print("Decision:", decision)


















