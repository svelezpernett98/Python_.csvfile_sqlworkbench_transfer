import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import string    
import random  



empdata = pd.read_csv('C:/Users/svelez/Documents/csv_sql_transfer/sales_2022-07-01_2022-08-10.csv', index_col=False, delimiter = ',')
empdata.head()

#------------CONECTAR CON EL HOST Y CREAR LA BD, SOLO SE HACE EN CASO DE QUE LA BD NO ESTE CREADA TODAVIA (LINEA 14 A 22):

# try:
#     conn = msql.connect(host='localhost', user='root',  
#                         password='')#give ur username, password
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("CREATE DATABASE testdb")
#         print("Database is created")
# except Error as e:
#     print("Error while connecting to MySQL", e)


#-----------CONECTAR CON EL HOST, SELECCIONAR LA BD Y ELIMINAR LA TABLA SI EXISTE(LINEA 33):
try:
    conn = msql.connect(host='localhost', database='testdb', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS table5;')
        print('Creating table....')

        #-----------CREAR TABLA:
        cursor.execute("CREATE TABLE table5(hour varchar(255), order_name varchar(255), financial_status varchar(255), fulfillment_status varchar(255), cancelled varchar(255), order_id varchar(255), sale_kind varchar(255), customer_id varchar(255), customer_name varchar(255), customer_email varchar(255), customer_type varchar(255), variant_sku varchar(255), shipping_city varchar(255), shipping_region varchar(255), shipping_country varchar(255), billing_city varchar(255), billing_region varchar(255), billing_country varchar(255), referrer_name varchar(255), referrer_source varchar(255), sale_line_type varchar(255), billing_postal_code varchar(255), utm_campaign_content varchar(255), utm_campaign_medium varchar(255), utm_campaign_name varchar(255), utm_campaign_source varchar(255), utm_campaign_term varchar(255), product_title varchar(255), product_type varchar(255), variant_title varchar(255), shipping_postal_code varchar(255), referrer_host varchar(255), product_price varchar(255), ordered_item_quantity varchar(255), total_sales varchar(255), discounts varchar(255), gross_sales varchar(255), net_sales varchar(255), returns varchar(255), shipping varchar(255), taxes varchar(255), units_per_transaction varchar(255), net_quantity varchar(255), gift_card_discounts varchar(255), gift_card_gross_sales varchar(255), gift_cards_issued varchar(255), returned_item_quantity varchar(255))")
        print("Table is created....")
        
        #-------------CICLO POR CADA FILA DEL EXCEL:
        for i,row in empdata.iterrows():
            #%S SIGNIFICA LOS VALORES DE STRING             
            
            #47 %S PORQUE SON 47 DATOS (COLUMNAS) POR FILA:
            sql = 'INSERT INTO table5 VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'#47 %s
            
            cursor.execute(sql, tuple(row))
            
            print("Record inserted")
            #LA CONECCION NO SE ACTUALIZA AUTOMATICAMENTE, POR ESO HAY QUE HACE COMMIT PARA AGREGAR LOS CAMBIOS:
            conn.commit()
        
        #------------PARA AGREGAR UNA LLAVE PRIMARIA AUTOINCREMENTAL SI NECESITO UNA:
        cursor.execute("ALTER TABLE table5 ADD test_pk int AUTO_INCREMENT PRIMARY KEY;")
        
        #------------PARA JUNTAR DOS O MAS COLUMNAS Y AÑADIRLAS COMO UNA NUEVA COLUMNA A LA TABLA:
        cursor.execute("ALTER TABLE table5 ADD COLUMN combinada VARCHAR(50);")
        cursor.execute("UPDATE yourtable SET combined = CONCAT(hour, ' - ', order_name, ', ', finantial_status);")
        
        conn.commit()
                
except Error as e:
            print("Error en la conexion con MySQL", e)
            
            
