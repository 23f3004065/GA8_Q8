import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Provided by Business Case ---
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Inventory_Turnover_Ratio': [5.44, 1.55, 7.09, 5.12]
}
df = pd.DataFrame(data)

# Target and Company Average (as stated in the prompt)
INDUSTRY_TARGET = 8.0
COMPANY_AVERAGE = 4.8
# The calculated average is 4.8 (5.44 + 1.55 + 7.09 + 5.12) / 4 = 4.8
calculated_average = df['Inventory_Turnover_Ratio'].mean() 
# We'll use the provided average of 4.8 in the story, but the calculated one confirms it.

# --- Data Visualization ---
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Create the bar plot for quarterly data
sns.barplot(
    x='Quarter', 
    y='Inventory_Turnover_Ratio', 
    data=df, 
    palette='viridis'
)

# Add a line for the Industry Target
plt.axhline(
    INDUSTRY_TARGET, 
    color='r', 
    linestyle='--', 
    linewidth=2, 
    label=f'Industry Target ({INDUSTRY_TARGET:.1f})'
)

# Add a line for the Company Average
plt.axhline(
    COMPANY_AVERAGE, 
    color='k', 
    linestyle='-', 
    linewidth=2, 
    label=f'Company Average ({COMPANY_AVERAGE:.1f})'
)

# Annotate each bar with its value
for index, row in df.iterrows():
    plt.text(
        index, 
        row['Inventory_Turnover_Ratio'] + 0.2, # Position above the bar
        f"{row['Inventory_Turnover_Ratio']:.2f}", 
        color='black', 
        ha="center"
    )

# --- Styling ---
plt.title(
    '2024 Quarterly Inventory Turnover Ratio Performance', 
    fontsize=16, 
    fontweight='bold'
)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Inventory Turnover Ratio', fontsize=12)
plt.ylim(0, INDUSTRY_TARGET + 1) # Set y-limit to clearly show the target line
plt.legend(loc='lower left')

# Save the visualization
plt.savefig('inventory_turnover_trend.png', dpi=300)
print("Analysis complete. Visualization saved as inventory_turnover_trend.png.")
print(f"Calculated Average: {calculated_average:.2f}. Company Average (for story): {COMPANY_AVERAGE:.1f}")