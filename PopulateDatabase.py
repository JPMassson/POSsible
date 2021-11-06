import mysql.connector

mydb = mysql.connector.Connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "POSDatabase"
)

print(mydb)

# create cursor instance
my_cursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS Customer, Products, Promotions, Staff, Supplier, Warehouse, Invoice, Order_Placed, Tracking, Feedback, Order_Status, Promotion"
my_cursor.execute(sql)

#create database
#my_cursor.execute("CREATE DATABASE POSDatabase")


#shows database
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

# create Products table
my_cursor.execute("CREATE TABLE Products (Product_ID INTEGER(12) PRIMARY KEY, Product_Name VARCHAR(255), Product_Brand VARCHAR(255), Product_Type VARCHAR(255), Product_Description VARCHAR(255)\
, Product_Per_Unit_Cost float(53), Stock_Level INTEGER(12))")
Product_info1 = "INSERT INTO Products (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567891, 'VB Schooner', 'CUB', 'Beer', 'Local Australian Beer', 7.0, 300 \
), (1234567890, 'Carlton Schooner', 'CUB', 'Beer', 'Local Australian Beer', 7.0, 250), (1234567889, 'Tooheys New Schooner', 'Lion', 'Beer', 'Local Australian Beer', 7.0, 500) , (1234567888, \
'XXXX Schooner', 'Lion', 'Beer', 'Mid Strength Beer', 6.80, 500), (1234567887, 'Furphy Schooner', 'Lion', 'Beer', 'Australian Craft Beer', 8.80, 300 \
), (1234567886, 'Kosciuszko Schooner', 'Lion', 'Beer', 'Australian Craft Beer', 8.80, 300 \
) "
Product_info2 = "INSERT INTO Products (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567885, 'Bottle of Rosé', 'Estate Wines', 'Rosé', 'French Rosé', 40.0, 300 \
), (1234567884, 'Bottle of Champagne', 'Estate Wines', 'Sparkling Wine', 'French Champagne', 62.0, 250), (1234567883, 'Glass of Shiraz', 'Estate Wines', 'Red Wine', 'Australian Shiraz', 8.80, 500) , (1234567882, \
'Bottle of Shiraz', 'Estate Wines', 'Red Wine', 'Australian Shiraz ', 48.0, 500), (1234567881, 'Glass of Chardonnay', 'Estate Wines', 'White Wine', 'Australian Chardonnay', 8.50, 300 \
), (1234567880, 'Bottle of Chardonnay', 'Estate Wines', 'White Wine', 'Australian Chardonnay', 45.0, 300 \
) "
Product_info3 = "INSERT INTO Products (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567879, 'Bundaberg OP Nip', 'Paramount', 'Spirit', 'Rum', 8.0, 300 \
), (1234567878, 'George Dickel Nip', 'Diageo', 'Spirit', 'Bourbon', 8.0, 250), (1234567877, 'Smirnoff Nip', 'Paramount', 'Spirit', 'Vodka', 8.0, 500) , (1234567876, \
'Gordons Nip', 'Diageo', 'Spirit', 'Gin', 48.0, 500), (1234567875, 'Don Julio Blanco Nip', 'Diageo', 'Spirit', 'Tequilla', 8.0, 300 \
), (1234567874, 'Johnnie Walker Red Nip', 'Paramount', 'Spirit', 'Whiskey', 8.0, 300 \
) "
Product_info4 = "INSERT INTO Products (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567873, 'Margarita', 'Parkhouse', 'Cocktail', 'Classic Coktails', 15.0, 300 \
), (1234567872, 'Cosmopolitan', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 15.0, 250), (1234567871, 'Mojito', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 16.0, 500) , (1234567870, \
'Old Fashioned', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 18.0, 500), (1234567869, 'Negroni', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 19.0, 300 \
), (1234567868, 'Espresso Martini', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 18.0, 300 \
) "
my_cursor.execute(Product_info1)
mydb.commit()
my_cursor.execute(Product_info2)
mydb.commit()
my_cursor.execute(Product_info3)
mydb.commit()
my_cursor.execute(Product_info4)
mydb.commit()


# create warehouse table
my_cursor.execute("CREATE TABLE Warehouse (Warehouse_ID INTEGER(9) PRIMARY KEY, Warehouse_Name VARCHAR(255), Warehouse_Phone VARCHAR(255), Warehouse_Building_No INTEGER(255), Warehouse_Street VARCHAR(255)\
, Warehouse_Suburb VARCHAR(255), Warehouse_City VARCHAR(255), Warehouse_State VARCHAR(255), Warehouse_ZipCode INTEGER(10))")
Warehouse_info = "INSERT INTO Warehouse (Warehouse_ID, Warehouse_Name, Warehouse_Phone, Warehouse_Building_No, Warehouse_Street, Warehouse_Suburb, Warehouse_City, Warehouse_State,\
 Warehouse_ZipCode) VALUES (24382949, 'Dockland Warehouse'\
, '6144445302', 34, 'Carlton', 'Merrylands', 'Sydney', 'NSW', 2438), (24382447, 'Campsie Warehouse'\
, '61488010926', 52, 'First Ave', 'Campsie', 'Sydney', 'NSW', 2194)"
my_cursor.execute(Warehouse_info)
mydb.commit()

# create Supplier table
my_cursor.execute("CREATE TABLE Supplier (Supplier_ID INTEGER(10) PRIMARY KEY, Supplier_Name VARCHAR(255), Supplier_Phone VARCHAR(255), Supplier_Building_No INTEGER(255), Supplier_Street VARCHAR(255), Supplier_Suburb VARCHAR(255)\
, Supplier_City VARCHAR(255), Supplier_State VARCHAR(255), Supplier_ZipCode INTEGER(10))")
Supplier_info = "INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Phone, Supplier_Building_No, Supplier_Street, Supplier_Suburb, Supplier_City, Supplier_State, Supplier_ZipCode) VALUES (11234478, 'Tooheys'\
, '6144445889', 29, 'Nyrang St', 'Lidcombe ', 'Sydney', 'NSW', 2141), (24382553, 'dan murphys warehouse'\
, '61488010002', 10, 'Fountain St', 'Alexandria', 'Sydney', 'NSW', 2015)"
my_cursor.execute(Supplier_info)
mydb.commit()

#create Customer table
my_cursor.execute("CREATE TABLE Customer (Customer_ID INTEGER(11) PRIMARY KEY, Customer_F_Name VARCHAR(20), Customer_L_Name VARCHAR(20), Customer_Email_ID VARCHAR(255), Customer_Phone_Number VARCHAR(11), Customer_Membership INTEGER(11))")
Customer_info = "INSERT INTO Customer (Customer_ID, Customer_F_Name, Customer_L_Name, Customer_Email_ID, Customer_Phone_Number, Customer_Membership) VALUES (987654321, 'Dave', 'Jones', 'DJones12@gmail.com', '61448801926', 123456789), \
(55432157, 'Bryce', 'Musk', 'BMusk115@gmail.com', '61448801884', 123456788), (45631278, 'Sarah', 'Musk', 'SMusk115@gmail.com', '61445521348', 123456777)"
my_cursor.execute(Customer_info)
mydb.commit()


# create Staff table
my_cursor.execute("CREATE TABLE Staff (Staff_ID INTEGER(7) PRIMARY KEY, Staff_F_Name VARCHAR(20), Staff_L_Name VARCHAR(20), Staff_Type VARCHAR(1), Staff_Email_ID VARCHAR(255), Staff_Phone_Number VARCHAR(12))")
Staff_info = "INSERT INTO Staff (Staff_ID, Staff_F_Name, Staff_L_Name, Staff_Type, Staff_Email_ID, Staff_Phone_Number) VALUES (123456, 'Callum', 'Freeburn', 'U', 'CFreeburn112@gmail.com', 6144821325),\
(654321, 'Hamish', 'Smith', 'A', 'HSmith@gmail.com', 61477412635)"
my_cursor.execute(Staff_info)
mydb.commit()

## CREATE Invoice table
my_cursor.execute("CREATE TABLE Invoice (Invoice_No INTEGER(255) PRIMARY KEY, Invoice_Date DATETIME(6), Invoice_Amount NUMERIC(65))")
Invoice_info = "INSERT INTO Invoice (Invoice_No, Invoice_Date, Invoice_Amount) VALUES (15564, '2020-08-22  12:55:14', 204.55), (16567, '2019-07-18  08:16:20', 88.9), (17986, '2021-05-03  01:18:08', 507), (18097, '2019-07-18  08:16:20', 88.9)"
my_cursor.execute(Invoice_info)
mydb.commit()

## CREATE Order table
my_cursor.execute("CREATE TABLE Order_Placed (Order_No INTEGER(255) PRIMARY KEY, Order_Til_No INTEGER(50), Order_Date DATETIME(6))")
Order_Placed_info = "INSERT INTO Order_Placed (Order_No, Order_Til_No, Order_Date) VALUES (456665, 12, '2017-12-24  14:12:18'), (68565, 5, '2016-08-23  15:08:12'), (77876, 2, '2019-02-20  20:13:04'), (89548, 14, '2021-06-14  07:09:55')"
my_cursor.execute(Order_Placed_info)
mydb.commit()

## CREATE Feedback table
my_cursor.execute("CREATE TABLE Feedback (Feedback_No INTEGER(255) PRIMARY KEY, Feedback_Rating INTEGER(20), Feedback_Description CHAR(100))")
Feedback_info = "INSERT INTO FEEDBACK (Feedback_No, Feedback_Rating, Feedback_Description) VALUES (2334, 7, 'it was very good'), (3347, 5, 'could improve service'), (4567, 8, 'a very postive experience'), (6923, 10, 'would recommend')"
my_cursor.execute(Feedback_info)
mydb.commit()


## CREATE OrderStatus table
my_cursor.execute("CREATE TABLE Order_Status (Status_ID INTEGER(255) PRIMARY KEY, Status_Name VARCHAR(40), Status_Description CHAR(100))")
Feedback_info = "INSERT INTO Order_Status (Status_ID, Status_Name, Status_Description) VALUES (679, 'Order Recieved', 'Expected to leave warehouse on Monday'), (786, 'Delivered', 'Left outside door'),  (884, 'In-transit', 'Fragile - Handle with care'), (336, 'Delivered', 'Left outside door')"
my_cursor.execute(Feedback_info)
mydb.commit()


## CREATE Promotion table
my_cursor.execute("CREATE TABLE Promotion (Promo_ID INTEGER(7) PRIMARY KEY, Promo_Description VARCHAR(255), Promo_Start_Date VARCHAR(100), Promo_End_Date VARCHAR(255), Promo_Eligibility BOOLEAN)")
Promotion_info = "INSERT INTO Promotion (Promo_ID, Promo_Description, Promo_Start_Date, Promo_End_Date, Promo_Eligibility) VALUES (657489, '10% off on all Heineken products', '2021-08-24 05:00:00', '2021-09-01 05:00:00', False)"
my_cursor.execute(Promotion_info)
mydb.commit()



# get all product ids from table
# my_cursor = mydb.cursor()
# my_cursor.execute("SELECT Product_ID FROM products")
# myresult = my_cursor.fetchall()
# for x in myresult:
# 	print(x)



## to edit or update item information
# my_cursor = mydb.cursor()
# sql = "UPDATE Products SET Product_Per_Unit_Cost = Product_Per_Unit_Cost + 1 WHERE Product_ID = '115'"
# my_cursor.execute(sql)
# mydb.commit()
# print(my_cursor.rowcount, "record(s) affected")

#show list of tables
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table)

#Function that gets entire row from SQL table using Primary_Key
Table = 'Products'
Primary_Key = 'Product_ID'
Primary_Key_Value = '1234567890'
sql_select_Query = "SELECT * FROM " + Table + " WHERE " + Primary_Key + "=" + Primary_Key_Value
my_cursor.execute(sql_select_Query)
# get all records
records = my_cursor.fetchall()
print("Total number of rows in table: ", my_cursor.rowcount)

print(type(records))

print("\nPrinting each row")
for row in records:
    print(row)




