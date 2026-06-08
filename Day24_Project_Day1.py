"""
Hospital Management System
Entity
- Patient
- Doctor
- Appointment

1- Add Patient Information
2- View All Patients
3- Update Patient Information
4- Delete A Patient
5- Add Doctor Information
6- View All Doctors Information
7- Active/Inactive Doctor
8- Book An Appointment
9- View All Appointments
0- Exit


"""
# IMPORTING REQUIRED LIBRARIES
import pickle

# A METHOD TO ADD PATIENT INFORMATION
def addPatient():
    pid = input("\n\tEnter Patient ID : ")
    pname = input("\tEnter Patient Name : ")
    page = input("\tEnter Patient Age : ")
    pgender = input("\tEnter Patient Gender : ")
    pmob = input("\tEnter Patient Mobile No : ")
    pdisease = input("\tExplain Disease/Problem : ")
    data = {pid:[pname,page,pgender,pmob,pdisease]}
    file = open('patient.bin','ab')
    pickle.dump(data,file)
    file.close()
    print("\n\t\tPatient Added Successfully!")

# DASHBOARD
while True:
    print("\n\t\tHospital Management System")
    print('''
        1- Add Patient Information
        2- View All Patients
        3- Update Patient Information
        4- Delete A Patient
        5- Add Doctor Information
        6- View All Doctors Information
        7- Active/Inactive Doctor
        8- Book An Appointment
        9- View All Appointments
        0- Exit''')
    ch = int(input("\n\tEnter Your Choice : "))
    if ch==0:
        print("\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addPatient()
        input("\n\t\tPress Enter To Continue...")

