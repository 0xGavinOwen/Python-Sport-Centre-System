def goat(): #
    print("\n\t-------------------------------")
    print("\tG.O.A.T CHAMPIONS SPORT ACADEMY")
    print("\t-------------------------------\n\n")

def future():#
    print("Hi future champ!!!\n")
    

def role():#
    goat()
    print("1. admin")
    print("2. students")
    print("3. exit")

    start = int(input("\nEnter your choice: "))

    if(start == 1):
        admin_login()
    elif(start == 2):
        students()
    elif(start == 3):
        keluar()


def keluar():#
    goat()
    print("Goodbye and have a nice day!!")

def admin_login():#
    goat()
    print("Please enter the log-in password")
    login = int(input("Log-In: "))
    if(login == 888):
        admin()
    else:
        login2 =int(input("wrong password, enter any key to re-log in or any 9 to exit:"))
        if(login2 == 9):
            keluar()
        else:
            admin_login()
        
def admin():#
    goat()
    print("Hi admin, what do you wanna do?\n")
    print("1. Add Records")
    print("2. Display  All Records")
    print("3. Search Specific Records")
    print("4. Sort And Display Records")
    print("5. Modify Record")
    print("6. Students feedback")
    print("7. Log-Out") 
    admin_pick = int(input("\nEnter your choice's number: "))

    if(admin_pick == 1):
        add_records()
        
    elif(admin_pick == 2):
        display_records()
        
    elif(admin_pick == 3):
        search_records()

    elif(admin_pick == 4):
        sort_records()

    elif(admin_pick == 5):
        modify_records()

    elif(admin_pick == 6):
        students_feedback()

    else:
        role()

def add_records():#
    goat()
    print("Hi admin, what records do you want to add?\n")
    print("1. Coach")
    print("2. Sport")
    print("3. Sport schedule")
    print("4. Return")
    add_pick = int(input("Enter your choice's number: "))

    if(add_pick == 1):
        add_coach()
        
    elif(add_pick == 2):
        add_sport()
        
    elif(add_pick == 3):
        add_schedule()

    else:
        admin()

def add_coach():#
    myfile = open ("coach_record.txt","a")
    myfile.close()
    myfile = open ("coach_record.txt","r")    
    goat()
    
    print("Please enter coach detail\n") 
    coach_id = str(input("Coach id: "))
    for line in myfile: #ngecek id
        data = line.rstrip()
        x = data.split(",")
        cid = x[0] 
        while (coach_id == cid):
            print("ID has been used, please re enter ID")
            coach_id = str(input("Coach id: "))               
    coach_name = str(input("Coach name: "))
    coach_joined = str(input("Join date(dd/mm/yy): "))
    coach_terminated = str(input("Left date(dd/mm/yy) or (-) if coach still present: "))
    coach_hourly = int(input("Hourly rate(MYR): "))
    while (coach_hourly>500 or coach_hourly<100):
        print("Rate is out of range, re-input rate")
        coach_hourly = int(input("Hourly rate(MYR): "))
    coach_hourly = str(coach_hourly)
    coach_phone = str(input("Phone number: "))
    coach_address = str(input("Address: "))
    coach_sid = str(input("Sport ID: "))
    coach_sname = str(input("Sport name: "))
    print("Bali/Jakarta/Surabaya")
    coach_slocation = str(input("Sport location: "))
    myfile.close()

    myfile = open ("coach_record.txt","a")                  
    myfile.write(coach_id+","+coach_name+","+coach_joined+","+coach_terminated
                    +","+coach_hourly+","+coach_phone+","+coach_address
                    +","+coach_sid+","+coach_sname+","+coach_slocation
                    +",5\n")
    myfile.close()

    choice=int(input("\nEnter any key to add another record or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        add_coach()

def add_sport():#
    myfile = open("sport_record.txt","a")
    myfile.close()
    
    myfile = open("sport_record.txt","r")
    goat()
    print("please enter sports detail\n")
    sport_code = str(input("Sport ID: "))
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        while (sport_code == lis[0]):
            print("ID has been used, please re enter ID")
            sport_code = str(input("Sport ID: "))               
    sport_name = str(input("Sport name: "))
    print("Bali/Jakarta/Surabaya")
    sport_location = str(input("Location: "))
    myfile.close()
    
    myfile = open("sport_record.txt","a")
    myfile.write(sport_code+","+sport_name+","+sport_location+"\n")
    myfile.close()

    print("\nEnter any key to add another sport data, enter 9 to exit")
    pick = int(input("Enter your choice: "))

    choice=int(input("\nEnter any key to add another record or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        add_sport()

def add_schedule():#
    myfile = open("sschedule_record.txt","a")
    goat()
    print("Please enter sports schedule detail\n")
    sschedule_id = str(input("Sport ID: "))
    sschedule_name = str(input("Sport name: "))
    sschedule_day = str(input("Day: "))
    sschedule_start = str(input("Time start: "))
    sschedule_duration = str(input("Duration: "))

    myfile.write(sschedule_id+","+sschedule_name+","+sschedule_day
                +","+sschedule_start+","+sschedule_duration+"\n")
    myfile.close()

    choice=int(input("\nEnter any key to add another record or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        add_schedule()

def display_records():#
    goat()
    print("Hi admin, what records do you want to display?\n")
    print("1. Coach")
    print("2. Sport")
    print("3. Sport schedule")
    print("4. Registered students")
    print("5. Return")
    display_pick = int(input("Enter your choice: "))

    if(display_pick == 1):
        display_coach()

    elif(display_pick == 2):
        display_sport()

    elif(display_pick == 3):
        display_schedule()

    elif(display_pick == 4):
        display_students()

    else:
        admin()

def display_coach():#
    goat()
    print("These are all the the coach record\n")
    print("ID\tName\tJoin\tLeft\tRate\tPhone\tAddress\tSID\tSport\tLocation\tStar")
    myfile = open ("coach_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[0]+"\t"+lis[1]+"\t"+lis[2]+"\t"+lis[3]
              +"\t"+lis[4]+"\t"+lis[5]+"\t"+lis[6]
              +"\t"+lis[7]+"\t"+lis[8]+"\t"+lis[9]
              +"\t"+lis[10])
    myfile.close

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        display_coach()


    
def display_sport():#
    goat()
    print("These are all the sport record\n")
    print("ID\tName\tLocation\n")
    myfile = open ("sport_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[0]+"\t"+lis[1]+"\t"+lis[2])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        display_sport()


def display_schedule():#
    goat()
    print("These are all the sport shcedule\n")
    print("ID\tName\tDay\tTime\tDuration\n")
    myfile = open ("sschedule_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[0]+"\t"+lis[1]+"\t"+lis[2]+"\t"+lis[3]+"\t"+lis[4])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        display_schedule()


def display_students():#
    goat()
    print("These are all the records of the registered students\n")
    print("ID\tName\tAddress\tPhone number\tDOB\tSport")
    myfile = open("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[2]+"\t"+lis[3]+"\t"+lis[4]+"\t"+lis[5]
              +"\t"+lis[6]+"\t"+lis[7])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        display_students()


def search_records():#
    goat()
    print("Hi admin, what records do you want to search?\n")
    print("1. Coach by coach ID")
    print("2. Coach by overall performance(stars)")
    print("3. Sport by sport ID")
    print("4. Student by student ID")
    print("5. Return")
    search_pick = int(input("Enter your choice: "))

    if(search_pick == 1):
        search_coachid()

    elif(search_pick == 2):
        search_coachstars()

    elif(search_pick == 3):
        search_sport()

    elif(search_pick == 4):
        search_students()

    else:
        admin()

def search_coachid():#
    goat()
    print("Please enter coach ID to be search")
    cid = str(input("Enter coach ID: "))
    myfile = open("coach_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        if (cid == x):
            print("\nCoach ID: "+lis[0])
            print("Name: "+lis[1])
            print("Join date: "+lis[2])
            print("Left date: "+lis[3])
            print("Hourly rate: "+lis[4])
            print("Phone number: "+lis[5])
            print("Address: "+lis[6])
            print("Sport ID: "+lis[7])
            print("Sport name: "+lis[8])
            print("Sport location: "+lis[9])      
    myfile.close()

    choice=int(input("\nEnter any key to search another coach or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        search_coachid()

def search_coachstars():#
    goat()
    print("Please enter star rating to be search")
    rating = int(input("In a range of 1-5 stars, enter star rating: "))
    while (rating>5 or rating<1):
        print("Rating is out of range, re-input rating")
        rating = int(input("In a range of 1-5 stars, enter star rating: "))
    rating = str(rating)
    myfile = open("coach_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if (rating == lis[10]):
            print("\nCoach ID: "+lis[0])
            print("Name: "+lis[1])
            print("Join date: "+lis[2])
            print("Left date: "+lis[3])
            print("Hourly rate: "+lis[4])
            print("Phone number: "+lis[5])
            print("Address: "+lis[6])
            print("Sport ID: "+lis[7])
            print("Sport name: "+lis[8])
            print("Sport location: "+lis[9])
            print("Star rating: "+lis[10])
    myfile.close()

    choice=int(input("\nEnter any key to search another coach or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        search_coachstars()

def search_sport():#
    goat()
    print("Please enter sport ID to be search")
    sid = str(input("Enter sport ID: "))

    myfile = open("sport_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        if (sid == x):
            print("\nSport ID: "+lis[0])
            print("Sport name: "+lis[1])
            print("Location: "+lis[2])
    myfile.close()

    choice=int(input("\nEnter any key to search another sport or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        search_sport()

def search_students():#
    goat()
    print("please enter student ID to be search")
    sid = str(input("Enter student ID: "))

    myfile = open("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[2]
        if (sid == x):
            print("\nStudent ID: "+lis[2])
            print("Name: "+lis[3])
            print("Address: "+lis[4])
            print("Phone number: "+lis[5])
            print("Date of birth: "+lis[6])
            print("Sport name: "+lis[7])
    myfile.close()

    choice=int(input("\nEnter any key to search another students or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        search_students()

def sort_records():#
    goat()
    print("Hi admin, what records do you want to sort?\n")
    print("1. Coach in ascending order by names")
    print("2. Coach hourly pay rate in ascending order")
    print("3. Coach performance(stars) in ascending order")
    print("4. Return")
    sort_pick = int(input("Enter your choice: "))

    if(sort_pick == 1):
        sort_coachnames()

    elif(sort_pick == 2):
        sort_coachrate()

    elif(sort_pick == 3):
        sort_coachstars()
        
    else:
        admin()

def sort_coachnames():#
    goat()
    print("List of coaches in ascending order by names\n")
    print("ID,Name,Join,Left,Rate,Phone,Address,SID,Sport,Location,Star\n")
    count = 0
    myfile = open("coach_record.txt","r")
    for line in myfile:
        count += 1
    myfile.close()

    myfile = open("coach_record.txt","r")
    string_list = myfile.readlines()
    data_min=""
    for i in range (0, count):
        data1 = string_list[i].split(",")
        name1 = data1[1]
        for j in range (i,count):
            data2 = string_list[j].split(",")
            name2 = data2[1]
            if(name1 > name2):
                data_min = string_list[j]
                string_list[j]=string_list[i]
                string_list[i]=data_min
                data1 = string_list[i].split(",")
                name1 = data1[1]
            else:
                data_min=string_list[i]
        print(data_min)
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        sort_coachnames()

        
def sort_coachrate():#
    goat()
    print("List of coaches in ascending order by hourly pay rate\n")
    print("ID,Name,Join,Left,Rate,Phone,Address,SID,Sport,Location,Star\n")
    count = 0
    myfile = open("coach_record.txt","r")
    for line in myfile:
        count += 1
    myfile.close()

    myfile = open("coach_record.txt","r")
    string_list = myfile.readlines()
    data_min=""
    for i in range (0, count):
        data1 = string_list[i].split(",")
        name1 = data1[4]
        for j in range (i,count):
            data2 = string_list[j].split(",")
            name2 = data2[4]
            if(name1 > name2):
                data_min = string_list[j]
                string_list[j]=string_list[i]
                string_list[i]=data_min
                data1 = string_list[i].split(",")
                name1 = data1[4]
            else:
                data_min=string_list[i]
        print(data_min)
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        sort_coachrate()


def sort_coachstars():#
    goat()
    print("List of coaches in ascending order by overall performance rate\n")
    print("ID,Name,Join,Left,Rate,Phone,Address,SID,Sport,Location,Star\n")
    count = 0
    myfile = open("coach_record.txt","r")
    for line in myfile:
        count += 1
    myfile.close()

    myfile = open("coach_record.txt","r")
    string_list = myfile.readlines()
    data_min=""
    for i in range (0, count):
        data1 = string_list[i].split(",")
        name1 = data1[10]
        for j in range (i,count):
            data2 = string_list[j].split(",")
            name2 = data2[10]
            if(name1 > name2):
                data_min = string_list[j]
                string_list[j]=string_list[i]
                string_list[i]=data_min
                data1 = string_list[i].split(",")
                name1 = data1[10]
            else:
                data_min=string_list[i]
        print(data_min)
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        sort_coachstars()

def modify_records():#
    goat()
    print("Hi admin, what records do you want to modify?\n")
    print("1. Coach records")
    print("2. Sport records")
    print("3. Sport schedule")
    print("4. Return")
    modify_pick = int(input("Enter your choice: "))

    if(modify_pick == 1):
        modify_coach()

    elif(modify_pick == 2):
        modify_sport()

    elif(modify_pick == 3):
        modify_schedule()
        
    else:
        admin()

def modify_coach():#
    goat()
    print("Please enter coach id to be modified")
    cid = str(input("Enter coach ID: "))

    myfile = open("coach_record.txt","r")
    terdata = ""
    new_data =""
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        if (cid == x):
            def coach():
                print("\n1. Coach ID: "+lis[0])
                print("2. Name: "+lis[1])
                print("3. Join date: "+lis[2])
                print("4. Left date: "+lis[3])
                print("5. Hourly rate: "+lis[4])
                print("6. Phone number: "+lis[5])
                print("7. Address: "+lis[6])
                print("8. Sport ID: "+lis[7])
                print("9. Sport name: "+lis[8])
                print("10. Sport location: "+lis[9])
            coach()

            ganti = int(input("\nEnter which number do you want to modified: "))
            terganti= str(input("Enter the value: "))
            lis[ganti-1]=terganti #buat pilih
            print("\nYour data has been modified")
            coach()
            
            terdata = (lis[0]+","+lis[1]+","+lis[2]+","+lis[3]+","+lis[4]+","+lis[5]+","+lis[6]
                            +","+lis[7]+","+lis[8]+","+lis[9]+","+lis[10]+"\n")
            new_data = (new_data+terdata)
        else:
            new_data = (new_data+data+"\n")
    myfile.close()

    myfile = open("coach_record.txt","w")
    myfile.write(new_data)
    myfile.close()

    choice=int(input("\nEnter any key to modify another coach or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        modify_coach()


def modify_sport():#
    goat()
    print("Please enter sport id to be modified")
    sid = str(input("Enter sport ID: "))

    myfile = open("sport_record.txt","r")
    terdata = ""
    new_data = ""
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        if (sid == x):
            def sport():
                print("\n1. Sport ID: "+lis[0])
                print("2. Sport name: "+lis[1])
                print("3. Location: "+lis[2])
            sport()

            ganti = int(input("\nEnter which number you want to modified: "))
            terganti = str(input("Enter the value: "))
            lis[ganti-1] = terganti
            print("\nYour data has been modified")
            sport()

            terdata = (lis[0]+","+lis[1]+","+lis[2]+"\n")
            new_data = (new_data+terdata)
        else:
            new_data = (new_data+data+"\n")
    myfile.close()

    myfile = open("sport_record.txt","w")
    myfile.write(new_data)
    myfile.close()

    choice=int(input("\nEnter any key to modify another sport or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        modify_sport()

def modify_schedule():#
    print("Please enter sport ID to modified it's schedule")
    ssid = str(input("Enter sport ID: "))

    myfile =open("sschedule_record.txt","r")
    terdata = ""
    new_data = ""
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        if (ssid == x):
            def sschedule():
                print("\n1. Sport ID: "+lis[0])
                print("2. Sport name: "+lis[1])
                print("3. Day: "+lis[2])
                print("4. Time: "+lis[3])
                print("5. Duration: "+lis[4])
            sschedule()

            ganti = int(input("\nEnter which number you want to modified: "))
            terganti = str(input("Enter the value: "))
            lis[ganti-1] = terganti
            print("\nYour data has been modified")
            sschedule()

            terdata = (lis[0]+","+lis[1]+","+lis[2]+","+lis[3]+","+lis[4]+"\n")
            new_data = (new_data+terdata)
        else:
            new_data = (new_data+data+"\n")
    myfile.close()

    myfile = open("sschedule_record.txt","w")
    myfile.write(new_data)
    myfile.close()

    choice=int(input("\nEnter any key to modify another schedule or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        modify_schedule()


def students_feedback():#
    goat()
    print("Hi admin,these are all the students feedback\n")
    myfile = open("feedback.txt","r")
    print(myfile.read())
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        admin()
    else:
        students_feedback()

def students():#
    goat()
    future()
    print("1. Show sport list")
    print("2. Show sport schedule")
    print("3. Login")
    print("4. Register")
    print("5. Exit")
    students_pick = int(input("Enter your choice's number: "))

    if(students_pick == 1):
        show_sport()
    elif(students_pick == 2):
        show_schedule()
    elif(students_pick == 3):
        students_login()
    elif(students_pick == 4):
        students_register()
    else:
        role()

def show_sport():#
    goat()
    print("These are all the sport list\n")
    print("ID\tName\tLocation\n")
    myfile = open ("sport_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[0]+"\t"+lis[1]+"\t"+lis[2])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        students()
    else:
        show_sport()

def show_schedule():#
    goat()
    print("These are all the sport shcedule\n")
    print("ID\tName\tDay\tTime\tDuration\n")
    myfile = open ("sschedule_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        print(lis[0]+"\t"+lis[1]+"\t"+lis[2]+"\t"+lis[3]+"\t"+lis[4])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        students()
    else:
        show_schedule()

def students_login():#
    goat()
    future()
    myfile = open("student_register.txt","r")
    username = str(input("Username: "))
    password = str(input("Password: "))
    cond = "false"
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        y = lis[1]
        if(username == x and password == y):
            cond = "true"
            students_menu(username)
    myfile.close()
    while(cond == "false"):
        myfile = open("student_register.txt","r")
        print("Wrong login, please re-enter username and password")
        username = str(input("Username: "))
        password = str(input("Password: "))
        for line in myfile:
            data = line.rstrip()
            lis = data.split(",")
            x = lis[0]
            y = lis[1]
            if(username == x and password == y):
                cond = "true"
                students_menu(username)
        myfile.close()

def students_menu(username):#
    goat()
    print ("Hi future champ, what do you wanna do?\n")
    print ("1. Show my coach detail")
    print ("2. Show my profile")
    print ("3. Show my sports schedule")
    print ("4. Modify my profile")
    print ("5. Provide feedback and star to coach")
    print ("6. Log-Out")     
    menu_pick = int(input("Enter your choice: "))

    if(menu_pick == 1):
        show_mycoach(username)

    elif(menu_pick == 2):
        show_myprofile(username)

    elif(menu_pick == 3):
        show_myschedule(username)

    elif(menu_pick == 4):
        modify_myprofile(username)

    elif(menu_pick == 5):
        provide_feedback(username)

    else:
        role()

def show_mycoach(username):#
    goat()
    future()
    print("This is my coach detail\n")
    myfile = open("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(username == lis[0]):
            mysport = lis[7]
    myfile.close()

    myfile = open("coach_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(mysport == lis[8]):
            print("ID: "+lis[0])
            print("Name: "+lis[1])
            print("Join date: "+lis[2])
            print("Left date: "+lis[3])
            print("Hourly rate: "+lis[4])
            print("Phone number: "+lis[5])
            print("Address: "+lis[6])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        students_menu(username)
    else:
        show_mycoach(username)



def show_myprofile(username):#
    goat()
    future()
    print("This is my profile\n")
    myfile = open ("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(username == lis[0]):
            print("Name: "+lis[3])
            print("Address: "+lis[4])
            print("Phone number: "+lis[5])
            print("Date of birth: "+lis[6])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        students_menu(username)
    else:
        show_myprofile(username)


def show_myschedule(username):#
    goat()
    future()
    print("This is my sport schedule")
    myfile = open("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(username == lis[0]):
            mysport = lis[7]
    myfile.close()

    myfile = open("sschedule_record.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(mysport == lis[1]):
            print("Sport ID: "+lis[0])
            print("Sport name: "+lis[1])
            print("Day: "+lis[2])
            print("Time: "+lis[3])
            print("Duration: "+lis[4])
    myfile.close()

    choice=int(input("\nEnter any key to re display or 9 to exit: "))
    if(choice == 9):
        students_menu(username)
    else:
        show_myschedule(username)

def modify_myprofile(username):#
    goat()
    future()
    print("This is my profile\n")
    myfile = open ("student_register.txt","r")
    terdata = ""
    new_data = ""
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(username == lis[0]):
            def myprofile():
                print("1. Name: "+lis[3])
                print("2. Address: "+lis[4])
                print("3. Phone number: "+lis[5])
                print("4. Date of birth: "+lis[6])
            myprofile()

            ganti = int(input("\nEnter which number do you want to edit: "))
            terganti = str(input("Enter value: "))
            lis[ganti+2] = terganti
            print("\nYour data has been modified")
            myprofile()

            terdata = (lis[0]+","+lis[1]+","+lis[2]+","+lis[3]+","+lis[4]
                       +","+lis[5]+","+lis[6]+","+lis[7]+"\n")
            new_data = (new_data+terdata)
        else:
            new_data = (new_data+data+"\n")
    myfile.close()

    myfile = open("student_register.txt","w")
    myfile.write(new_data)
    myfile.close()

    choice=int(input("\nEnter any key to re modify or 9 to exit: "))
    if(choice == 9):
        students_menu(username)
    else:
        modify_myprofile(username)

def provide_feedback(username):#
    goat()
    future()
    print("Please enter your feedback and star")

    myfile = open("feedback.txt","a")
    feedback = str(input("Write your feedback:\n"))
    myfile.write(feedback+"\n")
    myfile.close()
        
    print("\nThis is my coach detail")
    myfile = open("student_register.txt","r")
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(username == lis[0]):
            mysport = lis[7]
    myfile.close()

    myfile = open("coach_record.txt","r")
    terdata = ""
    new_data = ""
    
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        if(mysport == lis[8]):
            def rating():
                print("ID: "+lis[0])
                print("Name: "+lis[1])
                print("Current star rating: "+lis[10])
            rating()
            
            print("\nIn a rate of 1-5 stars,Please rate your coach")
            star = int(input("Enter stars: "))
            while (star >5 or star <1):
                print("Rating is out of range, re-input rating")
                star = int(input("Enter stars: "))
            a = int(lis[10])
            import math
            avg = math.ceil ((a+star)/2)
            lis[10] = str(avg)
            rating()

            terdata = (lis[0]+","+lis[1]+","+lis[2]+","+lis[3]+","+lis[4]+","+lis[5]+","+lis[6]
                            +","+lis[7]+","+lis[8]+","+lis[9]+","+lis[10]+"\n")
            new_data = (new_data+terdata)
        else:
            new_data = (new_data+data+"\n")
    myfile.close()
    
    myfile = open("coach_record.txt","w")
    myfile.write(new_data)
    myfile.close()

    choice=int(input("\nEnter any key to add another feedback or 9 to exit: "))
    if(choice == 9):
        students_menu(username)
    else:
        provide_feedback(username)

def students_register():#
    goat()
    future()
    myfile = open("student_register.txt","a")
    myfile.close()

    myfile = open("student_register.txt","r")
    username = str(input("Enter a username to register: "))
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        x = lis[0]
        while(username == x):
            print("username is used, enter another username")
            username = str(input("Enter a username to register: "))
    myfile.close()
            
    myfile = open("student_register.txt","r")
    password = str(input("Enter a password to register: "))
    print("\nPlease fill your personal detail")
    student_id = str(input("Enter an ID: "))
    for line in myfile:
        data = line.rstrip()
        lis = data.split(",")
        while(student_id == lis[2]):
            print("ID is used, enter another ID")
            student_id = str(input("Enter a ID to register: "))
    student_name = str(input("Name: "))
    student_address = str(input("Address: "))
    student_phone = str(input("Phone number: "))
    student_dob = str(input("Date of birth (dd/mm/yy): "))
    print("\nwhat sports will you participate in")
    student_sname = str(input("Sport name: "))
    myfile.close()
            
    myfile = open("student_register.txt","a")
    myfile.write(username+","+password+","+student_id+","+student_name
                 +","+student_address+","+student_phone+","+student_dob
                 +","+student_sname+"\n")      
    myfile.close()

    choice=int(input("\nEnter any key to create another account or 9 to exit: "))
    if(choice == 9):
        students()
    else:
        students_register()

role()
