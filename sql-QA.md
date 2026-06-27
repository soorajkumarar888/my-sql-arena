### 1. Show first name, last name, and gender of patients whose gender is 'M'.
* **Concepts Covered:** Column Selection (`SELECT`), Row Filtering (`WHERE`).

```sql
SELECT 
    first_name, 
    last_name, 
    gender
FROM patients 
WHERE gender = 'M';
```
### 2. Show first name and last name of patients who do not have allergies.
* **Concepts Covered:** Missing Data Handling (`IS NULL`).

```sql
SELECT 
    first_name, 
    last_name 
FROM patients 
WHERE allergies IS NULL;
```
### 3. Show first name of patients that start with the letter 'C'.
* **Concepts Covered:** Pattern Matching (`LIKE`), Wildcard Filtering (`%`), String Functions (`LEFT`, `SUBSTRING`).

```sql
-- Method 1: Standard Wildcard (Recommended)
SELECT first_name 
FROM patients 
WHERE first_name LIKE 'C%';

-- Method 2: Using LEFT function
SELECT first_name 
FROM patients 
WHERE LEFT(first_name, 1) = 'C';

-- Method 3: Using SUBSTRING function
SELECT first_name 
FROM patients 
WHERE SUBSTRING(first_name, 1, 1) = 'C';
```
### 4. Show first name and last name of patients that weight within the range of 100 to 120 (inclusive).
* **Concepts Covered:** Range Filtering (`BETWEEN`), Comparison Operators (`>=`, `<=`), Logical Operators (`AND`).

```sql
-- Method 1: Using BETWEEN (Cleanest)
SELECT first_name, last_name 
FROM patients 
WHERE weight BETWEEN 100 AND 120;

-- Method 2: Using Comparison Operators
SELECT first_name, last_name 
FROM patients 
WHERE weight >= 100 AND weight <= 120;
```
### 5. Update the patients table for the allergies column. If the patient's allergies is null then replace it with 'NKA'.
* **Concepts Covered:** Data Modification (`UPDATE`), Null Handling (`IS NULL`, `COALESCE`), Query Performance Optimization.

```sql
-- Method 1: Using WHERE Clause (Best Practice & Safe for Production)
UPDATE patients 
SET allergies = 'NKA' 
WHERE allergies IS NULL;

-- Method 2: Using COALESCE (Alternative, but warns: rewrites the whole table!)
UPDATE patients 
SET allergies = COALESCE(allergies, 'NKA');
```
### 6. Show first name and last name concatenated into one column to show their full name.
* **Concepts Covered:** String Manipulation (`CONCAT`, `CONCAT_WS`), Column Aliasing (`AS`).

```sql
-- Method 1: Using CONCAT_WS (Best Practice - Handles NULLs gracefully)
SELECT CONCAT_WS(' ', first_name, last_name) AS full_name
FROM patients;

-- Method 2: Using Standard CONCAT
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM patients;

-- Method 3: Using Standard SQL Pipe Operator (Alternative)
SELECT first_name || ' ' || last_name AS full_name
FROM patients;
```
### 7. Show first name, last name, and the full province name of each patient.
* **Concepts Covered:** Table Joins (`JOIN`), Table Aliasing.

```sql
SELECT 
    p.first_name, 
    p.last_name, 
    pr.province_name 
FROM patients p 
JOIN province_names pr 
    ON p.province_id = pr.province_id;
```
### 8. Show how many patients have a birth_date with 2010 as the birth year.
* **Concepts Covered:** Aggregate Functions (`COUNT`), Date Functions (`YEAR`), Row Filtering (`WHERE`).

```sql
SELECT COUNT(patient_id) AS total_patients 
FROM patients 
WHERE YEAR(birth_date) = 2010;
```
### 9. Show the first_name, last_name, and height of the patient with the greatest height.
* **Concepts Covered:** Sorting Data (`ORDER BY`), Limiting Results (`LIMIT`).

```sql
SELECT first_name, last_name, height 
FROM patients 
ORDER BY height DESC 
LIMIT 1;
```
### 10. Show all columns for patients who have one of the following patient_ids: 1, 45, 134, 90, 3.
* **Concepts Covered:** List Filtering (`IN`), Wildcard Selection (`*`).

```sql
SELECT * FROM patients 
WHERE patient_id IN (1, 45, 134, 90, 3);
```
### 11. Show the total number of admissions.
* **Concepts Covered:** Aggregate Functions (`COUNT`).

```sql
SELECT COUNT(admission_date) AS total_admissions 
FROM admissions;
```
### 12. Show all the columns from admissions where the patient was admitted and discharged on the same day.
* **Concepts Covered:** Column-to-Column Comparison, Row Filtering (`WHERE`).

```sql
SELECT * FROM admissions 
WHERE admission_date = discharge_date;
```
### 13. Show the total number of admissions for patient_id 9.
* **Concepts Covered:** Aggregate Functions (`COUNT`), Row Filtering (`WHERE`).

```sql
SELECT COUNT(*) AS total_admissions 
FROM admissions 
WHERE patient_id = 9;
```
