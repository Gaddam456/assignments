class School:
    def __init__(self, name, class_standard, rollNo, location, fav_sub):
        self.name = name
        self.class_standard = class_standard
        self.rollNo = rollNo
        self.location = location
        self.fav_sub = fav_sub

    def student_details(self):
        return f"My name is {self.name}. I am studying in {self.class_standard} standard. My roll number is {self.rollNo}. I stay in {self.location}. My favourite subject is {self.fav_sub}."    

abhinav = School("Abhinav", "5th", "11", "Madhura", "Social")
print(abhinav.student_details())
print("-----------------------")
aditya = School("Aditya", "6th", "2", "Karimnagar", "Science")
print(aditya.student_details())
print("-----------------------")
manohar = School("Manohar", "5th", "11", "Madhura", "Hindi")
print(manohar.student_details())
print("-----------------------")
nikhil = School("Nikhil", "4th", "16", "Warangal", "Science")
print(nikhil.student_details())
print("-----------------------")
ranjith = School("Ranjith", "4th", "23", "Dharmapuri", "Social")
print(ranjith.student_details())
print("-----------------------")
arjun = School("Arjun", "5th", "6", "Mancherial", "Maths")
print(arjun.student_details())
print("-----------------------")
santosh = School("Santhosh", "8th", "15", "Hyderabad", "Biology")
print(santosh.student_details())
print("-----------------------")
shilpa = School("Shilpa", "6th", "29", "Hyderabad", "Social")
print(shilpa.student_details())
print("-----------------------")
ramu = School("Ramu", "9th", "17", "Secunderabad", "Maths")
print(ramu.student_details())
print("-----------------------")
krishna = School("Krishna", "10th", "2", "Karimnagar", "Science")
print(krishna.student_details())
print("-----------------------")
