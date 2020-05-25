"""A simple app to hold information related to contact information, dates, and reminders to make
follow-up phone calls and/or e-mails."""

def create_new_job():
    job_1 = {}
    job_1["Company"] = input("Enter the name of the company: ")
    job_1["Phone number"] = input("Enter the company's phone number: ")
    job_1["Position"] = input("Enter the job position: ")
    job_1["Application Date"] = input("Enter the date you applied: ")
    job_1["Interview"] = input("Do you have an interview? ")
    job_1["Interview Date"] = input("Enter the date and time of your interview: ")
    job_1["Offer"] = input("Did you receive an offer? ")
    return (job_1)

def enter_new(jobs):        #adds new job dictionary to list
    new_job = create_new_job()
    jobs.append(new_job)
    add_another(jobs)

def add_another(jobs):
    another = input("Would you like to add another job? Enter 'yes' or 'no'. ")
    if another == "yes":
        enter_new(jobs)



def look_up(jobs):
    print(" ")
    for elem in jobs:
        for key in elem:
            print(str(key) + ", " + str(elem[key]))
        print(" ")

def main():
    jobs = []       #creates an empty list
    while True:     #program will continue until directly told by user to stop
        print("What would you like to do?")
        what_do = input("Type '1' to enter new job information \n Type '2' to look up job information: ")
        if what_do == '1':
            enter_new(jobs)
        if what_do == '2':
            look_up(jobs)
        done = input("If you are done, type 'done'. If you want to continue, press any key. \n")
        if done == "done":
            print("Thank you and good luck job-hunting!")
            break


if __name__== "__main__":
    main()