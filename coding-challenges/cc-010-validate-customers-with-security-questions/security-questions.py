# users' database - a particular index corresponds to a specific user
names = ["James", "John", "Emma"]
surnames = ["Oliver", "Smith", "Brown"]
birth_days = [15, 22, 8]
birth_months = [3, 6, 12]
birth_years = [1984, 1994, 2001]

# prompt for the user name
u_name = input("Please enter your name: ")

#Check if the name exists in the database (a list int his case).
if u_name in names:
  index = names.index(u_name)
        
  u_surname = input("Please enter your surname: ")
   #Check if the surename and username match and surname exits in the surname list.
  if surnames[index] == u_surname:
    u_birthday = input("Please enter your birthday (DD/MM/YYYY): ")
      #Check if the date is valid (length should be 10 and should have '/' in the 3rd and 5th indexes)
    if len(u_birthday) == 10 and u_birthday[2] == '/' and u_birthday[5] == '/':
    
      #Parse the given date string into day, month and year parts to be able to check if they are valid one by one from the day, month and year lists.
      u_day = u_birthday[3:5]
      u_month = u_birthday[:2]
      u_year = u_birthday[6:]
      #After confirming that all the input that is entered is correct, print "You are a customer" message.
      if int(u_day) == birth_days[index] and int(u_month) == birth_months[index] and int(u_year) == birth_years[index]:
        print("You are a customer!")
        
      else:
        print("You are not a customer!")
    else:
      print("You have entered an incorrect value!")
  else:
    print("You are not a customer!")
else:
  print("You are not a customer!")
