# we are trying to create a system for booking tickets.
print("*********************TICKET BOOKING SYSTEM ****************************")
restart = ("Y")

while restart !=("NO"):
    print("1 Check PNR status")
    print("2 ticket Reservation")
    option = int(input("enter your option :"))
    
    if option==1:
        print("Your PNR status is t3")
        exit(0)
    elif option ==2:
        people =int(input("enter the number of tickets you want:"))
        name=[]
        age=[]
        sex=[]
        number=[]
        for p in range (people):
            name =str(input("Name:"))
            age=str(input("Age:"))
            sex=str(input("male or female:"))
            # number=int(input("Number:"))
            
        restart=str(input("dID YOU FORGET ANYONE?y/n:"))
        if restart in ("y","YES"):
            restart=("Y")
        else:
            x=0
            print("Total Ticket:",people)
            for p in range(1,people+1):
                print("Ticket:",p)
                print("Name:",name[x])
                print("Age :",age[x])
                print("sex:",sex[x])
                # print("Number:",number[x])
                print("Thanks for supporting our system .")
                # exit(0)
                
               