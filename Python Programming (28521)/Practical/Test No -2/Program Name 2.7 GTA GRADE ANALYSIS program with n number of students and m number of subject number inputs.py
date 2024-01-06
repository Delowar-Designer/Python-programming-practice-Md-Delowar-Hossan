# GTA GRADE ANALYSIS program with n number of students and m number of subject number inputs
def calpoint(mark):
    if mark>=80:
        return 5
    elif mark>=70:
        return 4
    elif mark>=60:
        return 3.5
    elif mark>=50:
        return 3
    elif mark>=40:
        return 2
    elif mark>=33:
        return 1
    else:
        return 0

std = int(input("How Many Student = "))
for i in range(0,std):
    nosub = int(input("\n\t Number of Subject = "))
    obtain = []
    for i in range(0,nosub):
        ob = int(input("Enter obtain Marks = "))
        obtain.append(ob)
    poin = []
    for i in obtain:
        poin.append(calpoint(i))
    p = 1
    for i in poin:
        p = p * i
    if(p!=0):
        print("GPA:",sum(poin)/len(poin))
    else:
        print("\n GPA ",p)
    print("......................................")
