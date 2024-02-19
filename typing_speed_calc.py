from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range (len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error +=1
        except:
            error +=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input(" ready to test : Yes/No :")
        if ck == "Yes":
            test=["The time module comes with Python’s standard utility module, so there is no need to install it externally. We can simply import it using the import statement.",
                "The time module in Python provides functions for handling time-related tasks.",
                "In Python, the time() function returns the number of seconds passed since epoch (the point where time begins)."]
            test1 = r.choice(test)
            print("      ****** typing speed ******")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput=input("Enter : ")
            time_2 = time()

            print("Speed : ",  speed_time(time_1,time_2,testinput)," w/sec")
                
            print("Error : ", mistake(test1,testinput))

        elif ck=="No":
            print("Thank You")
            break

        else:
            print(" wrong input")
