def ExamSchedule(ch):

    if(ch == 'A'):
        print("Exam of division A at 7 AM")
    
    elif(ch == 'B'):
        print("Exam of division B at 8 AM")

    elif(ch == 'C'):
        print("Exam of division C at 9 AM")

    elif(ch == 'D'):
        print("Exam of division D at 10 AM")
    
    else:
        print("Invalid option")


def main():

    print("Enter the division")
    cValue = input()

    ExamSchedule(cValue)

if __name__ == "__main__":
    main()