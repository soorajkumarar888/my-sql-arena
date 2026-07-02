import csv


master_list=[]
with open ('patients.csv') as file:
  reader=csv.reader(file,delimiter=';')
  next(reader)
  for row in reader:
    patient_id = row[0]
    first_name = row[1]
    last_name = row[2]
    gender = row[3]
    birth_date = row[4]
    city = row[5]
    province_id = row[6]  
    allergies = row[7]    
    height = row[8]       
    weight = row[9]

    first_name_clean = first_name.replace("'", "''")
    last_name_clean = last_name.replace("'", "''")
    city_clean = city.replace("'", "''")

    if allergies.strip()=="":
      allergies="NULL"
      final_row = f"({patient_id}, '{first_name_clean}', '{last_name_clean}', '{gender}', '{birth_date}', '{city_clean}', {allergies}, {height}, {weight}, '{province_id}'),"

    else:
      allergies_clean=allergies.replace("'", "''")
      final_row = f"({patient_id}, '{first_name_clean}', '{last_name_clean}', '{gender}', '{birth_date}', '{city_clean}', '{allergies_clean}', {height}, {weight}, '{province_id}'),"


    master_list.append(final_row)
if master_list:
    master_list.insert(0,"INSERT INTO patients (patient_id, first_name, last_name, gender, birth_date, city, allergies, height, weight, province_id) VALUES")
    master_list[-1] = master_list[-1].replace("),",");")    

with open('patients-dml.sql',mode='w',encoding='utf-8') as outfile:
  for lines in master_list:
    outfile.write(lines+'\n')

