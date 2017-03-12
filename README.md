# Indoor-positioning-system-using-WiFi
This was a course project under Digital Communications course.
This project contains two files:

APinfo.py ==> This python script will gather the details of all the available access points within the range of the laptop. This will then pass the results will be used by the script Position.py

Position.py ==> This python script uses the details of the distance calculated by the APinfo.py. The three nearest access points will be used as reference (where they are assigned a defined set of coordinates). The location of the user will then be estimated using the trilateration approach and the co-ordinates of the user are then calculated accordingly.

