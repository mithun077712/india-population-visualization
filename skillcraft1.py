import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\DELL\Downloads\1.1 - India_Historical_Population_Density_Data.csv"
data = pd.read_csv(file_path)


print("Dataset Columns:", data.columns)
print(data.head())


data.rename(columns={'year': 'Year', 'Population_Density': 'Density'}, inplace=True)


plt.figure(figsize=(12,7))
ax1 = plt.gca()


if 'Population' in data.columns:
    ax1.bar(data['Year'], data['Population'], color='skyblue', label='Population', alpha=0.7)
    ax1.set_ylabel("Population", color='skyblue')
else:
    ax1.bar(data['Year'], data['Density'], color='lightblue', label='Density', alpha=0.7)
    ax1.set_ylabel("Density (people per sq km)", color='lightblue')


ax2 = ax1.twinx()
ax2.plot(data['Year'], data['Density'], marker='o', color='orange', linewidth=2, label='Density')
ax2.set_ylabel("Population Density (people per sq km)", color='orange')


plt.title("India's Population and Density Over the Years", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year")
ax1.grid(axis='y', linestyle='--', alpha=0.6)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

if 'Population' in data.columns:
    plt.figure(figsize=(10,6))
    plt.bar(data['Year'], data['Population'], color='deepskyblue', alpha=0.8)
    plt.title("India's Population Growth Over the Years", fontsize=14, fontweight='bold')
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()


plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Density'], marker='o', color='seagreen', linewidth=2)
plt.title("India's Population Density Over the Years", fontsize=14, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Population Density (people per sq km)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
