# -*- coding: utf-8 -*-
"""ITI_Python_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15smuZuZsKXis4m9A-gnVrvtoltaTldHB

Registration:
• First name
• Last name
• Email
• Password
• Confirm password
• Mobile phone [validated against Egyptian phone numbers]
"""

def startmenu():
  print("Welcome to Crowd-Funding")
  print("New to our app do you want to register? or login?")
  print("\n 1) Register \n 2) Login \n 3) Exit")
  choice = input("Please choose from menu :\n")
  if choice == "1":
    register()
  elif choice == "2":
    login()
  elif choice == "3":
    exit()

startmenu()

# Register a new user
import re
def register():
    print("\n-------------Register Form-------------\n")
    users = open("regusers.txt", "r")
    user_id = str(len(users.readlines()) + 1)
    
    first_name = input("First name: ")
    last_name = input("Last name: ")
    emails = []
    for i in users:
        fields = i.split("|")
        Email = fields[2]
        emails.append(Email)

    email = input("Email: ")
    pattern = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
    while not re.match(pattern, email):
        email =  input("Email address is invalid, Try again (ex: abc@mail.com): ")
    if email in emails:
        print("This user already exists!")
        print("\n 1) Register \n 2) Login \n ")
        choice = input("Please choose from menu :\n")
        if choice == "1":
            register()
            return
        elif choice == "2":
            login()
            return

    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    # Validate password
    while not password == confirm_password:
      confirm_password = input("Passwords don't match, Try again:")

    mobile_phone = input("Mobile phone starts with Egypt code number(+20): ")
    # Validate mobile phone number
    while not mobile_phone.startswith('+201') or len(mobile_phone) != 13:
        mobile_phone = input("Mobile phone is Invalid Try again: ")       

    # Insert user into file db
    # Open a file for appending 
    with open("regusers.txt", "a") as file:
      # Write the user input to the file
      try:
        file = open("regusers.txt", "a")
      except Exception as e:
        print(e)
      else:
      # Write the user input to the file
        file.write(user_id)
        file.write("|")
        file.write(first_name)
        file.write("|")
        file.write(last_name)
        file.write("|")
        file.write(email)
        file.write("|")
        file.write(password)
        file.write("|")
        file.write(mobile_phone)
        file.write("\n")
      print("You Registered Successfully , You may login with your account now")
      file.close()
      login()

# Login user
def login():
  print("\n-------------Login Form-------------\n")
  email = input("Email: ")
  password = input("Password: ")
  # Open the file containing the emails to be validated
  try:
    regusers_file = open('regusers.txt','r')
  except Exception as e:
    print(e)
  else:
    users = regusers_file.readlines()
    for user in users:
        userdata = user.strip("\n")
        userinfo = userdata.split("|")
        #print(userinfo)

        if userinfo[3] == email and userinfo[4] == password:
            print("Logged in successfully")
            userId = userinfo[0]
            projmenu(userId)
            break
    else:
        choice = input("Invalid Data \n 1) Try again \n 2) Register first ")
        if choice == "1":
            login()
            return
        elif choice == "2":
            register()
            return

def projmenu(userId):
    user_id = userId
    print("\n-------------Project Menu-------------\n")
    print("\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search for Project \n 6) Donate for Project \n 7) Log Out ")
    choice = input("Please choose from menu :\n")
    if choice == "1":
      createProject(user_id)
      projmenu(user_id)
    elif choice == "2":
      viewProjects()
      projmenu(user_id)
    elif choice == "3":
      edit(user_id)
      projmenu(user_id) 
    elif choice == "4":
      delete(user_id)
      projmenu(user_id)  
    elif choice == "5":
      search()
      projmenu(user_id)      
    elif choice == "6":
      fundProj()
      projmenu(user_id)
    elif choice == "7":
      exit()

import time
# Create Project
def createProject(userId):
  print("\n-------------Project Creation Form-------------\n")
  user_id = userId
  proj_title = input("Project Title: ")
  details = input("Details: ")
  total_target = input("Total Target (in EGP): ")
  start_time = input("Start Time (mm/dd/yyyy): ")
  end_time = input("End Time (mm/dd/yyyy): ")
  sum = 0
  try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')

        if valid_date1 and valid_date2:
            try:
                users_projects = open("proj_data.txt", "a")
            except Exception as e:
                print(e)
            else:
                user_data = f"{user_id}|{proj_title}|{details}|{total_target}|{start_time}|{end_time}|{sum}\n"
                users_projects.write(user_data)
                users_projects.close()
                print('Your project is created successfully')
  except Exception as e:
        print(e)
        print("Your Time format is invalid ,, Please Re-enter project creation details again:")
        createProject(user_id)

# View Projects
def viewProjects():
  print("\n-------------Current Projects-------------\n")
  try:
        users_projects = open("proj_data.txt", "r")
  except Exception as e:
        print(e)
  else:
        projects=users_projects.readlines()
        for project in projects:
            user_project = project.strip("\n")
            projinfo = user_project.split("|")
            print(projinfo)
        users_projects.close()
        return projects

# edit project
def edit(userId):
      user_id = userId
      all_projects = viewProjects()
      project_name = input("\n Select One Project To Edit:")
      matched = ""
      for j in all_projects:
            user_project = j.strip("\n")
            user_project = user_project.split("|")
            if user_project[1] == project_name and user_id == user_project[0]:
                  matched = "Done"
                  print("\n-------------Edit Menu-------------\n")
                  option = input ("\n Please Choose \n 1 for edit project title \n 2 for edit project details \n 3 for edit project target \n 4 for edit project start date \n 5 for edit project end date \n 6 for edit all \n")
                  if option == "1":
                      newtitle = input("Please Enter new title for project: ")
                      user_project[1] = newtitle
                  elif option == "2":
                      proj_detail = input("Please Enter proj_detail for project: ")
                      user_project[2] = proj_detail  
                  elif option == "3":
                      proj_target = input ("Please Enter proj_target for project: ")
                      user_project[3] = proj_target
                  elif option == "4":
                      proj_start = input("Please Enter proj_start for project: ")
                      user_project[4] = proj_start
                  elif option == "5":
                      proj_end = input("Please Enter proj_end for project: ")
                      user_project[5] = proj_end
                  elif option == "6":
                      newtitle = input("Please Enter new title for project: ")
                      user_project[1] = newtitle
                      proj_detail = input("Please Enter proj_detail for project: ")
                      user_project[2] = proj_detail
                      proj_target = input("Please Enter proj_target for project: ")
                      user_project[3] = proj_target
                      proj_start = input("Please Enter proj_start for project: ")
                      user_project[4] = proj_start
                      proj_end = input("Please Enter proj_end for project: ")
                      user_project[5] = proj_end
                      
                  updated_project = "|".join(user_project)
                  updated_project = f"{updated_project}\n"
                  proj_index = all_projects.index(j)
                  #print (proj_index)
                  all_projects[proj_index] = updated_project
                  print("Projects Updated Successfully")
                  break
      if (matched != "Done"):    
        print("You are not allowed to edit this project")    
      w = open("proj_data.txt", "w") 
      w.writelines(all_projects)
      w.close()

# delete project
def delete(userId):
    user_id = userId
    all_projects = viewProjects()
    del_proj = input ("Enter Project Name You Want to Delete It: ")
    matched = ""
    for proj in all_projects:
          user_project = proj.strip("\n")
          user_project = user_project.split("|")
          if user_project[1] == del_proj and user_id == user_project[0]:
                matched = "Done"
                all_projects.remove(proj)
                print("Project Deleted Successfully")
                break
    if (matched != "Done"):    
      print("You are not allowed to delete this project")    
    w = open("proj_data.txt", "w") 
    w.writelines(all_projects)
    w.close()

# Search For Projects
def search():
   all_projects = viewProjects()
   matched = ""
   date = input("\nEnter project date (mm/dd/yyyy) :")
   date_pattern = r"\d{2}/\d{2}/\d{4}"
   match = re.match(date_pattern, date)
   while not match:
        date = input("\nInvalid Format, Enter project date (mm/dd/yyyy) :")
        match = re.match(date_pattern, date)
   for d in all_projects:
        user_project = d.strip("\n")
        user_project = user_project.split("|")
        if user_project[4] == date or user_project[5] == date:
          matched = "Done"    
          print(user_project)
          break 
   if matched != "Done":
      print("Date not found")

#Fund a project
def fundProj():
  all_projects = viewProjects()
  fproj = input ("Enter Project Name You Want to Fund: ")
  matched = ""
  for proj in all_projects:
        user_project = proj.strip("\n")
        user_project = user_project.split("|")
        if user_project[1] == fproj :
              matched = "Done"
              donated_money = int(input("Please Enter How much you will donate (EGP)"))
              u = int(user_project[6])
              u += donated_money
              user_project[6] = str(u)
              updated_project = "|".join(user_project)
              updated_project = f"{updated_project}\n"
              proj_index = all_projects.index(proj)
              all_projects[proj_index] = updated_project
              print("You Funded this project Successfully")
              break
  if (matched != "Done"):    
    print("There is no Project with this Title")    
  w = open("proj_data.txt", "w") 
  w.writelines(all_projects)
  w.close()