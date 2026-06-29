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
### 14. Based on the cities that our patients live in, show unique cities that are in province_id 'NS'.
* **Concepts Covered:** Duplicate Removal (`DISTINCT`), Row Filtering (`WHERE`).

```sql
SELECT DISTINCT city 
FROM patients 
WHERE province_id = 'NS';
```
### 15. Write a query to find the first_name, last name and birth date of patients who have height more than 160 and weight more than 70.
* **Concepts Covered:** Row Filtering (`WHERE`), Logical Conjunction (`AND`), Comparison Operators (`>`).

```sql
SELECT first_name, last_name, birth_date 
FROM patients 
WHERE height > 160 AND weight > 70;
```
### 16. Show unique birth years from patients and order them by ascending.
* **Concepts Covered:** Date Extraction (`YEAR`), Duplicate Removal (`DISTINCT`), Sorting Data (`ORDER BY ... ASC`).

```sql
SELECT DISTINCT YEAR(birth_date) AS years 
FROM patients 
ORDER BY years ASC;
```
### 17. Show unique first names from the patients table which only occurs once in the list.
* **Concepts Covered:** Grouping Data (`GROUP BY`), Group Filtering (`HAVING`), Aggregate Counting (`COUNT`).

```sql
SELECT first_name 
FROM patients 
GROUP BY first_name 
HAVING COUNT(*) = 1;
```
### 18. Show patient_id and first_name from patients where their first_name starts and ends with 's' and is at least 6 characters long.
* **Concepts Covered:** String Functions (`LEFT`, `RIGHT`, `LENGTH`), Comparison Operators (`>=`), Row Filtering (`WHERE`).

```sql
SELECT patient_id, first_name 
FROM patients 
WHERE LEFT(first_name, 1) = 's' 
  AND RIGHT(first_name, 1) = 's' 
  AND LENGTH(first_name) >= 6;
```
### 19. Show patient_id, first_name, last_name from patients whose diagnosis is 'Cardiac Arrest'.
* **Concepts Covered:** Table Joins (`JOIN`), Join Conditions (`ON`), Row Filtering (`WHERE`).

```sql
SELECT 
    p.patient_id, 
    p.first_name, 
    p.last_name 
FROM patients p 
JOIN admissions a 
    ON p.patient_id = a.patient_id 
WHERE a.diagnosis = 'Cardiac Arrest';
```
### 20. Display every patient's first_name. Order the list by the length of each name and then by alphabetically.
* **Concepts Covered:** Sorting Data (`ORDER BY`), Multi-Column Sorting, String Length (`LENGTH`).

```sql
SELECT first_name 
FROM patients 
ORDER BY LENGTH(first_name), first_name;
```
### 21. Show the total number of male patients and the total number of female patients in the patients table. Display the two results in the same row.
* **Concepts Covered:** Conditional Aggregation (`SUM` with `CASE WHEN`), Column Aliasing (`AS`).

```sql
SELECT 
    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male,
    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female
FROM patients;
```
### 22. Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.
* **Concepts Covered:** Multi-Column Grouping (`GROUP BY`), Group Filtering (`HAVING`), Aggregate Counting (`COUNT`).

```sql
SELECT 
    patient_id, 
    diagnosis 
FROM admissions 
GROUP BY 
    patient_id, 
    diagnosis 
HAVING COUNT(*) > 1;
```
### 23. Show the city and the total number of patients in the city. Order from most to least patients and then by city name ascending.
* **Concepts Covered:** Grouping (`GROUP BY`), Column Aliasing (`AS`), Multi-Column Sorting using Alias Names.

```sql
SELECT 
    city, 
    COUNT(patient_id) AS total_patients 
FROM patients 
GROUP BY city 
ORDER BY 
    total_patients DESC, 
    city ASC;
```
### 24. Show first name, last name and role of every person that is either patient or doctor. The roles are either "Patient" or "Doctor"
* **Concepts Covered:** Combining Datasets (`UNION ALL`), Hardcoded String Literals, Column Aliasing.

```sql
SELECT 
    first_name, 
    last_name, 
    'Patient' AS role 
FROM patients  
UNION ALL
SELECT 
    first_name, 
    last_name, 
    'Doctor' AS role 
FROM doctors;
```
### 25. Show all allergies ordered by popularity. Remove NULL values from the query.
* **Concepts Covered:** Filtering Missing Data (`IS NOT NULL`), Grouping (`GROUP BY`), Sorting by Aggregate Calculations (`ORDER BY COUNT(*)`).

```sql
SELECT allergies 
FROM patients 
WHERE allergies IS NOT NULL 
GROUP BY allergies 
ORDER BY COUNT(*) DESC;
```
### 26. Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date
* **Concepts Covered:** Date Extraction (`YEAR()`), Range Filtering (`BETWEEN`), Chronological Sorting (`ORDER BY`).

```sql
SELECT 
    first_name, 
    last_name, 
    birth_date 
FROM patients 
WHERE YEAR(birth_date) BETWEEN 1970 AND 1979
ORDER BY birth_date;
```
### 27. Display each patient's full name in a single column (LAST_NAME,first_name) with specific casing rules, sorted by first_name descending.
* **Concepts Covered:** String Concatenation (`CONCAT_WS`), Casing Transformations (`UPPER`/`LOWER`), Sorting Data (`ORDER BY DESC`).

```sql
SELECT 
    CONCAT_WS(',', UPPER(last_name), LOWER(first_name)) AS full_name 
FROM patients 
ORDER BY first_name DESC;
```
### 28. Show the province_id(s), sum of height; where the total sum of its patient's height is greater than or equal to 5000.
* **Concepts Covered:** Aggregation (`SUM`), Grouping (`GROUP BY`), Group-Level Filtering (`HAVING`).

```sql
SELECT 
    province_id, 
    SUM(height) AS total_height 
FROM patients 
GROUP BY province_id 
HAVING SUM(height) >= 5000;
```

