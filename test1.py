print("this is a test1 file")

personDetails={"name":"Anu",
               "age": 30,
               "Field":"IT"}
print(personDetails)

#add new key values and pairs
personDetails["hobby"]="Learning"
print(personDetails)
personDetails.update({"location" : "japan"})
print(personDetails)

#removing values using pop function
personDetails.pop("name") # removes name key from dictionary 
print(personDetails)
personDetails.popitem() # removes last key from dictionary
print(personDetails)
