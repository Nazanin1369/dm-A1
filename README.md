## Data Mining First Assignment
Data Mining on counties GDP vs Income Group

### Data Files
Data files are provided under data directory: edstats_country.csv and gdp_data.csv.

### Dependencies
To be able to run the code you need to have the following dependencies installed:
* Python 3.5
* Numpy
* Pandas
* Matplotlib
* Jupyter Notebook

- For your convienience the Conda environment.yaml file is included in the project to install all dependencies.


### How to run the notebook
Run the following command on the root directory:

``` script
jupyter notebook --port 9999 Analysis.ipynb
```

Or simply run the python file to only see assignment answers:

``` script
python Analysis.py
```

``` script
(naz) 🦄 python Analysis.py
Total number of countries:  234
Total number of features:  28

### Question one ###
Total number of countries: 206
Number of matched countries: 187


### Question two ###
Last country in sorted_data is United States
USA    United States of America
Name: Long Name, dtype: object

13th country in sorted data is:  VUT    Republic of Vanuatu
Name: Long Name, dtype: object


### Question three ###
average GDP ranking for the “High income:OECD" and “High income:nonOECD" group:
61.1878787879


### Question four ###
Min:  1.0
First quantile:  47.5
Median:  94.0
Mean:  94.5240641711
Second quantile:  141.5
Max:  189.0

     Ranking         Income Group
CHN      2.0  Lower middle income
IND     10.0  Lower middle income
IDN     16.0  Lower middle income
THA     31.0  Lower middle income
EGY     38.0  Lower middle income

Number of High GDP countiest with low middle income  group:  5
```
