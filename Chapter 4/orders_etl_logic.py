import pandas as pd
import sqlalchemy as db

orders_table = "../Ex_Files_ETL_Python_SQL/Exercise Files/Chapter_4/H+ Sport orders.xlsx"
engine = db.create_engine('mysql+pymysql://root:password@localhost:3306/etl_course_db')

def main():
    orders = pd.read_excel(orders_table, sheet_name='data')

    orders = orders[["OrderID","Date","TotalDue","Status","CustomerID","SalespersonID"]]

    orders.to_sql('orders', engine,
                  if_exists='replace',
                  index=False)
    
    print("ETL script executed successfully.")