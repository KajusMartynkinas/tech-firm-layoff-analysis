import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
csv_file_path = 'layoffs.csv'  # Update this to the path of your CSV file
df = pd.read_csv(csv_file_path)
conn = sqlite3.connect(':memory:')
df.to_sql('layoffs', conn, index=False, if_exists='replace')

# Define and execute an SQL query
# query = "SELECT * FROM layoffs WHERE total_laid_off > 100"  # Example query

while True:

    #Which Industries had the most componies with layoffs
    def show_1():
        company_count="""
        SELECT industry, COUNT(DISTINCT company) as company_count
        FROM layoffs WHERE total_laid_off >= 1
        GROUP BY industry
        ORDER BY company_count desc
        LIMIT 10
        """
        top_industries = pd.read_sql_query(company_count, conn)
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 6))
        plt.bar(top_industries['industry'], top_industries['company_count'], color='cyan')
        plt.xlabel('Industry')
        plt.ylabel('Number of Companies with Layoffs')
        plt.title('Top 10 Industries with the Highest Count of Companies Having Layoffs')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    #Companies with most layoffs
    def show_2():
        layoff_count="""
        SELECT company, SUM(total_laid_off) AS sum_of_laid_off
        FROM layoffs 
        WHERE total_laid_off >= 1
        GROUP BY company
        ORDER BY sum_laid_off DESC
        LIMIT 10
        """
        top_companies = pd.read_sql_query(layoff_count, conn)
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 6))
        plt.bar(top_companies['company'], top_companies['sum_of_laid_off'], color='cyan')
        plt.xlabel('Company')
        plt.ylabel('Number of Layoffs')
        plt.title('Top 10 Companies with the Highest Sum of Layoffs')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    #Layoffs by Yearly Quarters from 2020 to 2024
    def show_3():
        layoff_count = """
        SELECT strftime('%Y', date) || '-' || CASE 
                   WHEN CAST(strftime('%m', date) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
                   WHEN CAST(strftime('%m', date) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
                   WHEN CAST(strftime('%m', date) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
                   WHEN CAST(strftime('%m', date) AS INTEGER) BETWEEN 10 AND 12 THEN 'Q4'
               END AS year_quarter,
               SUM(total_laid_off) AS sum_laid_off
        FROM layoffs
        WHERE total_laid_off >= 1
        GROUP BY year_quarter
        ORDER BY year_quarter
        """
        quarterly_layoff_result = pd.read_sql_query(layoff_count, conn)
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 6))
        plt.bar(quarterly_layoff_result['year_quarter'], quarterly_layoff_result['sum_laid_off'], color='cyan')
        plt.xlabel('Quarter')
        plt.ylabel('Total Layoffs')
        plt.title('Total Layoffs by Quarter')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    #Locations with most layoffs
    def show_4():
        layoff_count="""
        SELECT location, SUM(total_laid_off) AS sum_of_laid_off
        FROM layoffs
        WHERE total_laid_off >= 1
        GROUP BY location
        ORDER BY sum_of_laid_off desc
        LIMIT 10
        """
        top_countries = pd.read_sql_query(layoff_count, conn)
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 6))
        plt.bar(top_countries['location'], top_countries['sum_of_laid_off'], color='cyan')
        plt.xlabel('Location')
        plt.ylabel('Number of Layoffs')
        plt.title('Top 10 Locations with the Highest Sum of Layoffs')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    print("Select the graph that you want to be displayed:")
    print("1: Top 10 Industries with the Highest Count of Companies Having Layoffs")
    print("2: Top 10 Companies with the Highest Sum of Layoffs")
    print("3: Total Layoffs by Quarter")
    print("4: Top 10 Locations with the Highest Sum of Layoffs")
    print("0: Exit program")
    print("Enter the number of your choice: \n")
    choice = input()

    if choice == '1':
        show_1()
    elif choice == '2':
        show_2()
    elif choice == '3':
        show_3()
    elif choice == '4':
        show_4()
    elif choice == '0':
        print('The program is closing. Goodbye')
        break
    else:
        print('Incorrect choice. Try again: \n')

    # Display the result
    # print(result)
    # result.to_csv('layoffs0.csv')