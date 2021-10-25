# Simple Flask Python Base Project with sqlite3 and httpAuth

 1. This application has 3 pages - Home , login , Register
 2. All the html code is in Templates folder
 3. User needs to create a user before trying to login

## Pre-Req

 - Make sure latest python is installed (version 3+)
 - Make sure git is installed in your system
 - Make sure u have stable internet connection

Note : 

 - Most of the navigation are done using Command prompt /Terminal .As this project is created using Linux . 
 - Some of the commands starting with "$" means it is executed in your terminal / Command prompt .
Example :

    $cd  /home/FlaskAuthSqlLite3
Means u need to navigate to folder "FlaskAuthSqlLite3" from your terminal / command Prompt
 

## Steps to Run

 1. Create an empty folder in your PC,
 2. $cd {inside the new folder}
 3. run command  "$git clone https://github.com/j-thepac/FlaskAuthSqlLite3"
 4. A MedicalProjectStartkit folder gets downloaded 
 5. $cd FlaskAuthSqlLite3/MedicalProjectStartkit (cd until u see requirments.txt file)
 6. $pip install -r requirments.txt
 7. $python runner.py
 8. Now the server starts to run 
Use should see message "Running on http://localhost:5050/"
 9. Open Browser and navigate to http://localhost:5050/
 10. Press ctrl+c to stop server 
