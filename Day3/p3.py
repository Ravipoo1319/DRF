def dispaly_details(*args):
    print(args) # tuples
    first_name,last_name,city = args
    print("Firs name : ",first_name)
    print("Last Name : ",last_name)
    print("City :",city)
    
dispaly_details("Ravindra", "Pawar","Pune")