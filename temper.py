import pandas as pd
import numpy as np
import statistics as st
import csv

# Load the CSV file
df = pd.read_csv('CorrNCov.csv')

# Select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Calculate correlation coefficient
correlation_coefficient = df[numeric_cols].corr()

# Calculate covariance
covariance = df[numeric_cols].cov()

# Print the results
print("Correlation Coefficient:")
print(correlation_coefficient)
print("\nCovariance:")
print(covariance)

# Save the results to a new CSV file
correlation_coefficient.to_csv('correlation_coefficient.csv', index=True)
covariance.to_csv('covariance.csv', index=True)