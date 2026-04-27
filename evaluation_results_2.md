# TaxGPT India RAG Pipeline Evaluation Results

## Overall Metrics
- **Average Semantic Similarity:** 0.8758
- **Average ROUGE-L:** 0.4282
- **Average Grounded Precision:** 0.7222

## Detailed Breakdown
### Q1: What is the standard deduction limit for salaried employees under the new tax regime (Section 115BAC) for FY 2025-26?
- **Expected:** Under the new tax regime, the standard deduction for salaried employees and pensioners is ₹75,000 for FY 2025-26.
- **Generated:** The standard deduction for salaried employees under the new tax regime (section 115BAC) for FY 2025-26 is rupees 75,000 [Source 4].
- **Similarity:** 0.9251 | **ROUGE-L:** 0.4651 | **Precision:** 0.8421

### Q2: Who can file ITR-1 (Sahaj)?
- **Expected:** ITR-1 (Sahaj) can be filed by a resident individual having total income up to ₹50 lakh, having income from salaries, one house property, other sources (like interest), and agricultural income up to ₹5,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.6142 | **ROUGE-L:** 0.0 | **Precision:** 0.4444

### Q3: What is the TDS rate for fees for professional or technical services under section 194J?
- **Expected:** The TDS rate under section 194J is 2% for fees for technical services (not being a professional service) or royalty in nature of sale/distribution/exhibition of cinematographic films, and 10% for other professional services.
- **Generated:** The TDS rates under section 194J for fees for professional or technical services are:

*   **2%** for fees for technical services (which are not professional services), call centre services, or royalty in the nature of sale, distribution, or exhibition of cinematographic films [Source 1 | knowledge_base.txt (Page 1)].
*   **10%** for all other professional services, such as doctors, lawyers, architects, and consultants [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.922 | **ROUGE-L:** 0.6019 | **Precision:** 0.7234

### Q4: Are long-term capital gains on equity shares exempt from tax?
- **Expected:** No, long-term capital gains on listed equity shares are taxable under section 112A at 10% (or 12.5% per recent amendments) on gains exceeding ₹1 lakh (or ₹1.25 lakh per recent amendments) in a financial year, without indexation benefit.
- **Generated:** No, long-term capital gains (LTCG) on equity shares are not exempt from tax [Source 2]. Specifically, LTCG on listed equity shares, units of equity-oriented mutual funds, and units of business trusts where Securities Transaction Tax (STT) is paid, are taxable under section 112A at 12.5% on gains exceeding rupees 1,25,000 in a financial year, and no indexation benefit is available [Source 2].
- **Similarity:** 0.8876 | **ROUGE-L:** 0.5185 | **Precision:** 0.9

### Q5: What is the maximum deduction allowed under section 80C of the Income Tax Act?
- **Expected:** The maximum deduction allowed under section 80C for investments in PPF, LIC, ELSS, etc., is ₹1,50,000 in a financial year. This is only available under the old tax regime.
- **Generated:** The maximum deduction allowed under section 80C of the Income Tax Act is rupees 1,50,000 per financial year [knowledge_base.txt (Page 1)]. This deduction is only available under the old tax regime and not under the new tax regime [knowledge_base.txt (Page 1)].
- **Similarity:** 0.8603 | **ROUGE-L:** 0.5641 | **Precision:** 0.8571

### Q6: Is Health and Education Cess applicable on income tax?
- **Expected:** Yes, Health and Education Cess is levied at the rate of 4% on the amount of income-tax and surcharge.
- **Generated:** Yes, Health and Education Cess is levied at a rate of 4% on the amount of income tax and surcharge for all categories of taxpayers [Source 1 | knowledge_base.txt (Page 1)]. It is also shown as Health and Education Cess @ 4% on (1a+1b) in tax computations [Source 3 | ITR-3-2026-Eng.pdf (Page 57)].
- **Similarity:** 0.9115 | **ROUGE-L:** 0.4935 | **Precision:** 0.7179

### Q7: Can an NRI file ITR-1?
- **Expected:** No, Non-Resident Indians (NRIs) and Resident but Not Ordinarily Residents (RNORs) cannot file ITR-1. They must use ITR-2 or ITR-3.
- **Generated:** No, Non-Resident Indians (NRIs) cannot file ITR-1 [Source 1 | knowledge_base.txt (Page 1)]. They must use either ITR-2 or ITR-3 [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9288 | **ROUGE-L:** 0.6071 | **Precision:** 0.55

### Q8: What is the threshold limit for GST registration for a service provider?
- **Expected:** The general threshold limit for GST registration for service providers is an aggregate turnover of ₹20 lakh in a financial year (₹10 lakh for special category states).
- **Generated:** The provided context mentions the GST registration threshold for suppliers of goods is ₹ 40 lakh aggregate turnover in most states (and ₹ 20 lakh for special category states) [Source 2]. However, the context does not specify the GST registration threshold limit for a service provider.
- **Similarity:** 0.8995 | **ROUGE-L:** 0.3662 | **Precision:** 0.6286

### Q9: What is the difference between CGST and SGST?
- **Expected:** CGST (Central GST) is levied by the Central Government, and SGST (State GST) is levied by the State Government on intra-state supplies of goods and services.
- **Generated:** CGST (Central Goods and Services Tax) is levied by the Central Government on intra-state supplies of goods and services [Source 3]. SGST (State Goods and Services Tax) is levied by the State Government on intra-state supplies of goods and services [Source 3]. CGST and SGST are always levied together on intra-state supplies, and their rates are equal [Source 3, Source 6].
- **Similarity:** 0.9507 | **ROUGE-L:** 0.5495 | **Precision:** 0.7742

### Q10: Under which section of the CGST Act is the input tax credit (ITC) claimed?
- **Expected:** Input Tax Credit (ITC) is claimed under Section 16 of the CGST Act, 2017, subject to the conditions specified therein.
- **Generated:** The input tax credit (ITC) can be claimed under sub-section (1) of section 18 [Source 4]. Specifically, FORM GST ITC-01 is used for the declaration of the claim of input tax credit under sub-section (1) of section 18 [Source 4].
- **Similarity:** 0.7963 | **ROUGE-L:** 0.3175 | **Precision:** 0.8

### Q11: Is the new tax regime the default regime for FY 2025-26?
- **Expected:** Yes, the new tax regime under section 115BAC is the default tax regime. Taxpayers wishing to use the old regime must explicitly opt for it.
- **Generated:** Yes, the new tax regime under section 115BAC is the default tax regime for FY 2025-26 [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9322 | **ROUGE-L:** 0.5714 | **Precision:** 0.6316

### Q12: What is the tax rate for income between ₹8 lakh and ₹12 lakh under the new tax regime?
- **Expected:** Under the new tax regime, the tax rate for income between ₹8 lakh and ₹12 lakh is 10%.
- **Generated:** Under the new tax regime for FY 2025-26:
*   Income between ₹8,00,001 and ₹10,00,000 is taxed at 10% [Source 1 | knowledge_base.txt (Page 1)].
*   Income between ₹10,00,001 and ₹12,00,000 is taxed at 15% [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.8327 | **ROUGE-L:** 0.3582 | **Precision:** 0.5556

### Q13: What is Form 3CD?
- **Expected:** Form 3CD is a statement of particulars required to be furnished under Section 44AB of the Income Tax Act. It is part of the tax audit report prepared by a Chartered Accountant.
- **Generated:** Form 3CD is a statement of particulars that must be furnished under section 44AB of the Income Tax Act, along with the audit report [Source 2 | knowledge_base.txt (Page 1)]. This form is prepared and certified by a Chartered Accountant (CA) as part of the Tax Audit report (Form 3CA or Form 3CB) [Source 2 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9705 | **ROUGE-L:** 0.5376 | **Precision:** 0.7619

### Q14: Can a person with business income opt in and out of the new tax regime every year?
- **Expected:** No, a person having business or professional income can opt out of the new tax regime only once. Once they revert to the old regime, they cannot opt back into the new regime for that business, except in certain specific circumstances.
- **Generated:** A person having business or professional income who opts out of the new tax regime can do so only ONCE [Source 1 | knowledge_base.txt (Page 1)]. Once they revert to the old regime, they cannot opt back into the new regime for subsequent years, except in the year when they have no business income [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9636 | **ROUGE-L:** 0.6602 | **Precision:** 0.8864

### Q15: What is the due date for filing ITR for individuals not subject to tax audit?
- **Expected:** The due date for filing the Income Tax Return for individuals whose accounts are not required to be audited is generally July 31st of the assessment year.
- **Generated:** The due date for filing the Income Tax Return (ITR) for individuals whose accounts are not required to be audited is July 31st of the assessment year (e.g., July 31, 2026 for AY 2026-27) [Source 1 | knowledge_base.txt (Page 1), Source 5 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9088 | **ROUGE-L:** 0.6753 | **Precision:** 0.7368

### Q16: Is rent received from a house property fully taxable?
- **Expected:** No, from the gross annual value (rent received/receivable), municipal taxes paid are deducted to arrive at the Net Annual Value (NAV). From NAV, a standard deduction of 30% is allowed under section 24(a), plus deduction for interest on borrowed capital under section 24(b).
- **Generated:** Rent received from a house property is NOT fully taxable because deductions are allowed under section 24 [Source 1 | knowledge_base.txt (Page 1), Source 2 | knowledge_base.txt (Page 1)].

Specifically, the following deductions are allowed:
*   Municipal taxes actually paid by the owner are deducted from the gross annual value (rent received or receivable) to arrive at the Net Annual Value (NAV) [Source 1 | knowledge_base.txt (Page 1)].
*   A standard deduction of 30% of NAV is allowed under section 24(a) [Source 1 | knowledge_base.txt (Page 1)].
*   Interest on borrowed capital (home loan) is allowed under section 24(b) [Source 1 | knowledge_base.txt (Page 1), Source 2 | knowledge_base.txt (Page 1)].

Additionally, the annual value of the property consisting of a house or any part thereof shall be taken as nil if the owner occupies it for their own residence or cannot actually occupy it due to any reason [Source 8 | The-Income-tax-Act-2025.pdf (Page 47)].
- **Similarity:** 0.8796 | **ROUGE-L:** 0.3333 | **Precision:** 0.7674

### Q17: What is the threshold for deducting TDS on rent under section 194-I?
- **Expected:** TDS on rent under section 194-I must be deducted if the total rent paid or payable during the financial year exceeds ₹2,40,000.
- **Generated:** The threshold for deducting TDS under section 194-I is when the total rent paid or payable during the financial year exceeds rupees 2,40,000 [Source 1 | knowledge_base.txt (Page 1)]. Additionally, TDS on rent under section 194-I must be deducted if the total rent paid or payable during the financial year exceeds rupees 2,40,000 [Source 2 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9272 | **ROUGE-L:** 0.5435 | **Precision:** 0.7647

### Q18: What is IGST and when is it applicable?
- **Expected:** IGST stands for Integrated Goods and Services Tax. It is levied by the Central Government on all inter-state supplies of goods and services, as well as on imports and exports.
- **Generated:** IGST is levied on the value plus specified customs duties in the case of imports [Source 1].

Additionally, the following points relate to IGST:
*   For supplies that are intra-state, IGST should be reported, or CGST & SGST/UTGST should be reported [Source 5].
*   Place of Supply (POS) details are required only if the demand is created under the IGST Act [Source 3].
*   For imports, the GSTIN of the recipient taxpayer is used [Source 1].
*   In cases of imports or supplies received under the reverse charge mechanism, the GSTIN of the supplier is considered to be the GSTIN of the applicant (recipient) [Source 6].
- **Similarity:** 0.7929 | **ROUGE-L:** 0.1194 | **Precision:** 0.7188

### Q19: What are the components of the composition scheme under GST?
- **Expected:** Under the composition scheme, eligible taxpayers with a turnover up to ₹1.5 crore can pay a flat percentage of their turnover (e.g., 1% for traders, 5% for restaurants, 6% for service providers) instead of regular GST. They cannot claim input tax credit.
- **Generated:** The Composition Scheme, under section 10 of the CGST Act, allows eligible taxpayers with an aggregate turnover up to rupees 1.5 crore to pay a flat percentage of their turnover as tax instead of regular GST [Source 1 | knowledge_base.txt (Page 1)].

The flat percentages vary based on the type of business:
*   **Manufacturers and traders:** 1% (which is 0.5% CGST + 0.5% SGST) [Source 1 | knowledge_base.txt (Page 1)].
*   **Restaurants not serving alcohol:** 5% (which is 2.5% CGST + 2.5% SGST) [Source 1 | knowledge_base.txt (Page 1)].
*   **Other eligible service providers:** 6% (which is 3% CGST + 3% SGST) for turnover up to rupees 50 lakh [Source 1 | knowledge_base.txt (Page 1)].

Businesses opting for the Composition Scheme have certain restrictions, including:
*   They cannot claim Input Tax Credit (ITC) [Source 1 | knowledge_base.txt (Page 1)].
*   They cannot collect GST from customers [Source 1 | knowledge_base.txt (Page 1)].
*   They cannot make inter-state supplies [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.8821 | **ROUGE-L:** 0.2925 | **Precision:** 0.686

### Q20: How is agricultural income taxed in India?
- **Expected:** Agricultural income is exempt from income tax under Section 10(1) of the Income Tax Act. However, if the taxpayer has non-agricultural income exceeding the basic exemption limit, the agricultural income is included for rate purposes to calculate tax on the non-agricultural income.
- **Generated:** The provided documents detail how agricultural income is treated in the Income Tax Returns (ITR-3 and ITR-2), indicating that it is categorized under "EXEMPT INCOME" and is "not to be included in Total Income or not chargeable to tax" [Source 1 | ITR-3-2026-Eng.pdf (Page 49), Source 2 | ITR-2-2026-Eng.pdf (Page 24)].

The calculation for agricultural income differs slightly between the forms:

*   **In ITR-3:** Net Agricultural income is calculated as (Gross Agricultural receipts - Expenditure incurred on agriculture - Unabsorbed agricultural loss of previous eight assessment years + Agricultural income portion relating to Rule 7, 7A, 7B(1), 7B(1A) and 8) [Source 1 | ITR-3-2026-Eng.pdf (Page 49)].
*   **In ITR-2:** Net Agricultural income is calculated as (Gross Agricultural receipts - Expenditure incurred on agriculture - Unabsorbed agricultural loss of previous eight assessment years) [Source 2 | ITR-2-2026-Eng.pdf (Page 24)].

In both forms, if the net agricultural income for the year exceeds Rs. 5 lakh, specific details regarding the agricultural land must be furnished [Source 1 | ITR-3-2026-Eng.pdf (Page 49), Source 2 | ITR-2-2026-Eng.pdf (Page 24)].

For ITR-3, if the net agricultural income exceeds Rs. 5 lakh, you must provide:
*   The name of the district along with the pin code where the land is located [Source 1 | ITR-3-2026-Eng.pdf (Page 49)].
*   The measurement of the agricultural land in Acres [Source 1 | ITR-3-2026-Eng.pdf (Page 49)].

For ITR-2, if the net agricultural income exceeds Rs. 5 lakh, you must provide:
*   The name of the district along with the pin code where the land is located [Source 2 | ITR-2-2026-Eng.pdf (Page 24)].
*   The measurement of
- **Similarity:** 0.7892 | **ROUGE-L:** 0.1317 | **Precision:** 0.5327

### Q21: Can I claim HRA and deduction for home loan interest simultaneously?
- **Expected:** Yes, under the old tax regime, you can claim House Rent Allowance (HRA) exemption and deduction for interest on a home loan under section 24(b) simultaneously, provided the rented house and the owned house are in different cities, or you can prove genuine reasons for renting despite owning a house in the same city.
- **Generated:** Yes, House Rent Allowance (HRA) exemption under section 10(13A) can be claimed simultaneously with the home loan interest deduction under section 24(b), provided there is a genuine reason for renting, such as the owned and rented properties being in different cities [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9464 | **ROUGE-L:** 0.381 | **Precision:** 0.7955

### Q22: What is the penalty for late filing of Income Tax Return under section 234F?
- **Expected:** A fee of ₹5,000 is payable under section 234F if the return is furnished after the due date. However, if the total income does not exceed ₹5 lakh, the fee is restricted to ₹1,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.5904 | **ROUGE-L:** 0.0435 | **Precision:** 0.6667

### Q23: Are cryptocurrency gains taxed in India?
- **Expected:** Yes, income from the transfer of any Virtual Digital Asset (VDA), including cryptocurrencies, is taxed at a flat rate of 30% under Section 115BBH, plus applicable surcharge and cess. No deductions or set-off of losses are allowed.
- **Generated:** Yes, income from the transfer of Virtual Digital Assets (VDA), which includes cryptocurrencies, is taxable in India [Source 1 | knowledge_base.txt (Page 1)]. This income is taxed at a flat rate of 30% under section 115BBH, in addition to any applicable surcharge and Health and Education Cess [Source 1 | knowledge_base.txt (Page 1)]. When reporting this income, it can be classified under either the head "Business" or "Capital Gain" [Source 3 | ITR-3-2026-Eng.pdf (Page 49)].

Key points regarding the taxation of VDA income:
*   No deduction is allowed other than the cost of acquisition [Source 1 | knowledge_base.txt (Page 1)].
*   No set-off of losses from VDAs against any other income is permitted [Source 1 | knowledge_base.txt (Page 1)].
*   For the purpose of tax, "transfer" as defined in section 2(109) applies to any virtual digital asset, whether it is a capital asset or not [Source 5 | The-Income-tax-Act-2025.pdf (Page 220)].

The Income Tax Return form includes a Schedule for VDA Income, where details of every transaction must be filled, noting the Date of Acquisition, Date of Transfer, Head under which income is to be taxed (Business/Capital Gain), Cost of Acquisition, Consideration Received, and the Income from transfer (Consideration Received minus Cost of Acquisition) [Source 4 | ITR-3-2026-Eng.pdf (Page 35)].
- **Similarity:** 0.9255 | **ROUGE-L:** 0.2519 | **Precision:** 0.5897

### Q24: Who is required to obtain a Tax Deduction and Collection Account Number (TAN)?
- **Expected:** Any person who is responsible for deducting tax at source (TDS) or collecting tax at source (TCS) is required to obtain a 10-digit alphanumeric TAN under Section 203A of the Income Tax Act.
- **Generated:** Every person who is responsible for deducting tax at source (TDS) or collecting tax at source (TCS) is required to obtain a Tax Deduction and Collection Account Number (TAN) [Source 3].
- **Similarity:** 0.9214 | **ROUGE-L:** 0.6769 | **Precision:** 0.9231

### Q25: Can ITR-4 be used by a doctor?
- **Expected:** Yes, a doctor (medical professional) can use ITR-4 (Sugam) if they opt for the presumptive taxation scheme under section 44ADA and their gross receipts do not exceed the specified threshold (₹50 lakh or ₹75 lakh subject to cash receipt limits).
- **Generated:** Yes, a doctor or medical professional can use ITR-4 if they opt for the presumptive taxation scheme under section 44ADA and their gross receipts do not exceed rupees 75 lakh (provided at least 95% of receipts are through banking channels; otherwise, the limit is rupees 50 lakh) [Source 1 | knowledge_base.txt (Page 1)].
- **Similarity:** 0.9372 | **ROUGE-L:** 0.6458 | **Precision:** 0.8

