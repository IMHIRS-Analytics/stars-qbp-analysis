"""
Clover Insurance Co. v. HHS - MA Star Ratings Analysis
IMHIRS Analytics | Dawn Krysa, PA-C, MSHIIM, CHDA
github.com/IMHIRS-analytics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

# ── DATA ──────────────────────────────────────────────────────────────────────

measures = pd.DataFrame([
    {"measure": "Medication Adherence - Diabetes",         "part": "D", "weight": 3, "domain": "Outcomes",             "isnp_impact": True},
    {"measure": "Medication Adherence - Hypertension",     "part": "D", "weight": 3, "domain": "Outcomes",             "isnp_impact": True},
    {"measure": "Medication Adherence - Cholesterol",      "part": "D", "weight": 3, "domain": "Outcomes",             "isnp_impact": True},
    {"measure": "Controlling Blood Pressure",              "part": "C", "weight": 3, "domain": "Outcomes",             "isnp_impact": True},
    {"measure": "Blood Sugar Control - Diabetes",          "part": "C", "weight": 3, "domain": "Outcomes",             "isnp_impact": True},
    {"measure": "Statin Use - CVD (Part C)",               "part": "C", "weight": 2, "domain": "Intermediate Outcomes","isnp_impact": False},
    {"measure": "Statin Use - CVD (Part D)",               "part": "D", "weight": 2, "domain": "Intermediate Outcomes","isnp_impact": False},
    {"measure": "MTM CMR Completion Rate",                 "part": "D", "weight": 1, "domain": "Process",              "isnp_impact": True},
    {"measure": "Annual Flu Vaccine",                      "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": False},
    {"measure": "COA: Medication Review",                  "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": True},
    {"measure": "COA: Functional Status Assessment",       "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": True},
    {"measure": "COA: Pain Assessment",                    "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": True},
    {"measure": "Getting Needed Care",                     "part": "C", "weight": 2, "domain": "Access/Experience",    "isnp_impact": False},
    {"measure": "Getting Appointments Quickly",            "part": "C", "weight": 2, "domain": "Access/Experience",    "isnp_impact": False},
    {"measure": "Customer Service",                        "part": "C", "weight": 2, "domain": "Access/Experience",    "isnp_impact": False},
    {"measure": "Rating of Drug Plan",                     "part": "D", "weight": 2, "domain": "Access/Experience",    "isnp_impact": False},
    {"measure": "Rating of Health Plan",                   "part": "C", "weight": 2, "domain": "Access/Experience",    "isnp_impact": False},
    {"measure": "Breast Cancer Screening",                 "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": False},
    {"measure": "Colorectal Cancer Screening",             "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": False},
    {"measure": "Osteoporosis Management Post-Fracture",   "part": "C", "weight": 1, "domain": "Process",              "isnp_impact": False},
])

# ── SUMMARY STATS ─────────────────────────────────────────────────────────────

print("=" * 65)
print("CLOVER v. HHS — INVALIDATED MEASURE SUMMARY")
print("=" * 65)
print(f"Total measures invalidated:       {len(measures)}")
print(f"Total weight points removed:      {measures['weight'].sum()}")
print(f"Weight-3 measures (highest tier): {len(measures[measures['weight']==3])}")
print(f"I-SNP high-impact measures:       {measures['isnp_impact'].sum()}")
print()

print("BY DOMAIN:")
domain_summary = measures.groupby('domain').agg(
    count=('measure','count'),
    total_weight=('weight','sum'),
    isnp_count=('isnp_impact','sum')
).sort_values('total_weight', ascending=False)
print(domain_summary.to_string())
print()

print("BY PART:")
part_summary = measures.groupby('part').agg(
    count=('measure','count'),
    total_weight=('weight','sum')
)
print(part_summary.to_string())
print()

# ── QBP REVENUE MODELING ──────────────────────────────────────────────────────

plan_sizes = [1_000, 5_000, 10_000, 25_000, 50_000, 100_000]
benchmarks = {"Metropolitan": 950, "Rural": 1_100}
qbp_rate = 0.05  # 5% bonus for 4+ stars

print("QBP REVENUE AT RISK BY PLAN SIZE:")
print(f"{'Members':>12} {'Metro ($)':>14} {'Rural ($)':>14}")
print("-" * 44)
for size in plan_sizes:
    metro = size * benchmarks["Metropolitan"] * qbp_rate
    rural = size * benchmarks["Rural"] * qbp_rate
    print(f"{size:>12,} {metro:>14,.0f} {rural:>14,.0f}")
print()

# ── I-SNP SPECIFIC ANALYSIS ───────────────────────────────────────────────────

isnp_measures = measures[measures['isnp_impact']==True]
print("I-SNP HIGH-IMPACT MEASURES:")
print(f"  Count: {len(isnp_measures)}")
print(f"  Total weight: {isnp_measures['weight'].sum()}")
print(f"  Weight-3 measures: {len(isnp_measures[isnp_measures['weight']==3])}")
print()
for _, row in isnp_measures.iterrows():
    print(f"  [{row['part']}] W{row['weight']} - {row['measure']}")
print()

# ── VISUALIZATIONS ────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor('#f5f0e8')
gs = GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

colors = {
    'Outcomes': '#c8392b',
    'Intermediate Outcomes': '#1a4a7a',
    'Process': '#2d6a4f',
    'Access/Experience': '#b8860b'
}

# Plot 1: Weight distribution by domain
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor('#f5f0e8')
domain_wt = measures.groupby('domain')['weight'].sum()
bars = ax1.bar(range(len(domain_wt)), domain_wt.values,
               color=[colors[d] for d in domain_wt.index], edgecolor='#0d1117', linewidth=0.8)
ax1.set_xticks(range(len(domain_wt)))
ax1.set_xticklabels([d.replace('/', '/\n') for d in domain_wt.index], fontsize=8)
ax1.set_ylabel('Total Weight Points', fontsize=9)
ax1.set_title('Weight Points by Domain', fontsize=10, fontweight='bold', pad=8)
ax1.spines[['top','right']].set_visible(False)

# Plot 2: Part C vs D
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor('#f5f0e8')
part_counts = measures.groupby('part').agg(count=('measure','count'), weight=('weight','sum'))
x = np.arange(2)
w = 0.35
ax2.bar(x - w/2, part_counts['count'], w, label='Measures', color='#1a4a7a', edgecolor='#0d1117', linewidth=0.8)
ax2.bar(x + w/2, part_counts['weight'], w, label='Weight Points', color='#c8392b', edgecolor='#0d1117', linewidth=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(['Part C', 'Part D'])
ax2.set_title('Part C vs Part D', fontsize=10, fontweight='bold', pad=8)
ax2.legend(fontsize=8)
ax2.spines[['top','right']].set_visible(False)

# Plot 3: I-SNP impact pie
ax3 = fig.add_subplot(gs[0, 2])
ax3.set_facecolor('#f5f0e8')
isnp_ct = [measures['isnp_impact'].sum(), (~measures['isnp_impact']).sum()]
wedges, texts, autotexts = ax3.pie(
    isnp_ct, labels=['I-SNP\nHigh Impact', 'Standard'],
    colors=['#b8860b', '#d4cfc6'], autopct='%1.0f%%',
    startangle=90, wedgeprops={'edgecolor': '#0d1117', 'linewidth': 0.8}
)
ax3.set_title('I-SNP Impact Distribution', fontsize=10, fontweight='bold', pad=8)

# Plot 4: QBP revenue loss by plan size
ax4 = fig.add_subplot(gs[1, :2])
ax4.set_facecolor('#f5f0e8')
metro_losses = [s * 950 * 0.05 / 1e6 for s in plan_sizes]
rural_losses = [s * 1100 * 0.05 / 1e6 for s in plan_sizes]
ax4.plot(plan_sizes, metro_losses, 'o-', color='#1a4a7a', label='Metropolitan', linewidth=2, markersize=5)
ax4.plot(plan_sizes, rural_losses, 's--', color='#c8392b', label='Rural', linewidth=2, markersize=5)
ax4.set_xlabel('Plan Membership', fontsize=9)
ax4.set_ylabel('QBP Revenue at Risk ($M)', fontsize=9)
ax4.set_title('Annual QBP Revenue Exposure by Plan Size\n(Star Rating Drop Below 4.0 Threshold)', fontsize=10, fontweight='bold', pad=8)
ax4.legend(fontsize=9)
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
ax4.spines[['top','right']].set_visible(False)
ax4.grid(axis='y', alpha=0.3)

# Plot 5: Weight 3 measures detail
ax5 = fig.add_subplot(gs[1, 2])
ax5.set_facecolor('#f5f0e8')
w3 = measures[measures['weight']==3]
short_names = [m.replace('Medication Adherence - ', 'Adherence: ').replace('Blood Sugar Control - ', 'BG Control: ')
               for m in w3['measure']]
isnp_colors = ['#b8860b' if i else '#d4cfc6' for i in w3['isnp_impact']]
ax5.barh(range(len(w3)), w3['weight'], color=isnp_colors, edgecolor='#0d1117', linewidth=0.8)
ax5.set_yticks(range(len(w3)))
ax5.set_yticklabels(short_names, fontsize=8)
ax5.set_xlabel('Weight', fontsize=9)
ax5.set_title('Weight-3 Measures\n(Gold = I-SNP High Impact)', fontsize=10, fontweight='bold', pad=8)
ax5.spines[['top','right']].set_visible(False)

fig.suptitle('Clover Insurance Co. v. HHS — 20 Invalidated MA Star Rating Measures\nIMHIRS Analytics | github.com/IMHIRS-analytics',
             fontsize=12, fontweight='bold', y=1.01)

plt.savefig('stars_analysis.png', dpi=150, bbox_inches='tight', facecolor='#f5f0e8')
print("Visualization saved: stars_analysis.png")
plt.show()
