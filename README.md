# Layoffs Analysis

## Overview
The "Layoffs Analysis" project is a Python-based tool for analyzing and visualizing layoff trends across various industries, 
companies, and locations over time. Utilizing data sourced from layoffs during the recent economic changes in the tech industry,
the project aims to provide insights into employment dynamics.

## Dataset Description
This analysis utilizes a dataset that chronicles layoffs in the tech industry, 
reflecting the economic challenges faced since the COVID-19 pandemic 
(from March 11, 2020, to October 16, 2023). Economic factors such as decreased consumer spending, 
higher central bank interest rates, and strong international dollar values have pressured tech firms, 
leading to significant layoffs. Notably, companies like Meta have reduced their workforce substantially. 
The dataset, originally curated by Roger Lee, compiles information from sources like Bloomberg, TechCrunch, 
and The New York Times. Complete data is available on [Layoffs.fyi](https://www.kaggle.com/datasets/swaptr/layoffs-2022/data).

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: pandas, sqlite3, matplotlib

## Features
The script provides interactive visualizations in four key areas:
1. **Industries with the Highest Count of Companies with Layoffs**
2. **Companies with the Highest Sum of Layoffs**
3. **Total Layoffs by Quarter**
4. **Locations with the Highest Sum of Layoffs**

### Graph Analysis
Each graph offers a unique perspective:
- **Top Industries**: Indicates which sectors are most affected.
- **Top Companies**: Highlights companies facing the largest layoffs.
- **Quarterly Analysis**: Shows trends and patterns in layoffs over time.
- **Geographical Impact**: Reveals locations with the most layoffs.

## Data Source
The project analyzes data from 'layoffs.csv', sourced from Kaggle's "Tech Layoffs 2022" dataset. 
This dataset spans from March 11, 2020, to October 16, 2023, 
providing a comprehensive view of layoffs in the tech industry during this period. 
The data is compiled from various reputable sources and credited to Roger Lee.