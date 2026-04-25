# TaxGPT India RAG Pipeline Evaluation Results

## Overall Metrics
- **Average Semantic Similarity:** 0.5571
- **Average ROUGE-L:** 0.1662
- **Average Grounded Precision:** 0.5432

## Detailed Breakdown
### Q1: What is the standard deduction limit for salaried employees under the new tax regime (Section 115BAC) for FY 2025-26?
- **Expected:** Under the new tax regime, the standard deduction for salaried employees and pensioners is ₹75,000 for FY 2025-26.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4459 | **ROUGE-L:** 0.1333 | **Precision:** 0.3333

### Q2: Who can file ITR-1 (Sahaj)?
- **Expected:** ITR-1 (Sahaj) can be filed by a resident individual having total income up to ₹50 lakh, having income from salaries, one house property, other sources (like interest), and agricultural income up to ₹5,000.
- **Generated:** The context mentions that an individual of the age of eighty years or more, who furnishes the return in Form number SAHAJ (ITR-1), is subject to the requirement of accounts being audited under section 44AB of the Act [Source 4].
- **Similarity:** 0.5298 | **ROUGE-L:** 0.1053 | **Precision:** 0.7576

### Q3: What is the TDS rate for fees for professional or technical services under section 194J?
- **Expected:** The TDS rate under section 194J is 2% for fees for technical services (not being a professional service) or royalty in nature of sale/distribution/exhibition of cinematographic films, and 10% for other professional services.
- **Generated:** The TDS rate for fees for Technical Services, Call Centre, Royalty, Distribution under section 194J is 10% for Individuals/HUF and 10% for Others [Source 2].
- **Similarity:** 0.8164 | **ROUGE-L:** 0.459 | **Precision:** 0.6667

### Q4: Are long-term capital gains on equity shares exempt from tax?
- **Expected:** No, long-term capital gains on listed equity shares are taxable under section 112A at 10% (or 12.5% per recent amendments) on gains exceeding ₹1 lakh (or ₹1.25 lakh per recent amendments) in a financial year, without indexation benefit.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.365 | **ROUGE-L:** 0.0392 | **Precision:** 0.3333

### Q5: What is the maximum deduction allowed under section 80C of the Income Tax Act?
- **Expected:** The maximum deduction allowed under section 80C for investments in PPF, LIC, ELSS, etc., is ₹1,50,000 in a financial year. This is only available under the old tax regime.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3511 | **ROUGE-L:** 0.0976 | **Precision:** 0.3333

### Q6: Is Health and Education Cess applicable on income tax?
- **Expected:** Yes, Health and Education Cess is levied at the rate of 4% on the amount of income-tax and surcharge.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4404 | **ROUGE-L:** 0.2 | **Precision:** 0.4444

### Q7: Can an NRI file ITR-1?
- **Expected:** No, Non-Resident Indians (NRIs) and Resident but Not Ordinarily Residents (RNORs) cannot file ITR-1. They must use ITR-2 or ITR-3.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.2735 | **ROUGE-L:** 0.0 | **Precision:** 0.5556

### Q8: What is the threshold limit for GST registration for a service provider?
- **Expected:** The general threshold limit for GST registration for service providers is an aggregate turnover of ₹20 lakh in a financial year (₹10 lakh for special category states).
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.2419 | **ROUGE-L:** 0.1081 | **Precision:** 0.4444

### Q9: What is the difference between CGST and SGST?
- **Expected:** CGST (Central GST) is levied by the Central Government, and SGST (State GST) is levied by the State Government on intra-state supplies of goods and services.
- **Generated:** The provided context does not explicitly state the difference between CGST and SGST. However, it does provide rules regarding their reporting:

*   If CGST is reported, then SGST/UTGST must also be reported, and IGST will be blank [Source 1].
*   If SGST/UTGST is reported, then CGST must be reported, and IGST will be blank [Source 3].
- **Similarity:** 0.6233 | **ROUGE-L:** 0.1446 | **Precision:** 0.3529

### Q10: Under which section of the CGST Act is the input tax credit (ITC) claimed?
- **Expected:** Input Tax Credit (ITC) is claimed under Section 16 of the CGST Act, 2017, subject to the conditions specified therein.
- **Generated:** The provided context mentions that the input tax credit (ITC) in respect of inputs or input services is determined based on whether it is partly used for business and partly for other purposes, or partly used for effecting taxable supplies (including zero-rated supplies) and partly for effecting exempt supplies [Source 3]. Furthermore, the context refers to Section 16(4) of the CGST Act, 2017, in relation to the period within which credit on ITC availed in the next financial year must be utilized [Source 2]. However, the specific section of the CGST Act under which the ITC is claimed is not explicitly stated in the provided documents.
- **Similarity:** 0.8973 | **ROUGE-L:** 0.2188 | **Precision:** 0.6269

### Q11: Is the new tax regime the default regime for FY 2025-26?
- **Expected:** Yes, the new tax regime under section 115BAC is the default tax regime. Taxpayers wishing to use the old regime must explicitly opt for it.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.5236 | **ROUGE-L:** 0.1143 | **Precision:** 0.3333

### Q12: What is the tax rate for income between ₹8 lakh and ₹12 lakh under the new tax regime?
- **Expected:** Under the new tax regime, the tax rate for income between ₹8 lakh and ₹12 lakh is 10%.
- **Generated:** The tax rate for income between ₹800001 to ₹1200000 is 10% [Source 1].
- **Similarity:** 0.8781 | **ROUGE-L:** 0.5161 | **Precision:** 0.7692

### Q13: What is Form 3CD?
- **Expected:** Form 3CD is a statement of particulars required to be furnished under Section 44AB of the Income Tax Act. It is part of the tax audit report prepared by a Chartered Accountant.
- **Generated:** Form 3CD has two reporting requirements: (1) the amount of interest that is inadmissible under section 23 of the MSMED Act, 2006, and (2) any other amount that is not allowable under clause (h) of section 43B of the Income-tax Act, 1961 [Source 3].
- **Similarity:** 0.7405 | **ROUGE-L:** 0.3117 | **Precision:** 0.8182

### Q14: Can a person with business income opt in and out of the new tax regime every year?
- **Expected:** No, a person having business or professional income can opt out of the new tax regime only once. Once they revert to the old regime, they cannot opt back into the new regime for that business, except in certain specific circumstances.
- **Generated:** The provided context indicates that for a domestic company, the option to compute income-tax at the rate of 25% under the New tax regime (Section 199) is available, subject to certain conditions [Source 4]. However, the context does not state whether a person can opt in and out of this regime every year.
- **Similarity:** 0.6198 | **ROUGE-L:** 0.2316 | **Precision:** 0.5455

### Q15: What is the due date for filing ITR for individuals not subject to tax audit?
- **Expected:** The due date for filing the Income Tax Return for individuals whose accounts are not required to be audited is generally July 31st of the assessment year.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3912 | **ROUGE-L:** 0.1081 | **Precision:** 0.3333

### Q16: Is rent received from a house property fully taxable?
- **Expected:** No, from the gross annual value (rent received/receivable), municipal taxes paid are deducted to arrive at the Net Annual Value (NAV). From NAV, a standard deduction of 30% is allowed under section 24(a), plus deduction for interest on borrowed capital under section 24(b).
- **Generated:** Any income from letting out a residential house or a part of it by the owner shall not be included in income under sub-section (1) and shall be chargeable only under the head "Income from house property" [Source 4].

Furthermore, the amount of arrears of rent received by an assessee from a tenant, or the unrealised rent realised subsequently from a tenant, shall be deemed to be the income from house property in respect of the tax year in which such rent is received or realised [Source 1]. This amount deemed to be income from house property shall be included in the total income of the assessee under the head "Income from house property", regardless of whether the assessee is the owner of the property or not in that tax year [Source 1].

Deductions are available under this head, such as a sum equal to 30% of the arrears of rent or the unrealised rent referred to in sub-section (1) [Source 1], and also deductions related to the annual value, interest on borrowed capital, etc., as per section 22(1) [Source 2].
- **Similarity:** 0.6352 | **ROUGE-L:** 0.1565 | **Precision:** 0.7778

### Q17: What is the threshold for deducting TDS on rent under section 194-I?
- **Expected:** TDS on rent under section 194-I must be deducted if the total rent paid or payable during the financial year exceeds ₹2,40,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3914 | **ROUGE-L:** 0.1143 | **Precision:** 0.3333

### Q18: What is IGST and when is it applicable?
- **Expected:** IGST stands for Integrated Goods and Services Tax. It is levied by the Central Government on all inter-state supplies of goods and services, as well as on imports and exports.
- **Generated:** IGST is one of the taxes that should be reported, alongside either CGST & SGST/UTGST [Source 1 | CGST-Rules-2017-Part-Forms.pdf (Page 395)]. There is a specific field to report the applicability of IGST despite the supplier and recipient being located in the same State/UT [Source 3 | CGST-Rules-2017-Part-B-Forms.pdf (Page 378)]. Furthermore, there is a section for "Place of supply wise details of IGST demand" [Source 4 | CGST-Rules-2017-Part-B-Forms.pdf (Page 344)].
- **Similarity:** 0.6969 | **ROUGE-L:** 0.1217 | **Precision:** 0.62

### Q19: What are the components of the composition scheme under GST?
- **Expected:** Under the composition scheme, eligible taxpayers with a turnover up to ₹1.5 crore can pay a flat percentage of their turnover (e.g., 1% for traders, 5% for restaurants, 6% for service providers) instead of regular GST. They cannot claim input tax credit.
- **Generated:** The provided documents detail various forms related to GST, such as FORM GST CMP-01 and FORM GST CMP-02, which are for "Intimation to pay tax under section 10 (composition levy)" [Source 1, Source 2].

For FORM GST CMP-02, the categories of registered persons eligible for composition levy include:
*   Manufacturers, other than manufacturers of such goods as may be notified by the Government [Source 1]
*   Suppliers making supplies referred to in clause (b) of paragraph 6 of Schedule II [Source 1]
*   Any other supplier eligible for composition levy [Source 1]

For FORM GST CMP-01, the categories of registered persons include:
*   Manufacturers, other than manufacturers of such goods as notified by the Government [Source 2]
*   Suppliers making supplies referred to in clause (b) of paragraph 6 of Schedule II [Source 2]
*   Any other supplier eligible for composition levy [Source 2]
- **Similarity:** 0.5455 | **ROUGE-L:** 0.1075 | **Precision:** 0.6667

### Q20: How is agricultural income taxed in India?
- **Expected:** Agricultural income is exempt from income tax under Section 10(1) of the Income Tax Act. However, if the taxpayer has non-agricultural income exceeding the basic exemption limit, the agricultural income is included for rate purposes to calculate tax on the non-agricultural income.
- **Generated:** The provided documents indicate that there is a section for "Gross Agricultural receipts (other than income to be excluded under rule 7A, 7B or 8 of I.T. Rules)" under the details of Exempt Income [Source 2 | ITR-3-2026-Eng.pdf (Page 49), Source 4 | ITR-2-2026-Eng.pdf (Page 24)].

For the purpose of calculating Net Agricultural income, the following components are considered:
*   Gross Agricultural receipts (other than income to be excluded under rule 7A, 7B or 8 of I.T. Rules) [Source 2 | ITR-3-2026-Eng.pdf (Page 49), Source 4 | ITR-2-2026-Eng.pdf (Page 24)]
*   Less: Expenditure incurred on agriculture [Source 2 | ITR-3-2026-Eng.pdf (Page 49), Source 4 | ITR-2-2026-Eng.pdf (Page 24)]
*   Less: Unabsorbed agricultural loss of previous eight assessment years [Source 2 | ITR-3-2026-Eng.pdf (Page 49), Source 4 | ITR-2-2026-Eng.pdf (Page 24)]
*   Plus: Agricultural income portion relating to Rule 7, 7A, 7B(1), 7B(1A) and 8 (from Sl. No. 38 of Sch. BP) [Source 2 | ITR-3-2026-Eng.pdf (Page 49)]

The Net Agricultural income for the year is calculated as (i – ii – iii + iv) [Source 2 | ITR-3-2026-Eng.pdf (Page 49)].

Additionally, for the purpose of computing income from the manufacture of tea, income derived from the sale of tea grown and manufactured by the seller in India is computed as if it were income derived from business, and forty per cent of such income shall be deemed to be income liable to tax [Source 3 | Income-tax-Rules-1962_2026_en.pdf (Page 96)].
- **Similarity:** 0.6191 | **ROUGE-L:** 0.1203 | **Precision:** 0.7521

### Q21: Can I claim HRA and deduction for home loan interest simultaneously?
- **Expected:** Yes, under the old tax regime, you can claim House Rent Allowance (HRA) exemption and deduction for interest on a home loan under section 24(b) simultaneously, provided the rented house and the owned house are in different cities, or you can prove genuine reasons for renting despite owning a house in the same city.
- **Generated:** The provided context mentions that for claiming a deduction of interest under the head "Income from house property," the assessee must furnish the name, address, and permanent account number of the lender [Source 2]. However, the context does not state whether you can claim House Rent Allowance (HRA) and the deduction for home loan interest simultaneously.
- **Similarity:** 0.8474 | **ROUGE-L:** 0.2703 | **Precision:** 0.5814

### Q22: What is the penalty for late filing of Income Tax Return under section 234F?
- **Expected:** A fee of ₹5,000 is payable under section 234F if the return is furnished after the due date. However, if the total income does not exceed ₹5 lakh, the fee is restricted to ₹1,000.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.3541 | **ROUGE-L:** 0.0435 | **Precision:** 0.4444

### Q23: Are cryptocurrency gains taxed in India?
- **Expected:** Yes, income from the transfer of any Virtual Digital Asset (VDA), including cryptocurrencies, is taxed at a flat rate of 30% under Section 115BBH, plus applicable surcharge and cess. No deductions or set-off of losses are allowed.
- **Generated:** I don't know based on the provided tax documents.
- **Similarity:** 0.4857 | **ROUGE-L:** 0.0833 | **Precision:** 0.4444

### Q24: Who is required to obtain a Tax Deduction and Collection Account Number (TAN)?
- **Expected:** Any person who is responsible for deducting tax at source (TDS) or collecting tax at source (TCS) is required to obtain a 10-digit alphanumeric TAN under Section 203A of the Income Tax Act.
- **Generated:** Every person who is deducting or collecting tax must apply for the allotment of a tax deduction and collection account number to the Assessing Officer within the prescribed time, if they have not already been allotted such a number [Source 2]. However, this requirement does not apply to:
*   A person who is required to deduct tax under the provisions of section 393(1) [Source 2].
*   A person referred to in section 393(4) [Source 2].
*   A person notified in this regard by the Central Government [Source 2].
- **Similarity:** 0.5106 | **ROUGE-L:** 0.2314 | **Precision:** 0.7857

### Q25: Can ITR-4 be used by a doctor?
- **Expected:** Yes, a doctor (medical professional) can use ITR-4 (Sugam) if they opt for the presumptive taxation scheme under section 44ADA and their gross receipts do not exceed the specified threshold (₹50 lakh or ₹75 lakh subject to cash receipt limits).
- **Generated:** The context mentions that "Form SUGAM (ITR-4S) or Form No. ITR-4" was substituted for a previous form [Source 3]. Furthermore, it states that for an individual or a Hindu undivided family who is a resident other than not ordinarily resident, or a firm, other than a limited liability partnership firm, deriving income under the head "Profits or gains of business or profession" and such income is computed according to special provisions in section 44AD, section 44ADA, and section 44AE of the Act, they should use Form SUGAM (ITR-4) [Source 4].

Since a doctor is typically an individual engaged in a profession, and the context mentions the applicability of ITR-4/SUGAM for individuals deriving income under the head "Profits or gains of business or profession" under specific sections (like 44ADA, which relates to professionals), it suggests that ITR-4 (or its substitute, SUGAM) may be applicable to a doctor, provided they meet the criteria mentioned in Source 4 [Source 4].
- **Similarity:** 0.7032 | **ROUGE-L:** 0.1176 | **Precision:** 0.5263

