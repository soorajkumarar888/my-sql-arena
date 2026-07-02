import csv

master_list=[]
with open('province_names.csv') as file:
  reader=csv.reader(file, delimiter=';')
  next(reader)
  for row in reader:
    province_id=row[0]
    province_name=row[1]

    province_id_clean = province_id.replace("'", "''")
    province_name_clean = province_name.replace("'", "''")

    final_row = f"('{province_id_clean}', '{province_name_clean}'),"
    master_list.append(final_row)
if master_list:
    master_list.insert(0,"INSERT INTO province_names (province_id, province_name) VALUES")
    master_list[-1] = master_list[-1].replace("),",");")

  
with open('province_names-dml.sql', mode='w',encoding='utf-8') as outfile:
  for lines in master_list:
    outfile.write(lines+'\n')
    
