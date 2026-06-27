### 1. Show first name, last name, and gender of patients whose gender is 'M'.
* **Concepts Covered:** Column Selection (`SELECT`), Row Filtering (`WHERE`).

```sql
SELECT 
    first_name, 
    last_name, 
    gender
FROM patients 
WHERE gender = 'M';


