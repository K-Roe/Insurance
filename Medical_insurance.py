from audioop import add
import csv
from tkinter import Y
import numpy as np

with open("C:\KarlsCode\Python\Data_Science\Insurance\insurance.csv") as insurance_file:
    insurance_dataset = insurance_file.read()

#Make empty list for all the data from insurance.csv    
ages = []
sex_m_f = []
bmis = []
children_num = []
smoke = []
regions = []
cost = []


# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open("C:\KarlsCode\Python\Data_Science\Insurance\insurance.csv") as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sex_m_f, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(children_num, 'insurance.csv', 'children')
load_list_data(smoke, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(cost, 'insurance.csv', 'charges')

# open insurance.csv and .append each row in to the correct lists with the ["Key"]
with open("C:\KarlsCode\Python\Data_Science\Insurance\insurance.csv", newline = "") as insurance_file:
    insurance_dict = csv.DictReader(insurance_file)
    for row in insurance_dict:
        ages.append(row["age"])
        sex_m_f.append(row["sex"])
        bmis.append(row["bmi"])
        children_num.append(row["children"])
        smoke.append(row["smoker"])
        regions.append(row["region"])
        cost.append(row["charges"])

#print each list out to test it works
"""
print("Age: " + str(ages))
print("Sex: " + str(sex_m_f))
print("BMI: " + str(bmis))
print("Number of children: " + str(children_num))
print("Smoker: " + str(smoke))
print("Region: " + str(regions))
print("Cost of insurance: " + str(cost))
"""



class PatientsInfo:  
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker, patients_regions, patients_costs):
        
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker = patients_smoker
        self.patients_regions = patients_regions
        self.patients_costs = patients_costs
   
   
   
   
    def analyze_sexes(self):
        # initialize number of males and females to zero
        females = 0
        males = 0
        # iterate through each sex in the sexes list
        for sex in self.patients_sexes:
            # if female add to female variable
            if sex == 'female':
                females += 1
            # if male add to male variable
            elif sex == 'male':
                males += 1
        # print out the number of each
        print(f"Their are: {females} females in this data ")
        print(f"Their are: {males} males in this data")      
     
    def analyze_smokers(self):
        female_smoker = 0
        male_smoker = 0
        female_none = 0
        male_none = 0
        self.smoker_analyze = list(zip(self.patients_sexes, self.patients_smoker))
        #print(self.zipped_analyze)
        for x , y in self.smoker_analyze:
            if x == "female" and y == "yes":
                female_smoker +=1
            if x =="male" and y == "yes":
                male_smoker +=1
            if x == "female" and y == "no":
                female_none +=1
            if x == "male" and y == "no":
                male_none +=1
        print("The number of females that smoke is: " + str(female_smoker)) # 230
        print("The number of males that smoke is: " + str(male_smoker)) # 318
        print("The number of females that dont smoke is: " + str(female_none)) # 1094
        print("The number of males that dont smoke is: " + str(male_none)) # 1034
        
    def analyze_cost(self):
        female_cost = []
        male_cost = []
        
        self.cost_analyze = list(zip(self.patients_sexes, self.patients_costs))
        #print(self.cost_analyze)
        for x, y in self.cost_analyze:
            if x == "female":
                female_cost.append(y)
            if x == "male":
                male_cost.append(y)
        total_female_cost = [int(float(string)) for string in female_cost]
        sum1 = sum(number for number in total_female_cost)
        print(f"The total insurance cost for females is: {sum1}")
        total_male_cost = [int(float(string)) for string in male_cost]
        sum2 = sum(number for number in total_male_cost)
        print(f"The total insurance cost for males is: {sum2}")

     

           
            
        
   
        
        
      

        #print("The female insurance cost is: " + str(female_cost))
        #print("the male insureance cost is: " + str(male_cost))
        
            
        
        
        
patient_info = PatientsInfo(ages, sex_m_f, bmis, children_num, smoke, regions, cost)

patient_info.analyze_sexes()      
patient_info.analyze_smokers()
patient_info.analyze_cost()





    



# if sex = male and smoker = yes add 1 else add 0
# if sex = femaile and smoker = year add 1 else add 0
