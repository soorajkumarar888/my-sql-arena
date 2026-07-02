import csv

master_list=[]
with open('doctors.csv') as file:
  reader=csv.reader(file,delimiter=';')
  next(reader)
  for row in reader:
    doctor_id=row[0]
    first_name=row[1]
    last_name=row[2]
    specialty=row[3]

    first_name_clean = first_name.replace("'", "''")
    last_name_clean = last_name.replace("'", "''")
    specialty_clean = specialty.replace("'", "''")
    
    final_row=f"({doctor_id}, '{first_name_clean}', '{last_name_clean}', '{specialty_clean}'),"
    master_list.append(final_row)
if master_list:
    master_list.insert(0,"INSERT INTO doctors (doctor_id, first_name, last_name, speciality) VALUES")
    master_list[-1] = master_list[-1].replace("),",");")

with open ('doctors-dml.sql', mode='w', encoding='utf-8') as outfile:
  for lines in master_list:
    outfile.write(lines+'\n')

