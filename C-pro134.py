import pandas as pd
import matplotlib.pyplot as plt

# Import the data from the csv file
data = pd.read_csv("final_dataset.csv")

# Filter the data to keep only the stars with distance <= 100 light years
data = data[data["distance"] <= 100]

# Filter the data to keep only the stars with gravity in range of 150 to 350
data = data[(data["gravity"] >= 150) & (data["gravity"] <= 350)]

# Create a new csv file
data.to_csv("filtered_dataset.csv", index=False)
