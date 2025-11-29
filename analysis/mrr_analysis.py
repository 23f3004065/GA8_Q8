# Jules/Codex assisted analysis script
# Author: 23f3004065@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
import os

quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
mrr_growth = [7.71, 11.00, 11.89, 8.01]
benchmark = 15.0

avg_growth = sum(mrr_growth) / len(mrr_growth)
print(f"Computed average MRR growth: {avg_growth:.2f}%")

plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label="MRR Growth")
plt.axhline(benchmark, color="red", linestyle="--", label="Benchmark (15%)")
plt.axhline(avg_growth, color="green", linestyle=":", label=f"Average ({avg_growth:.2f}%)")
plt.title("MRR Growth 2024")
plt.xlabel("Quarter")
plt.ylabel("Growth (%)")
plt.legend()
plt.grid(True)

os.makedirs("visuals", exist_ok=True)
plt.savefig("visuals/mrr_growth_2024.png")
