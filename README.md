# Clover Insurance Co. v. HHS — MA Star Ratings Invalidation Analysis

**IMHIRS Analytics | Dawn Krysa, PA-C, MSHIIM, CHDA**
`github.com/IMHIRS-analytics`

---

## Overview

On May 27, 2026, the U.S. District Court for the Northern District of Georgia ruled that CMS lacked statutory authority to include 20 of 42 Medicare Advantage Star Rating measures in plan performance calculations. The court ordered CMS to recalculate Clover Insurance Company's Star Rating without those measures. CMS filed for reconsideration the same day. The court denied it.

This repository contains:
- An interactive dashboard with a live QBP revenue loss calculator and filterable measure table
- Complete inventory and analysis of all 20 invalidated measures
- I-SNP population-specific impact assessment
- Python analysis script with financial modeling
- Legal and program integrity commentary

---

## Background: What the Star Ratings Program Does

Medicare Advantage plans receive Quality Bonus Payments (QBP) when they achieve 4.0 or more Stars. The QBP can represent 5% of benchmark payments, translating to hundreds of millions of dollars across larger plans. CMS calculates Stars across up to 40+ measures spanning outcomes, process, intermediate outcomes, and access/experience domains.

For Clover, losing QBP eligibility based on a rating that included now-invalidated measures represented an estimated $120 million annual exposure.

---

## The 20 Invalidated Measures

| # | Measure | Part | Weight | I-SNP Impact |
|---|---------|------|--------|--------------|
| 1 | Medication Adherence for Diabetes Medications | D | 3 | High |
| 2 | Medication Adherence for Hypertension (RAS Antagonists) | D | 3 | High |
| 3 | Medication Adherence for Cholesterol (Statins) | D | 3 | High |
| 4 | Controlling Blood Pressure | C | 3 | High |
| 5 | Blood Sugar Controlled for Patients with Diabetes | C | 3 | High |
| 6 | Statin Use in Persons with Cardiovascular Disease | C | 2 | Standard |
| 7 | Statin Therapy for Patients with CVD (Part D) | D | 2 | Standard |
| 8 | MTM Program Completion Rate for CMR | D | 1 | High |
| 9 | Annual Flu Vaccine | C | 1 | Standard |
| 10 | Care for Older Adults: Medication Review | C | 1 | High |
| 11 | Care for Older Adults: Functional Status Assessment | C | 1 | High |
| 12 | Care for Older Adults: Pain Assessment | C | 1 | High |
| 13 | Getting Needed Care | C | 2 | Standard |
| 14 | Getting Appointments and Care Quickly | C | 2 | Standard |
| 15 | Customer Service | C | 2 | Standard |
| 16 | Rating of Drug Plan | D | 2 | Standard |
| 17 | Rating of Health Plan | C | 2 | Standard |
| 18 | Breast Cancer Screening | C | 1 | Standard |
| 19 | Colorectal Cancer Screening | C | 1 | Standard |
| 20 | Osteoporosis Management in Women Who Had a Fracture | C | 1 | Standard |

**Total weight points removed: 40**
**Measures with Weight 3 (highest): 5**
**Measures with disproportionate I-SNP impact: 7**

---

## I-SNP Population Analysis

Institutional Special Needs Plans serve frail elderly members in long-term care settings, a population with fundamentally different clinical profiles than community-dwelling MA members. Seven of the 20 invalidated measures disproportionately burdened I-SNP plans.

**Medication adherence measures (Weight 3 each):** The three adherence measures assume community-based pharmacy access, intact cognition, and self-directed medication management. I-SNP members are managed in facility settings where adherence is a facility responsibility, not a patient-level variable. Penalizing I-SNP plans on these measures conflated facility-level dispensing systems with individual adherence behavior.

**Blood pressure and blood sugar control:** Tight glycemic and hypertensive control targets in frail elderly patients with multiple comorbidities are not evidence-based goals. Clinical guidelines (ACC/AHA, ADA) explicitly recommend relaxed targets in this population. Applying community benchmarks to I-SNP populations penalized clinically appropriate, guideline-concordant management decisions.

**Care for Older Adults trilogy:** Medication review, functional status assessment, and pain assessment are core I-SNP competencies. The invalidation of these measures removes meaningful differentiation between plans that serve complex populations well and those that do not, which is an unresolved tension in the ruling's practical effect.

---

## Legal Framework

**Statutory basis:** 42 U.S.C. § 1395w-23 governs MA Quality Bonus Payments. The court found CMS exceeded its authority under this section for the 20 measures, and that the agency's rulemaking process failed to satisfy the arbitrary and capricious standard under the Administrative Procedure Act (APA).

**Reconsideration denied:** CMS filed for reconsideration May 28, 2026. Denied.

**Market implications:**
- Every MA plan now has a reproducible legal theory for challenging measures where CMS authority is contestable
- Plans near the 4.0 Stars threshold have financial incentive to evaluate litigation options
- The 2027 MA bid deadline was June 1, four days after the ruling; bids submitted with pre-ruling QBP assumptions may require recalculation

**Program integrity angle:** Plans that received QBP bonuses based on inflated ratings derived from now-invalidated measures face potential retroactive exposure. The intersection of Stars methodology and bonus payment certifications under the False Claims Act warrants monitoring as this case develops on appeal or in parallel litigation.

---

## Financial Modeling

The `analysis/measure_analysis.py` script models:
- QBP revenue impact across plan sizes (1,000 to 100,000 members)
- Metropolitan vs. rural benchmark differences
- Per-member-per-month exposure by star rating tier
- I-SNP-specific measure weight analysis

Run requirements: Python 3.8+, pandas, matplotlib, numpy

```bash
pip install pandas matplotlib numpy
python analysis/measure_analysis.py
```

---

## About This Project

This analysis was built by Dawn Krysa, PA-C, MSHIIM, CHDA, a clinician-turned-health data analyst specializing in Medicare Advantage risk adjustment, HCC validation, and program integrity. I work inside an I-SNP population daily doing CDI and clinical validation. The seven measures flagged as high I-SNP impact are not abstractions to me: they are the patients on my charts.

This project is part of the IMHIRS Analytics portfolio at `github.com/IMHIRS-analytics`.

**Contact:** darbydawn7683@gmail.com | linkedin.com/in/dawn-krysa-b00160388

---

*Analysis current as of June 2026. Case citation: Clover Insurance Co. v. U.S. Department of Health and Human Services, N.D. Ga. (2026).*
