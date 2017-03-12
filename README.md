# Indoor-positioning-system-using-WiFi
This was a course project under Digital Communications course.
This project contains two files:

APinfo.py ==> This python script will gather the details of all the available access points within the range of the laptop. This will then pass the results will be used by the script Position.py
              Check WiFiApp.png for the results of APinfo.py under the test environment

Position.py ==> This python script uses the details of the distance calculated by the APinfo.py. The three nearest access points will be used as reference (where they are assigned a defined set of coordinates). The location of the user will then be estimated using the trilateration approach and the co-ordinates of the user are then calculated accordingly.
            ==> Before using Postion.py make sure matplotlib library is installed else install it using "sudo pip install matplotlib"
                Check Pos.png for the results of Position.py under the test environment
