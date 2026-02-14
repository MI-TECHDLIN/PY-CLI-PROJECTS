import re
def grade(n=0):
    # re.search('A'):
    # re.sub(f'{'B'}',4,n)
    # re.sub(f'{'C'}',3,n)
    # re.sub(f'{'D'}',2,n)
    # re.sub(f'{'E'}',1,n)
    if n  == 'A':
        return 5
    elif n == 'B':
        return 4
    elif  n == 'C':
       return 3
    elif n == 'D':
        return 2
    elif n == 'E':
        return 1
    else:
        return 0

def main():
    grade()
mtsgrade= grade(input("what is your MTS grade "))
mtsunit=int(input('what your course unit?  '))

cscgrade= grade(input("what is your CSC grade "))
cscunit=int(input('what your course unit?  '))

meegrade= grade(input("what is your MEE grade "))
meeunit=int(input('what your course unit?  '))

gnsgrade= grade(input("what is your GNS grade "))
gnsunit=int(input('what your course unit?  '))

gstgrade= grade(input("what is your GST grade "))
gstunit=int(input('what your course unit?  '))

fsengrade= grade(input("what is your FSEN grade "))
fsenunit=int(input('what your course unit?  '))

phy101grade= grade(input("what is your PHY107 grade "))
phy101unit=int(input('what your course unit?  '))

phy107grade= grade(input("what is your phy107 grade "))
phy107unit=int(input('what your course unit?  '))

statgrade= grade(input("what is your STA grade "))
statunit=int(input('what your course unit?  '))


courses = {
    "MTS": (mtsgrade, mtsunit),
    "CSC": (cscgrade, cscunit),
    "MEE": (meegrade, meeunit),
    "GNS": (gnsgrade, gnsunit),
    "GST": (gstgrade, gstunit),
    "FSEN": (fsengrade, fsenunit),
    "PHY101": (phy101grade, phy101unit),
    "PHY107": (phy107grade, phy107unit),
    "STA": (statgrade, statunit),
}

total_points = 0
total_units = 0

for gp, unit in courses.values():
    total_points += gp * unit
    total_units+= unit
gpa=total_points/total_units
print("GPA:=",gpa)

if __name__ == '__main__':
    main()

