print("Test")
#dictionary datatype deos not allow duplicate values
# it uses key and values method
#creating a dictionary datatype
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
