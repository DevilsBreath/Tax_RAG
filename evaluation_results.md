# TaxGPT India RAG Pipeline Evaluation Results

## Overall Metrics
- **Average Semantic Similarity:** 0.5106
- **Average ROUGE-L:** 0.1694
- **Average Grounded Precision:** 0.3766

## Detailed Breakdown
### Q1: What is the standard deduction limit for salaried employees under the new tax regime (Section 115BAC) for FY 2025-26?
- **Expected:** Under the new tax regime, the standard deduction for salaried employees and pensioners is ₹75,000 for FY 2025-26.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4459 | **ROUGE-L:** 0.1333 | **Precision:** 0.3333

### Q2: Who can file ITR-1 (Sahaj)?
- **Expected:** ITR-1 (Sahaj) can be filed by a resident individual having total income up to ₹50 lakh, having income from salaries, one house property, other sources (like interest), and agricultural income up to ₹5,000.
- **Generated:** According to the provided tax rules, ITR-1 (Sahaj) can be filed by individuals who are resident (other than not ordinarily resident) and have a total income up to Rs. 50 lakh. This includes individuals having income from salaries, income from house property, other sources (such as interest), and long-term capital gains under section 112A up to Rs. 50 lakh. [Source 3]
- **Similarity:** 0.888 | **ROUGE-L:** 0.551 | **Precision:** 0.64

### Q3: What is the TDS rate for fees for professional or technical services under section 194J?
- **Expected:** The TDS rate under section 194J is 2% for fees for technical services (not being a professional service) or royalty in nature of sale/distribution/exhibition of cinematographic films, and 10% for other professional services.
- **Generated:** According to the TDS rate chart provided in [Source 1], the TDS rate for fees - technical services, call centre, royalty, distribution, etc., under section 194J is 2%. [Source 1 | TDS_and_TCS-rate-chart-2026.pdf (Page 2)]
- **Similarity:** 0.822 | **ROUGE-L:** 0.274 | **Precision:** 0.5

### Q4: Are long-term capital gains on equity shares exempt from tax?
- **Expected:** No, long-term capital gains on listed equity shares are taxable under section 112A at 10% (or 12.5% per recent amendments) on gains exceeding ₹1 lakh (or ₹1.25 lakh per recent amendments) in a financial year, without indexation benefit.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | Source 2 | Source 3 | Source 4]
- **Similarity:** 0.3569 | **ROUGE-L:** 0.0678 | **Precision:** 0.1875

### Q5: What is the maximum deduction allowed under section 80C of the Income Tax Act?
- **Expected:** The maximum deduction allowed under section 80C for investments in PPF, LIC, ELSS, etc., is ₹1,50,000 in a financial year. This is only available under the old tax regime.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3511 | **ROUGE-L:** 0.0976 | **Precision:** 0.2222

### Q6: Is Health and Education Cess applicable on income tax?
- **Expected:** Yes, Health and Education Cess is levied at the rate of 4% on the amount of income-tax and surcharge.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4404 | **ROUGE-L:** 0.2 | **Precision:** 0.2222

### Q7: Can an NRI file ITR-1?
- **Expected:** No, Non-Resident Indians (NRIs) and Resident but Not Ordinarily Residents (RNORs) cannot file ITR-1. They must use ITR-2 or ITR-3.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.2735 | **ROUGE-L:** 0.0 | **Precision:** 0.2222

### Q8: What is the threshold limit for GST registration for a service provider?
- **Expected:** The general threshold limit for GST registration for service providers is an aggregate turnover of ₹20 lakh in a financial year (₹10 lakh for special category states).
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.2419 | **ROUGE-L:** 0.1081 | **Precision:** 0.3333

### Q9: What is the difference between CGST and SGST?
- **Expected:** CGST (Central GST) is levied by the Central Government, and SGST (State GST) is levied by the State Government on intra-state supplies of goods and services.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.1255 | **ROUGE-L:** 0.0541 | **Precision:** 0.3333

### Q10: Under which section of the CGST Act is the input tax credit (ITC) claimed?
- **Expected:** Input Tax Credit (ITC) is claimed under Section 16 of the CGST Act, 2017, subject to the conditions specified therein.
- **Generated:** The input tax credit (ITC) is claimed under Section 42 of the CGST Act. [Source 3]
- **Similarity:** 0.929 | **ROUGE-L:** 0.6667 | **Precision:** 0.6

### Q11: Is the new tax regime the default regime for FY 2025-26?
- **Expected:** Yes, the new tax regime under section 115BAC is the default tax regime. Taxpayers wishing to use the old regime must explicitly opt for it.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | Source 2]
- **Similarity:** 0.519 | **ROUGE-L:** 0.1026 | **Precision:** 0.2857

### Q12: What is the tax rate for income between ₹8 lakh and ₹12 lakh under the new tax regime?
- **Expected:** Under the new tax regime, the tax rate for income between ₹8 lakh and ₹12 lakh is 10%.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | ITR-2-2026-Eng.pdf (Page 2)] and [Source 2 | The-Income-tax-Act-2025.pdf (Page 403)] provide details about tax rates for specific types of income and benefits, but do not specify the tax rate for income between ₹8 lakh and ₹12 lakh under the new tax regime. [Source 3 | implementation_of_budget_2025_26.pdf (Page 67)] and [Source 4 | The-Income-tax-Act-2025.pdf (Page 215)] discuss tax reforms and rates for certain types of income, but do not provide the specific rate for income between ₹8 lakh and ₹12 lakh.
- **Similarity:** 0.7966 | **ROUGE-L:** 0.254 | **Precision:** 0.3529

### Q13: What is Form 3CD?
- **Expected:** Form 3CD is a statement of particulars required to be furnished under Section 44AB of the Income Tax Act. It is part of the tax audit report prepared by a Chartered Accountant.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3065 | **ROUGE-L:** 0.0952 | **Precision:** 0.2222

### Q14: Can a person with business income opt in and out of the new tax regime every year?
- **Expected:** No, a person having business or professional income can opt out of the new tax regime only once. Once they revert to the old regime, they cannot opt back into the new regime for that business, except in certain specific circumstances.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | ITR-3-2026-Eng.pdf (Page 2)] indicates that the default regime under section 115BAC(1A) is the 'new regime'. However, the 'old regime' can be chosen by opting out of the new regime under section 115BAC(6) by filing form 10IEA, which should be exercised on or before the due date for furnishing the return of income under section 139(1). The document does not explicitly state whether a person can opt in and out of the new tax regime every year. [Source 2 | The-Income-tax-Act-2025.pdf (Page 487)] and [Source 3 | The-Income-tax-Act-2025.pdf (Page 224)] do not provide information on annual opt-in/out options for the new tax regime. Therefore, based on the provided information, we cannot definitively answer the question.
- **Similarity:** 0.634 | **ROUGE-L:** 0.163 | **Precision:** 0.4881

### Q15: What is the due date for filing ITR for individuals not subject to tax audit?
- **Expected:** The due date for filing the Income Tax Return for individuals whose accounts are not required to be audited is generally July 31st of the assessment year.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | Source 2 | Source 3 | Source 4]
- **Similarity:** 0.3294 | **ROUGE-L:** 0.0889 | **Precision:** 0.1875

### Q16: Is rent received from a house property fully taxable?
- **Expected:** No, from the gross annual value (rent received/receivable), municipal taxes paid are deducted to arrive at the Net Annual Value (NAV). From NAV, a standard deduction of 30% is allowed under section 24(a), plus deduction for interest on borrowed capital under section 24(b).
- **Generated:** Based on the provided legal context, rent received from a house property is deemed to be income from house property and is included in the total income of the assessee under the head "Income from house property." However, a deduction of 30% of the arrears of rent or unrealised rent is allowed. Therefore, while rent is fully taxable, a portion of it can be deducted. [Source 2, Source 3, Source 4]
- **Similarity:** 0.6531 | **ROUGE-L:** 0.2393 | **Precision:** 0.5532

### Q17: What is the threshold for deducting TDS on rent under section 194-I?
- **Expected:** TDS on rent under section 194-I must be deducted if the total rent paid or payable during the financial year exceeds ₹2,40,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3914 | **ROUGE-L:** 0.1143 | **Precision:** 0.2222

### Q18: What is IGST and when is it applicable?
- **Expected:** IGST stands for Integrated Goods and Services Tax. It is levied by the Central Government on all inter-state supplies of goods and services, as well as on imports and exports.
- **Generated:** IGST, or Integrated Goods and Services Tax, is a tax levied on the value of goods and services plus specified customs duties. It is applicable in cases where the supplier and recipient are located in different states or UTs. According to the CGST Rules 2017, IGST is levied on imports made by a recipient (GSTIN) in a month for which FORM GSTR-2B is being generated. The ICEGATE reference date is the date from which the recipient is eligible to take input tax credit. [Source 3]
- **Similarity:** 0.8719 | **ROUGE-L:** 0.2564 | **Precision:** 0.7241

### Q19: What are the components of the composition scheme under GST?
- **Expected:** Under the composition scheme, eligible taxpayers with a turnover up to ₹1.5 crore can pay a flat percentage of their turnover (e.g., 1% for traders, 5% for restaurants, 6% for service providers) instead of regular GST. They cannot claim input tax credit.
- **Generated:** The composition scheme under GST includes the following components:

1. **Intimation to Pay Tax**: This is provided through various forms such as FORM GST CMP-01, FORM GST CMP-02, and FORM GST CMP-04. These forms are used to inform the tax authorities about the intention to pay tax under the composition scheme. [Source 1 | CGST-Rules-2017-Part-B-Forms.pdf (Page 8)]

2. **Intimation/Application for Withdrawal from Composition Levy**: This form is used to withdraw from the composition scheme. [Source 1 | CGST-Rules-2017-Part-B-Forms.pdf (Page 11)]

3. **Intimation to Pay Tax under Section 10 (Composition Levy)**: This is applicable to registered persons who have opted out of the composition scheme during the current financial year. Their turnover, which includes both composition taxpayer and normal taxpayer turnover, needs to be declared. [Source 1 | CGST-Rules-2017-Part-B-Forms.pdf (Page 8)]

4. **Category of Registered Person**: The category of registered person eligible for the composition scheme includes:
   - Manufacturers, other than manufacturers of such goods as may be notified by the Government.
   - Suppliers making supplies referred to in clause (b) of paragraph 6 of Schedule II.
   - Any other supplier eligible for composition levy. [Source 1 | CGST-Rules-2017-Part-B-Forms.pdf (Page 7)]

These components are essential for the registered persons to comply with the GST rules and regulations. [Source 1 | CGST-Rules-2017-
- **Similarity:** 0.6437 | **ROUGE-L:** 0.1087 | **Precision:** 0.5526

### Q20: How is agricultural income taxed in India?
- **Expected:** Agricultural income is exempt from income tax under Section 10(1) of the Income Tax Act. However, if the taxpayer has non-agricultural income exceeding the basic exemption limit, the agricultural income is included for rate purposes to calculate tax on the non-agricultural income.
- **Generated:** I don't know based on the provided tax documents. [Source 1 | Source 2] The provided legal context does not specifically address how agricultural income is taxed in India. It outlines definitions and sections of the Income-tax Act 2025 but does not provide details on agricultural income taxation. For accurate information on agricultural income taxation, you would need to refer to specific sections or rules related to agricultural income in the Income-tax Act 2025 or the Income-tax Rules 1962.
- **Similarity:** 0.6904 | **ROUGE-L:** 0.2835 | **Precision:** 0.2963

### Q21: Can I claim HRA and deduction for home loan interest simultaneously?
- **Expected:** Yes, under the old tax regime, you can claim House Rent Allowance (HRA) exemption and deduction for interest on a home loan under section 24(b) simultaneously, provided the rented house and the owned house are in different cities, or you can prove genuine reasons for renting despite owning a house in the same city.
- **Generated:** I don't know based on the provided tax documents. [Source 1, Source 2]
- **Similarity:** 0.2847 | **ROUGE-L:** 0.058 | **Precision:** 0.2308

### Q22: What is the penalty for late filing of Income Tax Return under section 234F?
- **Expected:** A fee of ₹5,000 is payable under section 234F if the return is furnished after the due date. However, if the total income does not exceed ₹5 lakh, the fee is restricted to ₹1,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3541 | **ROUGE-L:** 0.0435 | **Precision:** 0.4444

### Q23: Are cryptocurrency gains taxed in India?
- **Expected:** Yes, income from the transfer of any Virtual Digital Asset (VDA), including cryptocurrencies, is taxed at a flat rate of 30% under Section 115BBH, plus applicable surcharge and cess. No deductions or set-off of losses are allowed.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4857 | **ROUGE-L:** 0.0833 | **Precision:** 0.3333

### Q24: Who is required to obtain a Tax Deduction and Collection Account Number (TAN)?
- **Expected:** Any person who is responsible for deducting tax at source (TDS) or collecting tax at source (TCS) is required to obtain a 10-digit alphanumeric TAN under Section 203A of the Income Tax Act.
- **Generated:** According to the provided tax rules, both the deductor and the collector are required to obtain a Tax Deduction and Collection Account Number (TAN). Specifically, [Source 1] states that "The deductor at the time of preparing statements of tax deducted shall,— (i) quote his tax deduction and collection account number (TAN) in the statement." And [Source 2] states that "The collector at the time of preparing statements of tax collected shall,— (i) quote his tax deduction and collection account number (TAN) in the statement." Therefore, both the deductor and the collector are required to obtain a TAN.
- **Similarity:** 0.5985 | **ROUGE-L:** 0.1527 | **Precision:** 0.5952

### Q25: Can ITR-4 be used by a doctor?
- **Expected:** Yes, a doctor (medical professional) can use ITR-4 (Sugam) if they opt for the presumptive taxation scheme under section 44ADA and their gross receipts do not exceed the specified threshold (₹50 lakh or ₹75 lakh subject to cash receipt limits).
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3325 | **ROUGE-L:** 0.0392 | **Precision:** 0.3333

