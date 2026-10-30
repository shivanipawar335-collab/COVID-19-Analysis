
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("COVID-19 ANALYSIS PROJECT")

# Load Dataset
df = pd.read_csv("owid-covid-data.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nAvailable Columns:")
print(df.columns.tolist())

# Check required columns
required = ["location", "date", "total_cases", "total_deaths",
            "new_cases", "new_deaths"]

if all(col in df.columns for col in required):

    df = df[required].copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Handle missing values
    for col in ["total_cases", "total_deaths",
                "new_cases", "new_deaths"]:
        df[col] = df[col].fillna(0)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nTotal Cases:")
    print(df["total_cases"].max())

    print("\nTotal Deaths:")
    print(df["total_deaths"].max())

    # Top 10 Countries
    country_data = df.groupby("location")["total_cases"].max()
    country_data = country_data.sort_values(ascending=False)

    print("\nTop 10 Countries:")
    print(country_data.head(10))

    # Save Cleaned Data
    df.to_csv("cleaned_covid_data.csv", index=False)

    # Graph
    country_data.head(10).plot(kind="bar", figsize=(10,5))
    plt.title("Top 10 Countries COVID Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.tight_layout()
    plt.savefig("top_10_countries.png")
    plt.show()

    print("\nPROJECT COMPLETED SUCCESSFULLY!")

else:
    print("\nRequired columns are missing!")
    print("Please check the Available Columns above.")

    print("\nALL COLUMN NAMES:")
print(df.columns.tolist())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("COVID-19 ANALYSIS PROJECT")

# Load Dataset
df = pd.read_csv("owid-covid-data.csv")

# Clean Column Names
df.columns = df.columns.str.strip()

# Dataset Information
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicate Rows
df = df.drop_duplicates()

# Handle Missing Values
for col in ["Cases", "Recovered", "Deaths", "Tests"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Total Analysis
print("\nTotal COVID Cases:")
print(df["Cases"].sum())

print("\nTotal Recovered:")
print(df["Recovered"].sum())

print("\nTotal Deaths:")
print(df["Deaths"].sum())

print("\nTotal Tests:")
print(df["Tests"].sum())

# Country Wise Analysis
country_data = df.groupby("country")["Cases"].max()
country_data = country_data.sort_values(ascending=False)

print("\nTop 10 Countries:")
print(country_data.head(10))

# Save Cleaned Dataset
df.to_csv("cleaned_covid_data.csv", index=False)

# Create Graph
country_data.head(10).plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Countries COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Cases")
plt.tight_layout()

plt.savefig("top_10_countries.png")
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")

# Country Wise Analysis

country_analysis = df.groupby("country")[
    ["Cases", "Recovered", "Deaths"]
].max()

print("\nCountry Wise COVID Analysis:")
print(country_analysis.head(10))

# Save Country Analysis
country_analysis.to_csv("country_wise_analysis.csv")

print("\nCountry Analysis Saved Successfully!")

country_analysis = df.groupby("country")[["Cases", "Recovered", "Deaths"]].max()

country_analysis.to_csv("country_wise_analysis.csv")

print("Country Wise Analysis Saved Successfully!")

country_analysis = df.groupby("country")[["Cases", "Recovered", "Deaths"]].max()

country_analysis.to_csv("country_wise_analysis.csv", index=True)

print("File Saved Successfully!")
print("File Location:")
import os
print(os.getcwd())
print(os.path.exists("country_wise_analysis.csv"))

# COVID-19 Deaths Graph

death_data = df.groupby("country")["Deaths"].max()

death_data = death_data.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))

death_data.plot(kind="bar", color="red")

plt.title("Top 10 Countries COVID-19 Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")

plt.tight_layout()
plt.savefig("top_10_deaths.png")
plt.show()

print("Deaths Graph Created Successfully!")

# COVID-19 Recovered Graph

recovered_data = df.groupby("country")["Recovered"].max()

recovered_data = recovered_data.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))

recovered_data.plot(kind="bar", color="green")

plt.title("Top 10 Countries COVID-19 Recovered")
plt.xlabel("Country")
plt.ylabel("Recovered Cases")

plt.tight_layout()

plt.savefig("top_10_recovered.png")
plt.show()

print("Recovered Graph Created Successfully!")

# Monthly COVID Analysis

df["time"] = pd.to_datetime(df["time"], errors="coerce")

df["Month"] = df["time"].dt.month

monthly_data = df.groupby("Month")["Cases"].sum()

print("\nMonthly COVID Cases:")
print(monthly_data)

plt.figure(figsize=(10, 5))

monthly_data.plot(kind="line", marker="o")

plt.title("Monthly COVID-19 Cases")
plt.xlabel("Month")
plt.ylabel("Total Cases")

plt.tight_layout()

plt.savefig("monthly_covid_cases.png")
plt.show()

print("Monthly Analysis Completed!")
# Correlation Analysis

correlation = df[["Cases", "Recovered", "Deaths", "Tests"]].corr()

print("\nCorrelation Analysis:")
print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("COVID-19 Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.show()

print("Correlation Analysis Completed!")