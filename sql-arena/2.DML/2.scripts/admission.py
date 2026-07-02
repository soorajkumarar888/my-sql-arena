import csv

master_list=[]
with open ('admissions.csv') as file:
  reader=csv.reader(file, delimiter=';')
  next(reader)
  for row in reader:
    patient_id = row[0]
    admission_date = row[1]
    discharge_date = row[2]
    diagnosis = row[3]
    attending_doctor_id = row[4]
    diagnosis_cleaned = diagnosis.replace("'", "''")
    final_row = f"({patient_id}, '{admission_date}', '{discharge_date}', '{diagnosis_cleaned}', {attending_doctor_id}),"
    master_list.append(final_row)
if master_list:
    master_list.insert(0,"INSERT INTO admissions (patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id) VALUES")
    master_list[-1] = master_list[-1].replace("),",");")    

with open('admissions-dml.sql', mode='w', encoding='utf-8') as outfile:
  for lines in master_list:
    outfile.write(lines+'\n')
    




