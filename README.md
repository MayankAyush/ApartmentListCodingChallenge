# ApartmentListCodingChallenge

Run this code on last Friday of every month to create random groups that increases interactivity between existing and new employees through an outdoor lunch
Instructions:
Command to run the code: python Friday_Lunch.py
Please include the NewEmployeeList.txt,EmployeeLunchList.txt within the same directory as the code

Functionality:
  3 files have been included: 
    NewEmployeeList.txt: This has information about new employees. 
    EmployeeLunchList.txt: This has all the employees going for lunch.
    Friday_Lunch.py file contans the code to be run

  Functions included in the code:
    read_lunchlist:function to get everyone going for lunch
    random_group:create random groups of size n(3,4,or 5)
    generate_groups:generate the groups and identify anyone left alone and assign them to one of the groups so no one is left
  
  Assumption:
    The NewEmployeeList.txt should not contain records for existing employees else the new run will contain duplicates

  OutSide the scope:
    Add the logic to check for existing records from NewEmployeeList.txt in EmployeeLunchList.txt, this will futureproof the    code against the old records being present in NewEmployeeList.txt
  
  
