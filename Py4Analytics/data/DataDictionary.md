# Boston Housing
This dataset contains information collected by the US Census Service concerning housing in the area of Boston Massachusetts. It was obtained from the StatLib archive (http://lib.stat.cmu.edu/datasets/boston). The dataset has 506 cases.
* __Source__: The data was originally published by Harrison, D. and Rubinfeld, D.L. `Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.
There are 14 attributes in each case of the dataset. They are:
    CRIM 	per capita crime rate by town
    ZN     	proportion of residential land zoned for lots over 25,000 sq.ft.
    INDUS	proportion of non-retail business acres per town.
    CHAS 	Charles River dummy variable (1 if tract bounds river; 0 otherwise)
    NOX   	nitric oxides concentration (parts per 10 million)
    RM    	average number of rooms per dwelling
    AGE   	proportion of owner-occupied units built prior to 1940
    DIS   	weighted distances to five Boston employment centres
    RAD  	index of accessibility to radial highways
    TAX  	full-value property-tax rate per $10,000
    PTRATIO 	pupil-teacher ratio by town
    LSTAT   	% lower status of the population
    MEDV	Median value of owner-occupied homes in $1000
# Cereal
* __Source__: DATA ANALYSIS FOR STUDENT LEARNING (DASL)
1. Name: Name of cereal
2. mfr: Manufacturer of cereal where A = American Home Food Products; G = General Mills; K = 
    Kelloggs; N = Nabisco; P = Post; Q = Quaker Oats; R = Ralston Purina
3. type: cold or hot
4. calories: calories per serving
5. protein: grams of protein
6. fat: grams of fat
7. sodium: milligrams of sodium
8. fiber: grams of dietary fiber
9. carbo: grams of complex carbohydrates
10. sugars: grams of sugars
11. potass: milligrams of potassium
12. vitamins: vitamins and minerals - 0, 25, or 100, indicating the typical percentage of FDA 
      recommended
13. shelf: display shelf (1, 2, or 3, counting from the floor)
14. weight: weight in ounces of one serving
15. cups: number of cups in one serving
16. rating: a rating of the cereals calculated by Consumer Reports
# GermanCredit
| Variable Name    | Description                                 | Variable Type | Code Description                                                 |
| :--------------- | :------------------------------------------ | :------------ | :--------------------------------------------------------------- |
| OBS#             | Observation No.                             | Categorical   |
| CHK_ACCT         | Checking account status                     | Categorical   | 0: < 0 DM                                                        |
|                  |                                             |               | 1:  0 < ...< 200 DM                                              |
|                  |                                             |               | 2: => 200 DM                                                     |
|                  |                                             |               | 3:  no checking account                                          |
| DURATION         | Duration of credit in months                | Numerical     |
| HISTORY          | Credit history                              | Categorical   | 0: no credits taken                                              |
|                  |                                             |               | 1: all credits at this bank paid back duly                       |
|                  |                                             |               | 2: existing credits paid back duly till now                      |
|                  |                                             |               | 3: delay in paying off in the past                               |
|                  |                                             |               | 4: critical account                                              |
| NEW_CAR          | Purpose of credit                           | Binary        | car (new) 0: No, 1: Yes                                          |
| USED_CAR         | Purpose of credit                           | Binary        | car (used) 0: No, 1: Yes                                         |
| FURNITURE        | Purpose of credit                           | Binary        | furniture/equipment 0: No, 1: Yes                                |
| RADIO/TV         | Purpose of credit                           | Binary        | radio/television 0: No, 1: Yes                                   |
| EDUCATION        | Purpose of credit                           | Binary        | education 0: No, 1: Yes                                          |
| RETRAINING       | Purpose of credit                           | Binary        | retraining 0: No, 1: Yes                                         |
| AMOUNT           | Credit amount                               | Numerical     |
| SAV_ACCT         | Average balance in savings account          | Categorical   | 0 : <  100 DM                                                    |
|                  |                                             |               | 1 : 100<= ... <  500 DM                                          |
|                  |                                             |               | 2 : 500<= ... < 1000 DM                                          |
|                  |                                             |               | 3 : =>1000 DM                                                    |
|                  |                                             |               | 4 : unknown/ no savings account                                  |
| EMPLOYMENT       | Present employment since                    | Categorical   | 0 : unemployed                                                   |
|                  |                                             |               | 1 :  < 1 year                                                    |
|                  |                                             |               | 2 : 1 <= ... < 4 years                                           |
|                  |                                             |               | 3 : 4 <=... < 7 years                                            |
|                  |                                             |               | 4 : >= 7 years                                                   |
| INSTALL_RATE     | Installment rate as % of disposable income  | Numerical     |
| MALE_DIV         | Applicant is male and divorced              | Binary        | 0: No, 1: Yes                                                    |
| MALE_SINGLE      | Applicant is male and single                | Binary        | 0: No, 1: Yes                                                    |
| MALE_MAR_WID     | Applicant is male and married or a widower  | Binary        | 0: No, 1: Yes                                                    |
| CO-APPLICANT     | Application has a co-applicant              | Binary        | 0: No, 1: Yes                                                    |
| GUARANTOR        | Applicant has a guarantor                   | Binary        | 0: No, 1: Yes                                                    |
| PRESENT_RESIDENT | Present resident since-years                | Categorical   | 0: <= 1 year                                                     |
|                  |                                             |               | 1<…<=2 years                                                     |
|                  |                                             |               | 2<…<=3 years                                                     |
|                  |                                             |               | 3:>4years                                                        |
| REAL_ESTATE      | Applicant owns real estate                  | Binary        | 0: No, 1: Yes                                                    |
| PROP_UNKN_NONE   | Applicant owns no property (or unknown)     | Binary        | 0: No, 1: Yes                                                    |
| AGE              | Age in years                                | Numerical     |
| OTHER_INSTALL    | Applicant has other installment plan credit | Binary        | 0: No, 1: Yes                                                    |
| RENT             | Applicant rents                             | Binary        | 0: No, 1: Yes                                                    |
| OWN_RES          | Applicant owns residence                    | Binary        | 0: No, 1: Yes                                                    |
| NUM_CREDITS      | Number of existing credits at this bank     | Numerical     |
| JOB              | Nature of job                               | Categorical   | 0: unemployed/ unskilled  - non-resident                         |
|                  |                                             |               | 1: unskilled - resident                                          |
|                  |                                             |               | 2: skilled employee / official                                   |
|                  |                                             |               | 3: management/ self-employed/highly  qualified employee/ officer |
NUM_DEPENDENTS  | Number of people for whom liable to provide maintenance |   Numerical|
TELEPHONE|        Applicant has phone in his or her name | Binary |   0: No, 1: Yes
FOREIGN |  	   Foreign worker   		     |    Binary     | 0: No, 1: Yes
RESPONSE|         Credit rating is good|   	         Binary  |    0: No, 1: Yes   	

# CancerMortality
These data were aggregated from a number of sources including the American Community Survey ([census.gov](http://census.gov/)), [clinicaltrials.gov](http://clinicaltrials.gov/), and [cancer.gov](http://cancer.gov/). Most of the data preparation process can be veiwed [here](https://data.world/nrippner/cancer-trials).
[source](https://data.world/nrippner/ols-regression-challenge)

* __TARGET_deathRate:__ Dependent variable. Mean per capita (100,000) cancer mortalities(a)
* __avgAnnCount:__ Mean number of reported cases of cancer diagnosed annually(a)
* __avgDeathsPerYear:__ Mean number of reported mortalities due to cancer(a)
* __incidenceRate:__ Mean per capita (100,000) cancer diagoses(a)
* __medianIncome:__ Median income per county (b)
* __popEst2015:__ Population of county (b)
* __povertyPercent:__ Percent of populace in poverty (b)
* __studyPerCap:__ Per capita number of cancer-related clinical trials per county (a)
* __binnedInc:__ Median income per capita binned by decile (b)
* __MedianAge:__ Median age of county residents (b)
* __MedianAgeMale:__ Median age of male county residents (b)
* __MedianAgeFemale:__ Median age of female county residents (b)
* __Geography:__ County name (b)
* __AvgHouseholdSize:__ Mean household size of county (b)
* __PercentMarried:__ Percent of county residents who are married (b)
* __PctNoHS18_24:__ Percent of county residents ages 18-24 highest education attained:__ less than high school (b)
* __PctHS18_24:__ Percent of county residents ages 18-24 highest education attained:__ high school diploma (b)
* __PctSomeCol18_24:__ Percent of county residents ages 18-24 highest education attained:__ some college (b)
* __PctBachDeg18_24:__ Percent of county residents ages 18-24 highest education attained:__ bachelor's degree (b)
* __PctHS25_Over:__ Percent of county residents ages 25 and over highest education attained:__ high school diploma (b)
* __PctBachDeg25_Over:__ Percent of county residents ages 25 and over highest education attained:__ bachelor's degree (b)
* __PctEmployed16_Over:__ Percent of county residents ages 16 and over employed (b)
* __PctUnemployed16_Over:__ Percent of county residents ages 16 and over unemployed (b)
* __PctPrivateCoverage:__ Percent of county residents with private health coverage (b)
* __PctPrivateCoverageAlone:__ Percent of county residents with private health coverage alone (no public assistance) (b)
* __PctEmpPrivCoverage:__ Percent of county residents with employee-provided private health coverage (b)
* __PctPublicCoverage:__ Percent of county residents with government-provided health coverage (b)
* __PctPubliceCoverageAlone:__ Percent of county residents with government-provided health coverage alone (b)
* __PctWhite:__ Percent of county residents who identify as White (b)
* __PctBlack:__ Percent of county residents who identify as Black (b)
* __PctAsian:__ Percent of county residents who identify as Asian (b)
* __PctOtherRace:__ Percent of county residents who identify in a category which is not White, Black, or Asian (b)
* __PctMarriedHouseholds:__ Percent of married households (b)
* __BirthRate:__ Number of live births relative to number of women in county (b)
(a): years 2010-2016
(b): 2013 Census Estimates

# Insurance
* __age__: age of primary beneficiary
* __sex__: insurance contractor gender, female, male
* __bmi__: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
* __children__: Number of children covered by health insurance / Number of dependents
* __smoker__: Smoking
* __region__: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
* __charges__: Individual medical costs billed by health insurance

# Toyota Corolla
(source unknown)
The dataset [ToyotaCorolla.csv](./ToyotaCorolla.csv) contains data on used cars on sale during the late summer of2004 in the Netherlands.

ToyotaCorolla
|Variable|   	 	Description|Example|
|--------|---------------------|-------|
|Id|   		 	Record_ID|
|Model|   	 	Model Description|
|Price|   		 	Offer Price in EUROs|
|Age_08_04|   	 	Age in months as in August 2004|
|Mfg_Month|   	 	Manufacturing month |(1-12)|
|Mfg_Year|   	 	Manufacturing Year|
|KM|   		 	Accumulated Kilometers on odometer|
|Fuel_Type|   		Fuel Type |(Petrol, Diesel, CNG)|
|HP|   			Horse Power|
|Met_Color|   	 	Metallic Color?  |(Yes=1, No=0)|
|Color|   		 	Color |(Blue, Red, Grey, Silver, Black, etc.)|
|Automatic|   	 	Automatic |(Yes=1, No=0)|
|CC|   		 	Cylinder Volume in cubic centimeters|
|Doors|   	 	Number of doors|
|Cylinders|   	 	Number of cylinders|
|Gears|   	 	Number of gear positions|
|Quarterly_Tax|  	Quarterly road tax in EUROs|
|Weight|   		Weight in Kilograms|
|Mfr_Guarantee|   	Within Manufacturer's Guarantee period  |(Yes=1, No=0)|
|BOVAG_Guarantee|   	BOVAG |(Dutch dealer network) Guarantee  |(Yes=1, No=0)|
|Guarantee_Period|       Guarantee period in months|
|ABS|   		 	Anti-Lock Brake System |(Yes=1, No=0)|
|Airbag_1|   	 	Driver_Airbag  |(Yes=1, No=0)||
|Airbag_2|   	 	Passenger Airbag  |(Yes=1, No=0)|
|Airco|   		 	Airconditioning  |(Yes=1, No=0)|
|Automatic_airco|   	Automatic Airconditioning  |(Yes=1, No=0)|
|Boardcomputer|   	Boardcomputer  |(Yes=1, No=0)|
|CD_Player|   	 	CD Player  |(Yes=1, No=0)|
|Central_Lock|   	Central Lock  |(Yes=1, No=0)|
|Powered_Windows|   	Powered Windows  |(Yes=1, No=0)|
|Power_Steering|   	Power Steering  |(Yes=1, No=0)|
|Radio|   		Radio  |(Yes=1, No=0)|
|Mistlamps|   	 	Mistlamps  |(Yes=1, No=0)|
|Sport_Model|   	 	Sport Model  |(Yes=1, No=0)|
|Backseat_Divider|        Backseat Divider  |(Yes=1, No=0)|
|Metallic_Rim|   	 	Metallic Rim  |(Yes=1, No=0)|
|Radio_cassette|   	Radio Cassette  |(Yes=1, No=0)|
|Parking_Assistant|    	Parking assistance system  |(Yes=1, No=0)|
|Tow_Bar|   		Tow Bar  |(Yes=1, No=0)|
