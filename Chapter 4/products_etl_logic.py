import pandas as pd
import sqlalchemy as db

products_table = "../Ex_Files_ETL_Python_SQL/Exercise Files/Chapter_4/H+ Sport products.xlsx"
engine = db.create_engine('mysql+pymysql://root:password@localhost:3306/etl_course_db')

def main():
    products = pd.read_excel(products_table, sheet_name='data')

    products["Price"] = products["Price"]/0.92

    products.to_sql('products', engine,
                  if_exists='replace',
                  index=False)
    
    print("ETL script executed successfully.")