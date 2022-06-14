import numpy as np

class P1(Exception):
    pass

class Student:
    def __init__(self):
        self.name=""
        self.lastname=""
        self.telephone=""
        self.grades=[]
    
    def CreateStudent(self):
        self.name=input("State your name: ")
        self.lastname=input("State your lastname: ")
        self.telephone=input("Give your Phone: ")
        
        for i in range(5):
            while(True):    
                try:
                    g=float(input("Give your grade of subject %d: " %(i+1)))
                    if (g<0 or g>100):
                        raise P1
                    else:
                        self.grades.append(g)
                        break
                except P1:
                    print("Grade must be between 0 -100")
                except:
                    print("Grade must be a number")
        
        print("\n")
    
    
    def Show(self):
        print("Student's stats:\n")
        print("Name: %s \t LastName: %s \t Telephone: %s" %(self.name,self.lastname,self.telephone))
        print("Grades: ", self.grades)
        print("Mean Grade: %f \t Max Grade: %f \t Min Grade: %f" %(self.Mean(),self.Max(),self.Min()))
        print("\n\n")
    
    def Mean(self):
        return np.mean(self.grades)
    
    def MeanStudents(self):
        print("Name: %s \t LastName: %s \t Mean Grade: %f" %(self.name,self.lastname,self.Mean()))
   
    def Max(self):
        return max(self.grades)
    
    def Min(self):
        return min(self.grades)
            
def menu():
    L=[]
    while(True):
        print ("1.Create Student")
        print ("2.Find and Show Student")
        print ("3.Mean Grade of all Students")
        print ("4.List of Mean Students' Grades")
        print ("0.Exit")
        print ("------------------------------")
        
        try:
            c=int(input("Choice: "))
            if (c<0 or c>4):
                print("Choice must be between 0 - 4\n")
            
            if (c==0):
                break
            
            if(c==1):
                S=Student()
                S.CreateStudent()
                L.append(S)
                           
            if(c==2):
                
                a=input("Give the lastname of a student: ")
                L2=[p.lastname for p in L]
                try:
                    i=L2.index(a)
                    L[i].Show()
                except:
                    print("Student couldn't found")
                    print("\n")
                    
            if(c==3):
                L3=[p.Mean() for p in L]
                print("Mean Grade of all Students: ", np.mean(L3))
                print("\n\n")
            
            if(c==4):
                for p in L:
                    p.MeanStudents()
                print("\n\n")
                
        except:
            print("Error, please try again")
                
menu()
