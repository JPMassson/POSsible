# POSsible
POSsible application and database. Point of Sales Data System Spring 2021  
**Front of House Application**  
In order to install and run the FOH applications of the POSsible data system you will need to have all the files from this repository downloaded.  
The 4 files that will be used for the FOH application is:  
CreateDatabase.py  
PopulateDatabase.py  
Registerintegrate1.py  
Loginintegration.py  

**Prerequisite**  
You will need to have python and MySQL running a localhost in order to run the code.  
The python packages needed are: mysql-connector-python==8.0.26  
This package should be installed from installing MySQL. If it's not installed, you can use the command: pip install mysql-connector-python  

**Step 1**  
To create the database open the CreateDatabase.py file. Fill in the Database connection details.  
host= "localhost" (Should remain as a localhost if you're running a localhost server)  
user= "root" (Update to the name of your MySQL connection username)  
passwd= "root" (Update to the password of your MySQL connection)   
With the code updated to your MySQL connection settings, save and run the file.  
This should then create a database on your MySQL localhost named POSDatabase  

**Step 2**
With the database created from the CreateDatabase.py file, the data needs to be populated. This is done through the PopulateDatabase.py file.  
This file will need the MySQL connections updated if necessary.  
user= "root" (Update to the name of your MySQL connection username)  
passwd= "root" (Update to the password of your MySQL connection)  
database= "POSDatabase" (Should be POSDatabase if you left the database name the same in the previous file)  
With the connections updated, save and run the file. This should popualate the database with the necessary data  

**Step 3**
With the data created, the Loginintegration.py file can be opened. This file will run the POSsible interface. Ensure that the connections are up to date for your MySQL connection.
user= "root" (Update to the name of your MySQL connection username)  
passwd= "root" (Update to the password of your MySQL connection)  
database= "POSDatabase" (Should be POSDatabase if you left the database name the same in the previous file)  
After this save and exit the file. 
Note: Ensure the images from the repositroy are in the same directory as the code to allow for proper compiling. 

**Step 4**
Now you can open the Registerintegrate1.py file. This file can be compiled without any edits. This should launch the Login/register feature.  
Use the register feature to create a user. Once a user has been created you can login with the user details.  
