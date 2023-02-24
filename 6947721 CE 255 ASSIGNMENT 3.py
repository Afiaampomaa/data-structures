#6947721
#Ampomaa Afia Sarkodie
#COMPUTER APPLICATION ASSIGNMENT 3
#https://github.com/Afiaampomaa


Car =["Toyota Vitz","Buggati Chiron","Toyota Camry","Bugatti Veyron","Toyota Corolla","Chevrolet Equinox","Toyota Sienna","Toyota Land Cruiser Prado",
      "Lincoln Navigator","Toyota Tundra","Toyota Tacoma","Toyota Sequoia","Toyota Matrix","Nissan Pathfinder",
      "Nissan Sentra","Nissan Maxima","Nissan Versa","Nissan Patrol","Nissan Titan","Nissan Frotier",
      "Hyundai Accent","Hyundai Elantra","Hyundai Tucson","Hyundai Sonata","Hyundai Santa Fe","Honda Civic","Honda Accord","Honda Pilot","Honda Odyssey",
      "Mercedes-Benz C-Class"]
Models=["2001","2004","2007","2012","2019","2020","2022"]
Price=[320000,125000,440000,930000,720000,178000,522000]
CarModelPrice=[]
print("Welcome to Afia's car Dealership")
order=input("Which car would you like to buy?")
if order in Car:
   model=input("Please enter the model of the car you would like to buy.")
   if model in Models:
     if model=="2001":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2004":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2007":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2012":
      print("The price of the vehicle chosen is GHS",Price[3])     
     elif model=="2019":
      print("The price of the vehicle chosen is GHS",Price[4])
     elif model=="2020":
      print("The price of the vehicle chosen is GHS",Price[5])
     elif model=="2022":
      print("The price of the vehicle chosen is GHS",Price[6])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    