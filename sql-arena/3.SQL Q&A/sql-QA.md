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
### 29. Show the difference between the largest weight and smallest weight for patients with the last name 'Maroni'
* **Concepts Covered:** Aggregate Math (`MAX` / `MIN`), Inline Subtraction, Specific Row Filtering (`WHERE`).

```sql
SELECT 
    MAX(weight) - MIN(weight) AS diff_weight 
FROM patients 
WHERE last_name = 'Maroni';
```
### 30. Show all of the days of the month (1-31) and how many admission_dates occurred on that day. Sort by the day with most admissions to least admissions.
* **Concepts Covered:** Date Part Extraction (`DAY()`), Row Aggregation (`COUNT(*)`), Evaluation-Level Grouping (`GROUP BY function`), Sorting by Aggregate Calculations (`ORDER BY DESC`).

```sql
SELECT 
    DAY(admission_date) AS day, 
    COUNT(*) AS total_no_of_admissions 
FROM admissions 
GROUP BY DAY(admission_date)
ORDER BY total_no_of_admissions DESC;
```
### 31. Show all of the patients grouped into weight groups. Show the total number of patients in each weight group. Order the list by the weight group descending. e.g. if they weigh 100 to 109 they are placed in the 100 weight group, 110-119 = 110 weight group, etc.
* **Concepts Covered:** Conditional Bucketing (`CASE WHEN`), Row Counting (`COUNT(*)`), MySQL Alias Grouping, Descending Sorting (`ORDER BY DESC`).
 --works on latest version because here GROUP BY will get internally executed before CASE WHEN 

```sql
--Method 1
 --works on latest version because here GROUP BY will get internally executed before CASE WHEN 
SELECT
    CASE
        WHEN weight BETWEEN 50 AND 59 THEN '50 weight group'
        WHEN weight BETWEEN 60 AND 69 THEN '60 weight group'
        WHEN weight BETWEEN 70 AND 79 THEN '70 weight group'
        WHEN weight BETWEEN 80 AND 89 THEN '80 weight group'
        WHEN weight BETWEEN 90 AND 99 THEN '90 weight group'
        WHEN weight BETWEEN 100 AND 109 THEN '100 weight group'
        WHEN weight BETWEEN 110 AND 119 THEN '110 weight group'
        WHEN weight >= 120 THEN '120 weight group'
    END AS weight_groups,
    COUNT(*) AS total_patients
FROM patients
GROUP BY weight_groups
ORDER BY weight_groups DESC;
```
```sql
--Method 2
--To tackle execution workflow use this
SELECT 
    CASE
        WHEN weight BETWEEN 50 AND 59 THEN '50 weight group'
        WHEN weight BETWEEN 60 AND 69 THEN '60 weight group'
        WHEN weight BETWEEN 70 AND 79 THEN '70 weight group'
        WHEN weight BETWEEN 80 AND 89 THEN '80 weight group'
        WHEN weight BETWEEN 90 AND 99 THEN '90 weight group'
        WHEN weight BETWEEN 100 AND 109 THEN '100 weight group'
        WHEN weight BETWEEN 110 AND 119 THEN '110 weight group'
        ELSE '120 weight group'
    END AS weight_groups,
    COUNT(*) AS total_patients
FROM patients
GROUP BY 
    CASE
        WHEN weight BETWEEN 50 AND 59 THEN '50 weight group'
        WHEN weight BETWEEN 60 AND 69 THEN '60 weight group'
        WHEN weight BETWEEN 70 AND 79 THEN '70 weight group'
        WHEN weight BETWEEN 80 AND 89 THEN '80 weight group'
        WHEN weight BETWEEN 90 AND 99 THEN '90 weight group'
        WHEN weight BETWEEN 100 AND 109 THEN '100 weight group'
        WHEN weight BETWEEN 110 AND 119 THEN '110 weight group'
        ELSE '120 weight group'
    END
ORDER BY weight_groups DESC; 
```
```sql
--Method 3
-- perfect one
SELECT 
    (weight / 10) * 10 AS weight_group,
    COUNT(*) AS total_patients
FROM patients
GROUP BY weight_group
ORDER BY weight_group DESC;
```
### 32. Show patient_id, weight, height, isObese from the patients table. Display isObese as a boolean 0 or 1.
* **Concepts Covered:** Unit Conversion, Arithmetic Order of Operations, Conditional Flagging (`CASE WHEN`).

```sql
SELECT 
    patient_id, 
    weight, 
    height,
    CASE 
        WHEN weight / ((height / 100.0) * (height / 100.0)) >= 30 THEN 1 
        ELSE 0 
    END AS isObese
FROM patients;
```
### 33. Show patient_id, first_name, last_name, and attending doctor's specialty. Show only the patients who has a diagnosis as 'Cardiac Arrest' and the doctor's first name is 'john'.
* **Concepts Covered:** Three-Table Joins (`JOIN`), Explicit Column Aliasing, Multi-Condition Filtering (`WHERE AND`).

```sql
SELECT 
    p.patient_id, 
    p.first_name, 
    p.last_name, 
    d.speciality 
FROM patients p 
JOIN admissions a ON p.patient_id = a.patient_id 
JOIN doctors d ON a.attending_doctor_id = d.doctor_id
WHERE a.diagnosis = 'Cardiac Arrest' 
  AND d.first_name = 'john';
```
### 34. Show the patient_id and temp_password for patients who have gone through admissions.
* **Concepts Covered:** String Manipulation (`CONCAT`, `LENGTH`), Date Extraction (`YEAR`), Aggregation Grouping (`GROUP BY`).

```sql
SELECT 
    p.patient_id, 
    CONCAT(p.patient_id, LENGTH(p.last_name), YEAR(p.birth_date)) AS temp_password
FROM patients p
JOIN admissions a ON p.patient_id = a.patient_id
GROUP BY p.patient_id;
```
### 35. Show first name, last name, and city of patients who live in either 'Hamilton' or 'Toronto' and have a weight over 80kg.
* **Concepts Covered:** Logical Filtering (`AND`, `OR`), Membership Filtering (`IN`), Conditional Parentheses Precedence.

#### Method 1: Explicit Logical OR (Standard)
```sql
SELECT 
    first_name, 
    last_name, 
    city 
FROM patients 
WHERE (city = 'Hamilton' OR city = 'Toronto') 
  AND weight > 80;
```
#### Method 2: Using IN
```sql
SELECT 
    first_name, 
    last_name, 
    city 
FROM patients 
WHERE city IN ('Hamilton', 'Toronto') 
  AND weight > 80;
```
### 36. Find all unique diagnoses in the admissions table that do not contain the word 'Cancer' or 'Flu'.
* **Concepts Covered:** Value Deduplication (`DISTINCT`), Wildcard Substring Pattern Matching (`NOT LIKE`), Compound Boolean Negation (`AND` vs `OR` traps).
When excluding multiple patterns, conditions must be chained using an `AND` operator. Using an `OR` operator accidentally causes every row to pass the filter, as a single diagnosis text string can never contain both words simultaneously.
```sql
SELECT DISTINCT diagnosis 
FROM admissions 
WHERE diagnosis NOT LIKE '%Cancer%' 
  AND diagnosis NOT LIKE '%Flu%';
```
### 37. Show the patient_id and diagnosis of all admissions that happened on a weekend (Saturday or Sunday).
* **Concepts Covered:** Date and Time Functions (`DAYNAME`), Set Membership Filtering (`IN`), Compound Boolean Evaluation (`OR`).

#### Method 1: Shorthand Set Membership (Optimized & Highly Scannable)
Using the `DAYNAME()` function combined with the `IN` operator allows for a clean, readable check against a collection of string targets.
```sql
SELECT 
    patient_id, 
    diagnosis 
FROM admissions 
WHERE DAYNAME(admission_date) IN ('Saturday', 'Sunday');
```
#### Method 2: Explicit Logical OR (Standard Breakdown)
```sql
SELECT 
    patient_id, 
    diagnosis 
FROM admissions 
WHERE DAYNAME(admission_date) = 'Saturday' 
   OR DAYNAME(admission_date) = 'Sunday';
```
### 38. Find all doctors whose specialties contain the word 'cardio' or 'neuro', but their first name does not start with 'J'.
* **Concepts Covered:** Substring Search (`LIKE`), Negated Wildcards (`NOT LIKE`), String Extraction (`LEFT`), Boolean Precedence Parentheses.

#### Method 1: Wildcard Substring Filtering (Standard & Recommended)
Using `%` wildcards isolates the roots 'cardio' and 'neuro' anywhere inside the specialty field. Parentheses group the `OR` conditions so that the first name negation `NOT LIKE 'J%'` applies strictly to both specialties.
```sql
SELECT 
    first_name, 
    last_name, 
    specialty
FROM doctors
WHERE (specialty LIKE '%cardio%' OR specialty LIKE '%neuro%')
  AND first_name NOT LIKE 'J%';
```
#### Method 2: Positional String Functions (Alternative Strategy)
This method uses the LEFT() function to pull the very first character from the left side of the name string and explicitly verifies that it does not equal the character 'J'.
```sql
SELECT 
    first_name, 
    last_name, 
    specialty
FROM doctors
WHERE (specialty LIKE '%cardio%' OR specialty LIKE '%neuro%')
  AND LEFT(first_name, 1) != 'J';
```
### 39. Show first name and last name of patients whose last name has 'o' as the second character and 'e' as the last character.
* **Concepts Covered:** Positional Wildcard Matching (`LIKE`), Character Extraction (`SUBSTRING`), Suffix Verification (`RIGHT` / Negative Offsets).

#### Method 1: Optimized Wildcard Blueprint (Highly Recommended)
Using the underscore (`_`) wildcard targets the exact second position, while the percent (`%`) wildcard handles variable middle lengths, forcing an explicit 'e' termination. This method keeps the query index-friendly.
```sql
SELECT 
    first_name, 
    last_name 
FROM patients 
WHERE last_name LIKE '_o%e';
```
#### Method 2: Precise Positional Substring Extractions
This approach uses a forward SUBSTRING anchor to isolate the second character, paired with a negative index position (`-1`) to count dynamically backward from the end of the text block.
```sql
SELECT 
    first_name, 
    last_name 
FROM patients 
WHERE SUBSTRING(last_name, 2, 1) = 'o' 
  AND SUBSTRING(last_name, -1, 1) = 'e';
```
### 40. Display all patient details for those who do not have any registered allergies and were born after December 31, 1999.
* **Concepts Covered:** Missing Data Handling (`IS NULL` vs Empty String `''`), Date Component Comparison (`YEAR`), SARGable Literal Date Filtering.

#### Method 1: Component Extraction & Dual Null Handling
This approach explicitly catches records where allergies are truly unassigned (`NULL`) or stored as a blank text block (`''`), combining it with a clean extraction of the calendar year.
```sql
SELECT * 
FROM patients 
WHERE (allergies IS NULL OR allergies = '') 
  AND YEAR(birth_date) > 1999;
```
### 41. Show all unique cities where patients live, excluding any cities that start with vowels (A, E, I, O, U).
* **Concepts Covered:** String Extraction (`LEFT`/`SUBSTRING`), Set Exclusion (`NOT IN`), Logical Conjunction (`AND` vs `OR` traps), Regular Expressions (`REGEXP`).

#### Method 1: Left-Boundary Set Exclusion (Clean & Practical)
Extracts the first character from the left side of the text string and validates that it does not belong to the set of uppercase vowels.
```sql
SELECT DISTINCT city 
FROM patients 
WHERE LEFT(city, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```
#### Method 2: SARGable Multiline Substring Filtering
Achieves identical results to Method 1 by utilizando explicit positional scanning parameters.
```sql
SELECT DISTINCT city 
FROM patients 
WHERE SUBSTRING(city, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```
#### Method 3: Regular Expression Anchor Matching (Highly Optimized)
Uses regular expression syntax to evaluate the starting boundary character. The outer ^ anchors the search to the start of the string, while [`^AEIOU`] ensures the first character is completely barred from matching any vowel.
```sql
SELECT DISTINCT city 
FROM patients 
WHERE city REGEXP '^[^AEIOU]';
```
### 42. Find all patients whose patient_id is an even number and whose height is greater than 175cm.
* **Concepts Covered:** Arithmetic Operators (`%`), Modulo Evaluation (`MOD`), Compound Boolean Filtering (`AND`).

#### Method 1: Modulo Remainder Operator (Shorthand Syntax)
Evaluates whether the `patient_id` is an even value by confirming that dividing the record ID by 2 yields a remainder of exactly 0.
```sql
SELECT * 
FROM patients 
WHERE patient_id % 2 = 0 
  AND height > 175;
```
#### Method 2: Explicit MOD Function (Standard ANSI-SQL Syntax)
```sql
SELECT * 
FROM patients 
WHERE MOD(patient_id, 2) = 0 
  AND height > 175;
```
### 43. Show all details of admissions where the patient stayed in the hospital for exactly 7 days or more.
* **Concepts Covered:** Date Arithmetic (`DATEDIFF`), Interval Computations, Relational Comparison Filters.

#### Method 1: Date Difference Evaluation (MySQL / Standard)
Using the built-in `DATEDIFF()` function safely computes the absolute number of calendar days between boundaries, ignoring mathematical month-crossing anomalies. In MySQL, the syntax subtracts the second date argument from the first.
```sql
SELECT * 
FROM admissions 
WHERE DATEDIFF(discharge_date, admission_date) >= 7;
```
### 44. Find patients whose first names are exactly 5 characters long and end with the letter 'a'.
* **Concepts Covered:** String Length Verification (`LENGTH`), Boundary Char Matching (`RIGHT`/`SUBSTRING`), SARGable Fixed-Length Wildcards (`LIKE`).

#### Method 1: SARGable Fixed-Length Wildcard Match (Highly Optimized)
Uses four positional underscore (`_`) wildcards followed by a terminal character anchor. This forces an exact length constraint of five characters without calling runtime string functions, keeping the query highly efficient.
```sql
SELECT * 
FROM patients 
WHERE first_name LIKE '____a';
```
#### Method 2: String Length with Terminal Suffix Matching
Combines the LENGTH() calculation with standard trailing pattern matching to verify string dimensions and target boundaries cleanly.
```sql
SELECT * 
FROM patients 
WHERE LENGTH(first_name) = 5 
  AND first_name LIKE '%a';
```
#### Method 3: Combined Length and Extraction Functions
Pairs structural length auditing with target boundary extraction via the RIGHT() function to validate string requirements.
```sql
SELECT * 
FROM patients 
WHERE LENGTH(first_name) = 5 
  AND RIGHT(first_name, 1) = 'a';
```
#### Method 4: Pure Positional Boundary Isolation (Advanced Constraint)
Forces both the ending character validation and the strict 5-character length boundary by asserting that the fifth index contains the target letter 'a', while verifying that the sixth index evaluates to an empty string wrapper.
```sql
SELECT * 
FROM patients 
WHERE SUBSTRING(first_name, 5, 1) = 'a' 
  AND SUBSTRING(first_name, 6, 1) = '';
```
### 45. Display admissions where the diagnosis is exactly 3 words long.
* **Concepts Covered:** String Manipulation, Space Character Extraction (`REPLACE`), Character Metric Math, Multi-Boundary Wildcard Filtering (`LIKE`/`NOT LIKE`).

#### Method 1: Mathematical Space Character Counting (Highly Recommended)
Calculates the word count by isolating the volume of spaces within the text block. Because a phrase with exactly 3 words must contain exactly 2 spaces, subtracting the space-less length from the original length yields the precise filter condition.
```sql
SELECT * 
FROM admissions 
WHERE LENGTH(diagnosis) - LENGTH(REPLACE(diagnosis, ' ', '')) = 2;
```
### 46. Show patients who were born in any month except June, July, or August.
* **Concepts Covered:** Date Component Extraction (`MONTHNAME`), Literal Text Set Exclusion (`NOT IN`), Case-Insensitive String Verification.

#### Method 1: Literal String Month Exclusion (Clean & Readable)
Utilizes the `MONTHNAME()` function to extract the full text label of the birth month, evaluating it against a strict set exclusion array to filter out the summer peak.
```sql
SELECT * 
FROM patients 
WHERE MONTHNAME(birth_date) NOT IN ('June', 'July', 'August');
```
### 47. Show all details of doctors whose last name is alphabetically sorted after 'Miller'.
* **Concepts Covered:** Lexicographical Text Evaluation (`>`), String ASCII Comparison, Ordering Datasets (`ORDER BY`).

#### Method 1: Lexicographical String Comparison (Highly Recommended)
Applies a standard greater-than (`>`) comparison operator directly to a text string. SQL naturally evaluates strings character-by-character based on alphabetical sorting rules, capturing all names ranked after the specified string literal.
```sql
SELECT * 
FROM doctors 
WHERE last_name > 'Miller' 
ORDER BY last_name;
```
### 48. Pull all unique patient IDs from admissions who were admitted during the first 10 days of any month.
* **Concepts Covered:** Value Duplication Prevention (`DISTINCT`), Date Part Extraction (`DAY` / `EXTRACT`), Comparison Operators.

#### Method 1: Day Component Integer Filtering (Highly Recommended)
Uses the native `DAY()` function to isolate the calendar day component of the timestamp as an integer, applying a simple relational boundary filter to capture dates between the 1st and the 10th.
```sql
SELECT DISTINCT patient_id 
FROM admissions 
WHERE DAY(admission_date) <= 10;
```
### 49. Show all columns for patients where the city column has an actual text value, but it contains a space (e.g., 'New York').
* **Concepts Covered:** String Pattern Matching (`LIKE`), Wildcard Anchoring (`_`), Data Cleaning Protection (`TRIM`), Blank/Space Anomaly Handling.

#### Method 1: Protected Space Wildcard Matching (Highly Recommended)
Uses a standard space wildcard filter combined with a data-cleaning `TRIM()` condition. This guarantees that rows matching the space requirement represent actual text names rather than empty string wrappers or blank entries.
```sql
SELECT * 
FROM patients 
WHERE city LIKE '% %' 
  AND TRIM(city) != '';
```
#### Method 2:Pure Wildcard Text Anchoring
Employs positional underscore (_) wildcards to force the engine to verify that at least one character exists on both the leading and trailing edges of the space, effectively blocking pure blank fields without calling string functions.
```sql
SELECT * 
FROM patients 
WHERE city LIKE '_% %_';
```
### 50. Show first name, last name, and the full province name for all patients who live in the province of 'Ontario'.
* **Concepts Covered:** Table Joins (`JOIN`), Structural Key Mapping (`ON` vs `USING`), Table Aliasing, Column Ambiguity Prevention.

#### Method 1: Explicit Equi-Join via Key Mapping (Gold Standard)
Connects the operational transactional table to the master entity reference table via an explicit key mapping assertion. Applying descriptive structural aliases prevents column name collisions.
```sql
SELECT 
    p.first_name, 
    p.last_name, 
    pr.province_name 
FROM patients p 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
WHERE pr.province_name = 'Ontario';
```
### 51. Display patient_id, admission_date, and the attending doctor's first and last name concatenated together for every admission.
* **Concepts Covered:** Relational Joins (`JOIN`), Text Concatenation (`CONCAT` vs `CONCAT_WS`), Column Aliasing.

#### Method 1: Standard Multi-Argument Concatenation (Highly Readable)
Executes a traditional table join between transactional admissions and doctor master files, utilizing the standard `CONCAT()` function to manually sandwich a blank spacing string between the target name fields.
```sql
SELECT 
    a.patient_id, 
    a.admission_date, 
    CONCAT(d.first_name, ' ', d.last_name) AS full_name 
FROM admissions a 
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
### 52. Show the first name, last name, and specialty of all doctors who have never attended an admission (Look for unassigned doctors).
* **Concepts Covered:** Exclusionary Joins (`LEFT JOIN`), Filtering Missing Relationships (`IS NULL`), Understanding Cartesian Joins vs. Inequality Operators (`!=`).
#### Method 1: Left Join with Null Filtration (Optimal & Standard)
Dont use != or <> here because when joining two tables, the database conceptually builds a Cartesian Product ($A \times B$). Every single row in the left table is temporarily paired with every single row in the right table.
Executes a left outer join preserving all doctor records, then filters out successfully matched pairings to isolate only the inactive doctors where the corresponding transaction record resolves to `NULL`.
```sql
SELECT 
  d.first_name, 
  d.last_name, 
  d.speciality 
FROM doctors d 
LEFT JOIN admissions a 
  ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;
```
### 53. Find the first name and last name of patients who were attended by a doctor specializing in 'Cardiology'.
* **Concepts Covered:** Chained Relational Joins (`INNER JOIN`), Associative Schema Traversal (Junction Bridging), Target Predicate Filtering (`WHERE`).

#### Method 1: Chained Horizontal Joins (Optimal & High-Performance)
Executes sequential inner joins to bridge the transactional distance between `patients` and `doctors` using `admissions` as an associative junction table, then applies a precise text filter on the doctor's specialty.
```sql
SELECT 
  p.first_name, 
  p.last_name 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id 
WHERE d.speciality = 'Cardiology';
```

### 54. Show the patient_id, diagnosis, and full province name for patients whose diagnosis is 'Pneumonia'.
* **Concepts Covered:** Multi-Table Star Schema Joins (`INNER JOIN`), Relational Mapping, Predicate Filtering (`WHERE`).

#### Method 1: Central Normalized Joins (Optimal & High-Performance)
Executes dual horizontal inner joins using the patient master file as the structural hub to pull transactional records from the admissions log and geographic details from the province master file simultaneously.
```sql
SELECT 
  p.patient_id, 
  a.diagnosis, 
  pr.province_name 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
WHERE a.diagnosis = 'Pneumonia';
```
### 55. Display every doctor's name along with the total number of unique patients they have treated.
* **Concepts Covered:** Aggregation Functions (`COUNT`), Deduplication Metrics (`DISTINCT`), Full-Set Preservation (`LEFT JOIN`), Multi-Column Grouping (`GROUP BY`).

#### Method 1: Left Join with Multi-Column Aggregation (Optimal & Complete)
Executes a left outer join to preserve the entire doctor registry, groups the records by individual doctor names and identification keys, and counts unique patient IDs to accurately report metrics for both active and inactive doctors.
```sql
SELECT 
  d.first_name, 
  d.last_name, 
  COUNT(DISTINCT a.patient_id) AS total_patients 
FROM doctors d 
LEFT JOIN admissions a 
  ON d.doctor_id = a.attending_doctor_id
GROUP BY 
  d.doctor_id, 
  d.first_name, 
  d.last_name;
```
### 56. Show a list of all patients (first and last name) who have been admitted to the hospital more than once under the exact same doctor.
* **Concepts Covered:** Relational Joins (`INNER JOIN`), Multi-Column Grouping (`GROUP BY`), Aggregate Filtering (`HAVING`), Relationship Frequency Metrics.

#### Method 1: Multi-Column Grouping with Aggregate Filtration (Optimal & Standard)
Joins the patient registry with the transactional admissions table, groups the dataset by unique patient and doctor pairings, and evaluates the group frequency using `HAVING COUNT(*) > 1` to isolate repeat admissions under the same physician.
```sql
SELECT 
  p.first_name, 
  p.last_name 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
GROUP BY 
  p.patient_id, 
  p.first_name, 
  p.last_name, 
  a.attending_doctor_id 
HAVING COUNT(*) > 1;
```
### 57. Find the first name and last name of patients who live in a province where the province name ends with the letter 'a'.
* **Concepts Covered:** Wildcard Pattern Matching (`LIKE`), String Extraction Functions (`RIGHT`, `SUBSTRING`), Relational Joins (`INNER JOIN`).

#### Method 1: Trailing Wildcard Search (Optimal & Standard)
Executes an inner join to pair patients with their province data, applying the standard `%a` wildcard filter to locate province names ending in 'a'.
```sql
SELECT 
  p.first_name, 
  p.last_name 
FROM patients p 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
WHERE pr.province_name LIKE '%a';
```
#### Method 2: String Slicing with Negative Offset (SUBSTRING)
Uses a negative starting index (-1) to begin reading from the end of the string, extracting a single character to verify if it equals 'a'.
note: you can also use RIGHT.
```sql
SELECT 
  p.first_name, 
  p.last_name 
FROM patients p 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
WHERE SUBSTRING(pr.province_name, -1, 1) = 'a';
```
### 58. Find pairs of patients who live in the same city and share the exact same last name. Display their names and the city.
* **Concepts Covered:** Relational Self-Joins (`JOIN` on same table), Pair Deduplication Operators (`<` Inequality), Column Aliasing (`AS`).

#### Method 1: Relational Self-Join with Strict Asymmetric Key Comparison (Optimal & Standard)
Joins the `patients` table to itself (`p` and `p0`), matching records on identical city and last name fields. Applies a strict inequality condition (`p.patient_id < p0.patient_id`) to ensure each unique patient pair is represented exactly once without self-matching or duplicate mirror pairs.

```sql
SELECT 
  p.first_name AS patient_1_first_name,
  p0.first_name AS patient_2_first_name,
  p.last_name,
  p.city
FROM patients p 
JOIN patients p0 
  ON p.city = p0.city 
 AND p.last_name = p0.last_name 
 AND p.patient_id < p0.patient_id;
```
### 59. Show all admissions records, including the patient's first name, last name, and the attending doctor's specialty.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Foreign Key Navigation, Record Projection.

#### Method 1: Multi-Table Inner Join with Explicit Field Projection (Optimal & Standard)
Joins the central `admissions` transactional table with both the `patients` and `doctors` dimension tables using their respective primary/foreign key relationships.
```sql
SELECT 
  a.admission_id,
  a.patient_id,
  a.admission_date,
  a.discharge_date,
  a.diagnosis,
  a.attending_doctor_id,
  p.first_name AS patient_first_name,
  p.last_name AS patient_last_name,
  d.specialty AS doctor_specialty
FROM admissions a
JOIN patients p 
  ON a.patient_id = p.patient_id
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
#### Method 2: Wildcard Record Projection (a.*)
Retrieves all raw columns directly from the admissions table while joining adjacent tables to project patient names and doctor specialties.
```sql
SELECT 
  p.first_name, 
  p.last_name, 
  d.specialty, 
  a.* 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
### 60. Show patient_id, full name, and the total number of days they spent in the hospital across all admissions combined.
* **Concepts Covered:** Date Arithmetic (`DATEDIFF`), Aggregate Summation (`SUM`), String Concatenation (`CONCAT_WS`), Relational Grouping (`GROUP BY`).

#### Method 1: DATEDIFF Aggregation with CONCAT_WS (Optimal & Standard)
Joins patient records to admission logs, calculates the duration of each individual stay using `DATEDIFF()`, and aggregates total duration per patient using `SUM()`.

```sql
SELECT 
  p.patient_id,
  CONCAT_WS(' ', p.first_name, p.last_name) AS full_name,
  SUM(DATEDIFF(a.discharge_date, a.admission_date)) AS total_days
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id
GROUP BY 
  p.patient_id,
  p.first_name,
  p.last_name;
```
### 61. List all provinces along with the total count of doctors who have treated a patient from that province.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Geographic Aggregation (`GROUP BY`), Distinct Cardinality Aggregation (`COUNT(DISTINCT)`).

#### Method 1: Relational Join with Distinct Doctor Aggregation (Optimal & Standard)
Joins patient records with admission logs and geographic master data (`province_names`). Uses `COUNT(DISTINCT)` to deduplicate attending doctor IDs so each unique doctor is counted once per province group.

```sql
SELECT 
  pr.province_name,
  COUNT(DISTINCT a.attending_doctor_id) AS doctor_count
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id
JOIN province_names pr 
  ON p.province_id = pr.province_id 
GROUP BY 
  pr.province_name;
```
### 62. Find the diagnosis that has been assigned to patients from the highest number of different provinces.
* **Concepts Covered:** Multi-Table Joins (`INNER JOIN`), Distinct Aggregation (`COUNT(DISTINCT)`), Result Ordering (`ORDER BY`), Top-N Filtering (`LIMIT`).

#### Method 1: Distinct Province Counting with Limit (Optimal & Standard)
Groups admission records by diagnosis and calculates the cardinality of unique geographic provinces (`COUNT(DISTINCT p.province_id)`). Sorts the resulting counts in descending order and limits output to the top record.

```sql
SELECT 
  a.diagnosis,
  COUNT(DISTINCT p.province_id) AS province_count
FROM admissions a
JOIN patients p 
  ON a.patient_id = p.patient_id
GROUP BY 
  a.diagnosis
ORDER BY 
  province_count DESC
LIMIT 1;
```
### 63. Show patient_id, first_name, and admission_date for patients whose attending doctor has the first name 'Michael'.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Foreign Key Navigation, Filter Conditions (`WHERE`).

#### Method 1: Multi-Table Relational Join (Optimal & Standard)
Joins the `patients`, `admissions`, and `doctors` tables to map patient admissions back to the attending doctor, filtering specifically for doctors named 'Michael'.

```sql
SELECT 
  p.patient_id, 
  p.first_name, 
  a.admission_date 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id 
WHERE d.first_name = 'Michael';
```
### 64. Display every patient's first name, last name, and their doctor's specialty. If they haven't been admitted yet, show 'No Admission'.
* **Concepts Covered:** Outer Relational Joins (`LEFT JOIN`), Conditional Null Value Substitution (`CASE WHEN` / `COALESCE`).

#### Method 1: LEFT JOIN with CASE WHEN Conditional Formatting (Optimal & Standard)
Performs an outer join starting from the master `patients` directory down through `admissions` and `doctors`. Employs a `CASE WHEN` block to check for missing relational records and substitute `'No Admission'` for unassigned doctor specialties.

```sql
SELECT 
  p.first_name,
  p.last_name,
  CASE 
    WHEN d.specialty IS NULL THEN 'No Admission'
    ELSE d.specialty
  END AS doctor_specialty
FROM patients p
LEFT JOIN admissions a 
  ON p.patient_id = a.patient_id
LEFT JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
#### Method 2: Concise Substitution with COALESCE
Uses the standard ANSI COALESCE() function to fall back to the default string 'No Admission' whenever d.specialty evaluates to NULL.
```sql
SELECT 
  p.first_name,
  p.last_name,
  COALESCE(d.specialty, 'No Admission') AS doctor_specialty
FROM patients p
LEFT JOIN admissions a 
  ON p.patient_id = a.patient_id
LEFT JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
### 65. Find all patients who were admitted on the exact same day that another patient was discharged.
* **Concepts Covered:** Self-Joins (`INNER JOIN` on same table), Relational Inequality (`<>`), Cardinality Deduplication (`DISTINCT`).

#### Method 1: Self-Join on Date Alignment (Optimal & Standard)
Performs a self-join on the `admissions` table matching `admission_date` from instance `a1` with `discharge_date` from instance `a2`, enforcing `a1.patient_id <> a2.patient_id` to isolate distinct patients.

```sql
SELECT DISTINCT 
  p.first_name,
  p.last_name
FROM patients p
JOIN admissions a1 
  ON p.patient_id = a1.patient_id
JOIN admissions a2 
  ON a1.admission_date = a2.discharge_date 
  AND a1.patient_id <> a2.patient_id;
```
### 66. Show the name of the province that has the highest number of recorded patient admissions.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Relational Aggregation (`GROUP BY`), Sorting (`ORDER BY`), Top-N Filtering (`LIMIT`).

#### Method 1: Relational Join with Count Ordering & Limit (Optimal & Standard)
Joins `patients`, `admissions`, and `province_names` to calculate total recorded admissions per province group. Sorts the counts in descending order and uses `LIMIT 1` to isolate the top province.

```sql
SELECT 
  pr.province_name 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
JOIN province_names pr 
  ON p.province_id = pr.province_id
GROUP BY 
  pr.province_name 
ORDER BY 
  COUNT(*) DESC 
LIMIT 1;
```
### 67. Find all doctors who have treated patients with 'Asthma' and display the total number of asthma patients they treated.
* **Concepts Covered:** Relational Joins (`INNER JOIN`), Row-Level Filtering (`WHERE`), Aggregation with Grouping (`GROUP BY`), Distinct Patient Counting (`COUNT(DISTINCT)`).

#### Method 1: Pre-Aggregation Row Filtering with WHERE (Optimal & Standard)
Filters admission logs specifically for 'Asthma' diagnoses in the `WHERE` clause prior to grouping, aggregating unique patient counts per attending doctor.

```sql
SELECT 
  d.first_name,
  d.last_name,
  COUNT(DISTINCT a.patient_id) AS total_asthma_patients
FROM doctors d
JOIN admissions a 
  ON d.doctor_id = a.attending_doctor_id
WHERE 
  a.diagnosis = 'Asthma'
GROUP BY 
  d.doctor_id,
  d.first_name,
  d.last_name;
```
### 68. Show the city and the average weight of patients in that city, but only display cities where the average weight is over 75kg.
* **Concepts Covered:** Group-Level Aggregation (`GROUP BY`), Average Calculation (`AVG`), Aggregate Group Filtering (`HAVING`).

#### Method 1: Group By with HAVING Aggregate Filter (Optimal & Standard)
Groups patient records by city, calculates the average weight per group, and uses the `HAVING` clause to filter out cities where the average weight is 75kg or less.

```sql
SELECT 
  city, 
  AVG(weight) AS average_weight 
FROM patients 
GROUP BY 
  city 
HAVING 
  AVG(weight) > 75;
```
### 69. Show the attending_doctor_id and the total number of admissions they handled, sorted from highest to lowest admissions.
* **Concepts Covered:** Group-Level Aggregation (`GROUP BY`), Cardinality Deduplication (`COUNT(DISTINCT)`), Result Sorting (`ORDER BY`).

#### Method 1: Distinct Patient Aggregation per Doctor (Optimal & Standard)
Groups admission logs by `attending_doctor_id` to evaluate unique patient admissions handled per doctor, ordering the results from highest to lowest volume.

```sql
SELECT 
  attending_doctor_id, 
  COUNT(DISTINCT patient_id) AS count_of_admissions 
FROM admissions
GROUP BY 
  attending_doctor_id 
ORDER BY 
  count_of_admissions DESC;
```
### 70. For each specialty, find the average height of patients treated by doctors in that specialty.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Aggregate Calculations (`AVG`), Numeric Formatting (`ROUND`), Relational Grouping (`GROUP BY`).

#### Method 1: Relational Join with Rounded Average Aggregation (Optimal & Standard)
Joins `patients`, `admissions`, and `doctors` to map patient measurements back to attending physician specialties. Groups results by `d.specialty` and calculates the rounded average patient height.

```sql
SELECT 
  d.specialty, 
  ROUND(AVG(p.height), 2) AS avg_height 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id
GROUP BY 
  d.specialty;
```
### 71. Find the province IDs where the total number of patients living there is less than 50.
* **Concepts Covered:** Group-Level Aggregation (`GROUP BY`), Cardinality Deduplication (`COUNT(DISTINCT)`), Aggregate Group Filtering (`HAVING`).

#### Method 1: Group By with HAVING Aggregate Filter (Optimal & Standard)
Groups patient records by `province_id`, calculates total patient count per group, and filters out provinces with 50 or more patients using the `HAVING` clause.

```sql
SELECT 
  province_id 
FROM patients 
GROUP BY 
  province_id 
HAVING 
  COUNT(patient_id) < 50;
```
### 72. For each unique diagnosis, display the diagnosis name and the minimum and maximum age of patients who received it.
* **Concepts Covered:** Date Arithmetic (`TIMESTAMPDIFF` / `strftime`), Min/Max Aggregations (`MIN`, `MAX`), Relational Joins (`INNER JOIN`), Relational Grouping (`GROUP BY`).

#### Method 1: SQLite Date Functionality (`strftime`)
Extracts year components using `strftime('%Y')` to compute patient age differences, grouping by diagnosis to extract `MIN()` and `MAX()` extremes.

```sql
SELECT 
  a.diagnosis,
  MIN(strftime('%Y', 'now') - strftime('%Y', p.birth_date)) AS min_age,
  MAX(strftime('%Y', 'now') - strftime('%Y', p.birth_date)) AS max_age
FROM patients p
JOIN admissions a 
  ON p.patient_id = a.patient_id
GROUP BY 
  a.diagnosis;
```
#### Method 2: MySQL Standard Syntax (TIMESTAMPDIFF)
Calculates precise year boundaries between birth_date and `CURDATE()` using` TIMESTAMPDIFF(YEAR, ...)`.
```sql
SELECT 
  a.diagnosis,
  MIN(TIMESTAMPDIFF(YEAR, p.birth_date, CURDATE())) AS min_age,
  MAX(TIMESTAMPDIFF(YEAR, p.birth_date, CURDATE())) AS max_age
FROM patients p
JOIN admissions a 
  ON p.patient_id = a.patient_id
GROUP BY 
  a.diagnosis;
```
### 73. Show the admission year and the total number of admissions that took place in that year.
* **Concepts Covered:** Date Part Extraction (`YEAR` / `strftime`), Event Aggregation (`COUNT`), Relational Grouping (`GROUP BY`).

#### Method 1: Standard SQL Date Function (`YEAR`)
Uses the standard `YEAR()` scalar function to isolate the calendar year from `admission_date` and aggregate total admission events per year.

```sql
SELECT 
  YEAR(admission_date) AS admission_year,
  COUNT(*) AS total_admissions
FROM admissions
GROUP BY 
  YEAR(admission_date);
```
Note: If using an SQLite environment (such as sql-practice.com), you can replace `YEAR(admission_date)` with `strftime('%Y', admission_date)`.

### 74. Display the patient_id and the total number of admissions they had, but only for patients with more than 3 admissions.
* **Concepts Covered:** Group-Level Aggregation (`GROUP BY`), Event Counting (`COUNT`), Aggregate Group Filtering (`HAVING`).

#### Method 1: Group By with HAVING Aggregate Filter (Optimal & Standard)
Groups admission logs by `patient_id`, counts total admissions per patient, and filters for patients with strictly more than 3 recorded admissions using `HAVING`.

```sql
SELECT 
  patient_id, 
  COUNT(patient_id) AS count_of_admissions 
FROM admissions 
GROUP BY 
  patient_id 
HAVING 
  COUNT(patient_id) > 3;
```
### 75. Find the average duration of a hospital stay (Discharge date minus Admission date) grouped by the patient's gender.
* **Concepts Covered:** Date Arithmetic (`DATEDIFF` / `julianday`), Aggregate Calculations (`AVG`), Relational Joins (`INNER JOIN`), Grouping (`GROUP BY`).

#### Method 1: Standard MySQL Syntax (`DATEDIFF`)
Calculates the length of stay per admission using `DATEDIFF()` and aggregates average duration per patient gender.

```sql
SELECT 
  p.gender,
  AVG(DATEDIFF(a.discharge_date, a.admission_date)) AS avg_duration 
FROM admissions a 
JOIN patients p 
  ON p.patient_id = a.patient_id 
GROUP BY 
  p.gender;
```
### 76. Show the city, gender, and total count of patients grouped by city and then by gender.
* **Concepts Covered:** Multi-Column Grouping (`GROUP BY`), Record Aggregation (`COUNT`).

#### Method 1: Multi-Column Group By Aggregation (Optimal & Standard)
Groups patient records by `city` first, then subgroups by `gender`, calculating the total patient count per combination.

```sql
SELECT 
  city, 
  gender, 
  COUNT(patient_id) AS patient_count 
FROM patients 
GROUP BY 
  city, 
  gender;
```
### 77. Find the total weight of all male patients living in province_id 'ON'.
* **Concepts Covered:** Conditional Row Filtering (`WHERE`), Group-Level Aggregation (`GROUP BY` / `HAVING`), Numeric Aggregation (`SUM`).

#### Method 1: Pre-Filtered Aggregate Sum (Optimal & Standard)
Filters raw patient records using `WHERE` before aggregating, minimizing total row processing.

```sql
SELECT 
  SUM(weight) AS total_weight 
FROM patients 
WHERE gender = 'M' 
  AND province_id = 'ON';
```
### 78. Display the doctor's specialty and the total amount of unique diagnoses they have issued, filtered for specialties with more than 5 unique diagnoses.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Distinct Group Aggregation (`COUNT(DISTINCT)`), Aggregate Group Filtering (`HAVING`).

#### Method 1: Relational Join with Distinct HAVING Filter (Optimal & Standard)
Joins admissions with doctor profiles, aggregates distinct diagnosis strings per specialty, and filters out specialties with 5 or fewer unique diagnoses using `HAVING`.

```sql
SELECT 
  d.specialty, 
  COUNT(DISTINCT a.diagnosis) AS unique_diagnoses 
FROM admissions a 
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id 
GROUP BY 
  d.specialty 
HAVING 
  COUNT(DISTINCT a.diagnosis) > 5;
```
### 79. Show the patient_id and the earliest (oldest) admission date they have on record.
* **Concepts Covered:** Group Aggregation (`GROUP BY`), Minimum Value Extraction (`MIN`).

#### Method 1: Group By with MIN Aggregate Function (Optimal & Standard)
Groups admission records by `patient_id` and applies `MIN(admission_date)` to determine each patient's initial admission date.

```sql
SELECT 
  patient_id, 
  MIN(admission_date) AS earliest_admission_date 
FROM admissions 
GROUP BY 
  patient_id;
```
### 80. Find the average height of patients grouped by their birth year, ordered by birth year ascending.
* **Concepts Covered:** Date Part Extraction (`YEAR` / `strftime`), Numeric Aggregation (`AVG`), Relational Grouping (`GROUP BY`), Sorting (`ORDER BY`).

#### Method 1: Standard SQL Date Function (`YEAR`)
Extracts the year component from `birth_date`, calculates the average height per birth year group, and orders the output chronologically.

```sql
SELECT 
  YEAR(birth_date) AS birth_year, 
  AVG(height) AS avg_height 
FROM patients 
GROUP BY 
  YEAR(birth_date) 
ORDER BY 
  birth_year ASC;
```
### 81. Show the province names that have an average patient weight between 65kg and 85kg.
* **Concepts Covered:** Relational Joins (`INNER JOIN`), Grouping Aggregation (`GROUP BY`), Range Filtering on Aggregates (`HAVING` / `BETWEEN`).

#### Method 1: Relational Join with HAVING Range Filter (Optimal & Standard)
Joins patient demographics with province definitions, calculates the average patient weight per province, and filters the aggregated groups using `HAVING ... BETWEEN`.

```sql
SELECT 
  pr.province_name 
FROM patients p 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
GROUP BY 
  pr.province_name 
HAVING 
  AVG(p.weight) BETWEEN 65 AND 85;
```
### 82. Count how many patients have a last name that starts with each letter of the alphabet. Group by the starting letter.
* **Concepts Covered:** String Extraction (`LEFT` / `SUBSTR`), Group Aggregation (`GROUP BY`), Sorting (`ORDER BY`).

#### Method 1: Using `LEFT()` Function (Optimal & Standard)
Extracts the first character of `last_name` using `LEFT()`, groups records by that starting character, and calculates total patient counts.

```sql
SELECT 
  LEFT(last_name, 1) AS alphabet, 
  COUNT(patient_id) AS total_counts 
FROM patients 
GROUP BY 
  LEFT(last_name, 1) 
ORDER BY 
  alphabet ASC;
```
### 83. Find the total number of admissions handled by each doctor specialty.
* **Concepts Covered:** Multi-Table Relational Joins (`INNER JOIN`), Group-Level Aggregation (`GROUP BY`), Count Aggregation (`COUNT`).

#### Method 1: Relational Join with Group Aggregation (Optimal & Standard)
Joins admission records to doctor profiles using `attending_doctor_id`, groups by `specialty`, and counts total admission records per specialty category.

```sql
SELECT 
  dr.specialty, 
  COUNT(a.patient_id) AS total_admissions 
FROM admissions a 
JOIN doctors dr 
  ON a.attending_doctor_id = dr.doctor_id 
GROUP BY 
  dr.specialty;
```
### 84. Show the month number (1–12) and the total number of patients born in that specific month.
* **Concepts Covered:** Date Part Extraction (`MONTH` / `strftime`), Record Aggregation (`COUNT`), Relational Grouping (`GROUP BY`), Sorting (`ORDER BY`).

#### Method 1: Standard SQL Date Function (`MONTH`)
Extracts the month integer (1 through 12) from `birth_date` using `MONTH()`, groups patients by month, and orders the output chronologically.

```sql
SELECT 
  MONTH(birth_date) AS month_number, 
  COUNT(patient_id) AS total_patients 
FROM patients 
GROUP BY 
  MONTH(birth_date) 
ORDER BY 
  month_number ASC;
```
### 85. Display the patient_id and average length of stay for patients whose max stay in a single visit was over 10 days.
* **Concepts Covered:** Date Arithmetic (`DATEDIFF`), Grouping Aggregation (`GROUP BY`), Aggregate Filtering (`HAVING`), Group Level Extremes (`MAX` / `AVG`).

#### Method 1: Aggregate Group Filtering with HAVING (Optimal & Standard)
Groups admission records by `patient_id`, calculates each patient's average length of stay, and uses `HAVING MAX(...) > 10` to include only patients with at least one visit exceeding 10 days.

```sql
SELECT 
  patient_id, 
  AVG(DATEDIFF(discharge_date, admission_date)) AS avg_length_of_stay 
FROM admissions 
GROUP BY 
  patient_id 
HAVING 
  MAX(DATEDIFF(discharge_date, admission_date)) > 10;
```
### 86. Find cities where the total number of female patients is exactly zero.
* **Concepts Covered:** Conditional Aggregation (`SUM(gender = 'F')`), Aggregate Group Filtering (`HAVING`), Subquery Exclusion (`NOT IN`).

#### Method 1: Conditional Aggregation with HAVING (Optimal & Standard)
Groups records by `city` and sums boolean flags (`1` for Female, `0` for Male) in `HAVING` to isolate cities where the female total is strictly 0.

```sql
SELECT 
  city 
FROM patients 
GROUP BY 
  city 
HAVING 
  SUM(gender = 'F') = 0;
```
### 87. Show the attending_doctor_id who has treated patients from at least 3 distinct provinces.
* **Concepts Covered:** Relational Joins (`INNER JOIN`), Grouping Aggregation (`GROUP BY`), Distinct Value Counting (`COUNT(DISTINCT)`), Aggregate Group Filtering (`HAVING`).

#### Method 1: Relational Join with HAVING COUNT(DISTINCT) (Optimal & Standard)
Joins admission records with patient demographic data, groups by doctor ID, and counts unique `province_id` values per doctor to filter for those meeting or exceeding the 3-province threshold.

```sql
SELECT 
  a.attending_doctor_id 
FROM admissions a 
JOIN patients p 
  ON a.patient_id = p.patient_id 
GROUP BY 
  a.attending_doctor_id 
HAVING 
  COUNT(DISTINCT p.province_id) >= 3;
```
### 88. Categorize patients by weight classes using CASE WHEN.
* **Concepts Covered:** Conditional Categorization (`CASE WHEN`), Range Filtering (`BETWEEN`), Derived Display Columns (`AS`).

#### Method 1: Explicit Range Evaluation with BETWEEN (Optimal & Standard)
Evaluates `weight` against explicit numerical boundaries to categorize patients into 'Underweight', 'Normal', or 'Overweight' weight classes.

```sql
SELECT 
  patient_id, 
  weight, 
  CASE 
    WHEN weight < 50 THEN 'Underweight' 
    WHEN weight BETWEEN 50 AND 80 THEN 'Normal' 
    WHEN weight > 80 THEN 'Overweight' 
  END AS weight_class 
FROM patients;
```
### 89. Show all patient details for patients who weigh more than the average weight of all patients in the database.
* **Concepts Covered:** Scalar Subqueries (`WHERE column > (SELECT ...)`), Aggregate Summary Calculation (`AVG`).

#### Method 1: Scalar Subquery in WHERE Clause (Optimal & Standard)
Uses a nested scalar subquery to calculate the global average weight first, then filters row-by-row in the outer query for patients exceeding that threshold.

```sql
SELECT * 
FROM patients 
WHERE weight > (
  SELECT AVG(weight) 
  FROM patients
);
```
### 90. Display the first name, last name, and a masked string where the first 3 letters of the last name are attached to their birth year.
* **Concepts Covered:** String Manipulation (`CONCAT`, `SUBSTRING` / `LEFT`), Date Part Extraction (`YEAR` / `strftime`), Column Aliasing (`AS`).

#### Method 1: Standard String Concatenation & Substring (Optimal & Standard)
Extracts the initial 3 characters of `last_name`, pulls the 4-digit year from `birth_date`, and joins them together using `CONCAT()`.

```sql
SELECT 
  first_name, 
  last_name, 
  CONCAT(SUBSTRING(last_name, 1, 3), YEAR(birth_date)) AS password 
FROM patients;
```
### 91. Display all admissions where the diagnosis is the most common diagnosis in the table.
* **Concepts Covered:** Scalar Subqueries (`WHERE column = (SELECT ...)`), Frequency Aggregation (`COUNT(*)`), Result Set Limiting (`ORDER BY ... DESC LIMIT 1`).

#### Method 1: Scalar Subquery with Aggregation & Limit (Optimal & Standard)
Uses an inner query to group admissions by `diagnosis`, counts frequencies to sort descending, and uses `LIMIT 1` to isolate the mode diagnosis for outer query filtering.

```sql
SELECT * 
FROM admissions 
WHERE diagnosis = (
  SELECT diagnosis 
  FROM admissions 
  GROUP BY diagnosis 
  ORDER BY COUNT(*) DESC 
  LIMIT 1
);
```
### 92. Translate gender codes ('M'/'F') into full text ('Male'/'Female') using a conditional statement.
* **Concepts Covered:** Conditional Mapping (`CASE WHEN`), Value Translation, Column Aliasing (`AS`).

#### Method 1: Explicit Conditional Evaluation (Optimal & Standard)
Uses `CASE WHEN` to evaluate `gender` values line-by-line and outputs mapped full-text labels as `Gender_Full`.

```sql
SELECT 
  *, 
  CASE 
    WHEN gender = 'M' THEN 'Male' 
    WHEN gender = 'F' THEN 'Female' 
  END AS Gender_Full 
FROM patients;
```
### 93. Format first names to uppercase followed by character length in parentheses.
* **Concepts Covered:** String Case Formatting (`UPPER`), String Length Calculation (`LENGTH` / `LEN`), String Concatenation (`CONCAT`).

#### Method 1: Standard String Concatenation & Length (Optimal & Standard)
Converts `first_name` to uppercase, calculates its string character length, and joins them with parenthesis formatting.

```sql
SELECT 
  CONCAT(UPPER(first_name), ' (', LENGTH(first_name), ')') AS formatted_name 
FROM patients;
```
### 94. Update doctor first names to include 'Dr. ' prefix if not already present.
* **Concepts Covered:** Data Modification (`UPDATE`), String Prepending (`CONCAT`), Pattern Matching Safeguards (`NOT LIKE`).

#### Method 1: Conditional Update with NOT LIKE (Optimal & Standard)
Uses `UPDATE` with a `WHERE NOT LIKE 'Dr. %'` clause to ensure records that already carry the 'Dr. ' prefix are safely excluded from duplicate concatenation.

```sql
UPDATE doctors 
SET first_name = CONCAT('Dr. ', first_name) 
WHERE first_name NOT LIKE 'Dr. %';
```
### 95. Find patients who have never been admitted using NOT EXISTS.
* **Concepts Covered:** Subquery Correlated Evaluation (`NOT EXISTS`), Unmatched Record Identification, Anti-Join Operations.

#### Method 1: Correlated Subquery with NOT EXISTS (Optimal & Standard)
Evaluates each patient row against the `admissions` table inside a subquery, keeping only patient records where no matching admission exists.

```sql
SELECT * 
FROM patients p 
WHERE NOT EXISTS (
  SELECT 1 
  FROM admissions a 
  WHERE a.patient_id = p.patient_id
);
```
### 96. Display patient details with a binary indicator (1/0) for allergy status.
* **Concepts Covered:** Conditional Binary Flagging (`CASE WHEN`), Null Value Checking (`IS NOT NULL`), Fallback Assignment (`ELSE`), Column Aliasing (`AS`).

#### Method 1: Explicit CASE WHEN with Numeric Flags (Optimal & Standard)
Evaluates whether the `allergies` field contains a valid entry (not NULL and not empty) and maps it to a binary integer `1` (Yes) or `0` (No).

```sql
SELECT 
  patient_id, 
  first_name, 
  CASE 
    WHEN allergies IS NOT NULL AND allergies != '' THEN 1 
    ELSE 0 
  END AS Has_Allergies 
FROM patients;
```
### 97. Find the patient with the second-highest height without using LIMIT or TOP.
* **Concepts Covered:** Double Nested Subqueries (`WHERE column = (SELECT ...)`), Aggregate Max Searching (`MAX()`), Filtering Without Limit Syntax.

#### Method 1: Double Nested Subqueries with MAX() (Optimal & Standard)
Uses an inner scalar subquery to find the absolute maximum height, a middle subquery to find the highest height less than that maximum, and an outer query to fetch matching patient records.

```sql
SELECT * 
FROM patients 
WHERE height = (
  SELECT MAX(height) 
  FROM patients 
  WHERE height < (
    SELECT MAX(height) 
    FROM patients
  )
);
```
### 98. Combine city and province code into standard mailing format ("City, PROVINCE_ID") using CONCAT_WS.
* **Concepts Covered:** Separator String Concatenation (`CONCAT_WS`), Null-Safe Formatting, Column Aliasing (`AS`).

#### Method 1: CONCAT_WS Separator Formatting (Optimal & Standard)
Uses `CONCAT_WS(', ', ...)` to automatically join text fields using a comma-and-space separator while gracefully skipping NULL values if present.

```sql
SELECT 
  city, 
  province_id, 
  CONCAT_WS(', ', city, province_id) AS format 
FROM province_names;
```
### 99. Find all diagnoses that have been given to both male and female patients.
* **Concepts Covered:** Grouping Aggregation (`GROUP BY`), Multi-Category Distinct Counting (`COUNT(DISTINCT)`), Group Filtering (`HAVING`).

#### Method 1: GROUP BY with HAVING COUNT(DISTINCT gender) (Optimal & Standard)
Groups admissions by `diagnosis` and counts unique gender distinct values per group, ensuring both 'M' and 'F' exist (distinct count = 2).

```sql
SELECT a.diagnosis 
FROM patients p 
JOIN admissions a ON p.patient_id = a.patient_id 
GROUP BY a.diagnosis 
HAVING COUNT(DISTINCT p.gender) = 2;
```
### 100. Display patients whose weight is equal to the minimum weight of patients in their same city.
* **Concepts Covered:** Correlated Grouping, Aggregate Subqueries (`MIN()`), Self/Derived Table Joins, Partition Filtering.

#### Method 1: Derived Table Aggregation Join (Optimal & Standard)
Uses an inner subquery to calculate the minimum weight per city, then joins back to the main `patients` table on both `city` and `weight`.

```sql
SELECT 
  p.first_name, 
  p.last_name 
FROM patients p 
JOIN (
  SELECT 
    city, 
    MIN(weight) AS min_weight 
  FROM patients 
  GROUP BY city
) AS s 
  ON p.city = s.city 
WHERE p.weight = s.min_weight;
```
### 101. Calculate the percentage of total patients that are female.
* **Concepts Covered:** Conditional Aggregation (`CASE WHEN` / Boolean Flags), Ratio Calculation, Integer Division Safety, Decimal Rounding (`ROUND`).

#### Method 1: AVG() Boolean Shortcut (Optimal for MySQL / SQLite)
Averages a boolean condition (`gender = 'F'`), which returns a decimal ratio (0.0 to 1.0), then scales by 100 and rounds to a clean integer.

```sql
SELECT 
  ROUND(AVG(gender = 'F') * 100) AS percentage_of_females 
FROM patients;
```
### 102. Find admissions where the diagnosis text contains the patient's own first name.
* **Concepts Covered:** Dynamic Pattern Matching (`LIKE`), String Concatenation (`CONCAT`), Wildcard Search (`%`), Dynamic Column Evaluation.

#### Method 1: Dynamic Pattern Matching with CONCAT (Optimal & Standard)
Dynamically builds a wildcard search string combining leading/trailing `%` characters with `p.first_name` to perform a substring match inside `a.diagnosis`.

```sql
SELECT 
  p.patient_id, 
  a.diagnosis 
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id 
WHERE 
  a.diagnosis LIKE CONCAT('%', p.first_name, '%');
```
### 103. Find all doctors who have treated at least one patient with a Penicillin allergy.
* **Concepts Covered:** Filtering Subqueries (`WHERE ... IN`), Pattern Substring Matching (`LIKE`), Deduplication (`DISTINCT`), Multi-Table Joins.

#### Method 1: Subquery Filtering with IN (Optimal & Direct)
Filters doctors whose IDs appear in a nested subquery that retrieves attending doctor IDs associated with patients who have 'Penicillin' in their allergies.

```sql
SELECT 
  first_name, 
  last_name 
FROM doctors 
WHERE doctor_id IN (
  SELECT DISTINCT a.attending_doctor_id 
  FROM admissions a 
  JOIN patients p ON a.patient_id = p.patient_id 
  WHERE p.allergies LIKE '%Penicillin%'
);
```
### 104. Output a formatted summary string for every patient admission.
* **Concepts Covered:** String Concatenation (`CONCAT`), Date-to-Text Formatting, Table Joins (`JOIN`), Column Aliasing (`AS`).

#### Method 1: CONCAT String Formatting (Optimal & Standard)
Joins `patients` and `admissions` to combine string literals and column values into a single formatted sentence per admission.

```sql
SELECT 
  CONCAT(
    p.first_name, ' ', 
    p.last_name, ' was admitted on ', 
    a.admission_date, ' for ', 
    a.diagnosis
  ) AS admission_details
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id;
```
### 105. Find the average height of patients who do not live in 'Toronto', grouped by province name.
* **Concepts Covered:** Grouping Aggregation (`GROUP BY`), Average Function (`AVG()`), Inequality Filtering (`!=` / `<>`), Table Joins (`JOIN`).

#### Method 1: JOIN with WHERE Filter & GROUP BY (Optimal & Standard)
Filters out patients residing in 'Toronto' before grouping by `province_name` and calculating the average height per province.

```sql
SELECT 
  pr.province_name, 
  ROUND(AVG(p.height), 2) AS avg_height 
FROM patients p 
JOIN province_names pr 
  ON p.province_id = pr.province_id 
WHERE p.city != 'Toronto' 
GROUP BY pr.province_name;
```
#### Method 2: Derived Table Subquery with Explicit Column Aliasing
Uses an inner subquery to pre-join and filter patients from non-Toronto cities. Explicit column aliases (patient_prov_id, master_prov_id) are assigned to avoid column name collisions exiting the subquery boundary before the outer GROUP BY executes.

```sql
SELECT 
  sub.province_name, 
  ROUND(AVG(sub.height), 2) AS avg_height 
FROM (
  SELECT 
    p.height, 
    p.province_id AS patient_prov_id, 
    pr.province_id AS master_prov_id, 
    pr.province_name 
  FROM patients p 
  JOIN province_names pr 
    ON p.province_id = pr.province_id 
  WHERE p.city != 'Toronto'
) AS sub 
GROUP BY sub.province_name;
```
### 106. Update empty (`NULL`) discharge dates in admissions to the current date.
* **Concepts Covered:** Data Modification (`UPDATE`), Conditional Filtering (`WHERE ... IS NULL`), Current Date Functions (`CURRENT_DATE()` / `CURDATE()`), `COALESCE`.

#### Method 1: Standard UPDATE with IS NULL Filter (Optimal)
Targeted update that modifies only rows where `discharge_date` is currently `NULL`, setting them to the current system date.

```sql
UPDATE admissions 
SET discharge_date = CURRENT_DATE() 
WHERE discharge_date IS NULL;
```
#### Method 2: COALESCE Fallback UPDATE
Uses COALESCE to evaluate existing dates and fall back to the current date if NULL.
```sql
UPDATE admissions 
SET discharge_date = COALESCE(discharge_date, CURRENT_DATE()) 
WHERE discharge_date IS NULL;
```
# 🚀 Phase 2: Advanced SQL, Window Functions & Analytics (#107 – #206)

> **Focus Areas:** Window Functions (`OVER`, `PARTITION BY`, `ORDER BY`), Frame Specifications (`ROWS BETWEEN`), Navigational Queries (`LAG`/`LEAD`/`FIRST_VALUE`), Advanced CTEs, Recursive Logic, and Complex Healthcare Analytics.

---

### 🏛️ Key Concepts Quick Reference

| Category | Functions / Keywords | Key Use Case |
| :--- | :--- | :--- |
| **Ranking** | `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()` | Top-N per group, deduplication, quantile division |
| **Navigational** | `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()` | Row-to-row comparisons, time gaps, visit history |
| **Aggregate Windows** | `SUM() OVER()`, `AVG() OVER()`, `COUNT() OVER()` | Running totals, moving averages, group benchmark comparisons |
| **Frame Bounds** | `ROWS BETWEEN ... PRECEDING AND ... FOLLOWING` | Rolling multi-day calculations, centered metrics |
| **Advanced CTEs** | `WITH ... AS (...)`, Recursive CTEs | Gaps & Islands problems, date generation, complex pipelines |

---

### 107. For each patient, rank their admissions chronologically from earliest to latest using ROW_NUMBER().
* **Concepts Covered:** Window Functions (`OVER`), Partitioning (`PARTITION BY`), Sorting Windows (`ORDER BY`), Sequential Ranking (`ROW_NUMBER()`).

#### SQL Method
Assigns a unique chronological sequence number to every admission associated with a patient using `ROW_NUMBER()`.

```sql
SELECT 
  a.patient_id, 
  a.admission_date, 
  ROW_NUMBER() OVER (
    PARTITION BY a.patient_id 
    ORDER BY a.admission_date
  ) AS adrank 
FROM admissions a;
```
### 108. Find the most recent admission record for every patient without using MAX() with GROUP BY.
* **Concepts Covered:** Deduplication, Window Functions (`ROW_NUMBER()`), Descending Order (`ORDER BY ... DESC`), Derived Table Filtering.

#### SQL Method
Ranks each patient's admissions in descending chronological order inside a subquery, then filters for `adrank = 1` in the outer query to extract complete details of their latest visit.

```sql
SELECT * 
FROM (
  SELECT 
    *, 
    ROW_NUMBER() OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date DESC
    ) AS adrank 
  FROM admissions
) AS sub 
WHERE adrank = 1;
```
### 109. Rank doctors based on the total number of admissions they handled using DENSE_RANK().
* **Concepts Covered:** Aggregate Functions (`COUNT`), Window Functions (`DENSE_RANK()`), Table Joins (`JOIN`), Grouping (`GROUP BY`).

#### SQL Method
Groups admissions by doctor to sum up total handled admissions, then applies `DENSE_RANK()` in descending order so doctors with the same admission total share the same rank without skipping rank numbers.

```sql
SELECT 
  d.doctor_id,
  d.first_name,
  d.last_name,
  COUNT(a.admission_date) AS total_admissions,
  DENSE_RANK() OVER (
    ORDER BY COUNT(a.admission_date) DESC
  ) AS doctor_rank
FROM doctors d
JOIN admissions a 
  ON d.doctor_id = a.attending_doctor_id
GROUP BY 
  d.doctor_id, 
  d.first_name, 
  d.last_name;
```
### 110. Find the top 3 highest-weight patients in each province using `ROW_NUMBER()`.
* **Concepts Covered:** Subqueries / CTEs, Window Functions (`ROW_NUMBER()`), Partitioning (`PARTITION BY`), Filtering (`WHERE`).

#### SQL Method
Partitions patient records by `province_id` and orders them by `weight` in descending order (`DESC`) so that the heaviest patients in each province are assigned row numbers `1`, `2`, and `3`. A subquery wraps this logic to filter for `weight_rank BETWEEN 1 AND 3`, using a meaningful alias (`weight_rank`) to clearly describe the ranked output.

```sql
SELECT 
  patient_id, 
  province_id, 
  weight
FROM (
  SELECT 
    patient_id, 
    province_id, 
    weight, 
    ROW_NUMBER() OVER (
      PARTITION BY province_id 
      ORDER BY weight DESC
    ) AS weight_rank 
  FROM patients
) AS ranked_patients 
WHERE weight_rank BETWEEN 1 AND 3;
```
### 111. Divide all patients into 4 equal weight quartiles using `NTILE(4)`.
* **Concepts Covered:** Window Functions (`NTILE()`), Data Binning / Bucketing, Ordering (`ORDER BY`).

#### SQL Method
Applies `NTILE(4)` over the entire table ordered by `weight` in ascending order (`ASC`). This splits the patients evenly into 4 buckets (quartiles), where bucket `1` contains the lightest 25% of patients and bucket `4` contains the heaviest 25%.

```sql
SELECT 
  patient_id,
  first_name,
  last_name,
  weight,
  NTILE(4) OVER (
    ORDER BY weight ASC
  ) AS weight_quartile
FROM patients;
```
### 112. Rank patients within each city by height, where ties receive the same rank and leave gaps in ranking (`RANK()`).
* **Concepts Covered:** Window Functions (`RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Partitions patient records by `city` and applies `RANK()` ordered by `height DESC` so that patients inside each city are ranked from tallest to shortest. When patients share the exact same height, they receive the same rank, and the next rank skips numbers accordingly (e.g., 1, 2, 2, 4).

```sql
SELECT 
  patient_id, 
  city, 
  height, 
  RANK() OVER (
    PARTITION BY city 
    ORDER BY height DESC
  ) AS height_rank 
FROM patients;
```
### 113. Identify patients who have had more than 3 admissions, and select only their 2nd and 4th admission records.
* **Concepts Covered:** Subqueries / CTEs, Window Functions (`ROW_NUMBER()`, `COUNT() OVER`), Pre-filtering (`HAVING`), Performance Optimization.

#### Method 1: Subquery Approach (Single-Pass Window Functions)
Uses `ROW_NUMBER()` to sequence admission records and `COUNT() OVER()` to calculate total patient admissions in a single subquery pass, filtering for patients with > 3 admissions and extracting their 2nd and 4th records.

```sql
SELECT 
  patient_id,
  admission_date,
  discharge_date,
  diagnosis,
  attending_doctor_id
FROM (
  SELECT 
    patient_id,
    admission_date,
    discharge_date,
    diagnosis,
    attending_doctor_id,
    ROW_NUMBER() OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) AS rownumber,
    COUNT(patient_id) OVER (
      PARTITION BY patient_id
    ) AS rowcount
  FROM admissions
) AS tab
WHERE rowcount > 3 
  AND rownumber IN (2, 4);
```
#### Method 2: Optimized CTE Approach (Early Pre-Filtering)
Pre-filters qualifying patient IDs using GROUP BY ... HAVING COUNT(*) > 3 before applying window functions. This reduces memory overhead by running ROW_NUMBER() only on eligible patients.
```sql
WITH FrequentPatients AS (
  SELECT patient_id
  FROM admissions
  GROUP BY patient_id
  HAVING COUNT(*) > 3
),
RankedAdmissions AS (
  SELECT 
    a.patient_id,
    a.admission_date,
    a.discharge_date,
    a.diagnosis,
    a.attending_doctor_id,
    ROW_NUMBER() OVER (
      PARTITION BY a.patient_id 
      ORDER BY a.admission_date ASC
    ) AS rownumber
  FROM admissions a
  JOIN FrequentPatients fp 
    ON a.patient_id = fp.patient_id
)
SELECT 
  patient_id,
  admission_date,
  discharge_date,
  diagnosis,
  attending_doctor_id
FROM RankedAdmissions
WHERE rownumber IN (2, 4);
```
### 114. Find the second most common diagnosis per province using ranking functions.
* **Concepts Covered:** Common Table Expressions (`WITH`), Aggregation (`COUNT` / `GROUP BY`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`).

#### Method 1: Optimized CTE Approach (Recommended)
Groups diagnosis records by `province_id` and `diagnosis` to compute occurrence counts, then applies `DENSE_RANK()` partitioned by `province_id` in descending order of frequency. The outer query filters for `rank_num = 2` to extract the second most common diagnosis per province.

```sql
WITH DiagnosisCounts AS (
  SELECT 
    p.province_id,
    a.diagnosis,
    COUNT(*) AS diagnosis_count
  FROM patients p
  JOIN admissions a 
    ON p.patient_id = a.patient_id
  GROUP BY 
    p.province_id, 
    a.diagnosis
),
RankedDiagnoses AS (
  SELECT 
    province_id,
    diagnosis,
    diagnosis_count,
    DENSE_RANK() OVER (
      PARTITION BY province_id 
      ORDER BY diagnosis_count DESC
    ) AS rank_num
  FROM DiagnosisCounts
)
SELECT 
  province_id,
  diagnosis,
  diagnosis_count
FROM RankedDiagnoses
WHERE rank_num = 2;
```
### 115. Assign a unique sequence number to every admission associated with each doctor, sorted by admission date.
* **Concepts Covered:** Window Functions (`ROW_NUMBER()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

####  Method 1
Uses `ROW_NUMBER()` partitioned by `attending_doctor_id` and ordered by `admission_date` in ascending order. This assigns an incremental sequential number (`1, 2, 3...`) to each doctor's admissions sorted by date.

```sql
SELECT 
  attending_doctor_id, 
  patient_id, 
  admission_date, 
  ROW_NUMBER() OVER (
    PARTITION BY attending_doctor_id 
    ORDER BY admission_date ASC
  ) AS sequence_number 
FROM admissions;
```
### 116. List all patients whose weight ranks in the top 10% within their province.
* **Concepts Covered:** Common Table Expressions (`WITH`), Window Functions (`NTILE()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### Method
Uses `NTILE(10)` partitioned by `province_id` and ordered by `weight DESC` to divide patients within each province into 10 equal deciles (10% buckets) from heaviest to lightest. Filtering for `weight_decile = 1` isolates the top 10% heaviest patients in each province.

```sql
WITH RankedPatients AS (
  SELECT 
    patient_id, 
    weight, 
    province_id, 
    NTILE(10) OVER (
      PARTITION BY province_id 
      ORDER BY weight DESC
    ) AS weight_decile 
  FROM patients
)
SELECT 
  patient_id, 
  weight, 
  province_id 
FROM RankedPatients 
WHERE weight_decile = 1;
```
### 117. Rank patients by age (calculated from `birth_date`) within each gender group.
* **Concepts Covered:** Date Functions (`TIMESTAMPDIFF`, `CURDATE`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Uses `TIMESTAMPDIFF(YEAR, birth_date, CURDATE())` to calculate each patient's age in years. Applies `DENSE_RANK()` partitioned by `gender` and sorted by `birth_date ASC` (or `age DESC`) to rank patients within their gender group from oldest to youngest.

```sql
SELECT 
  patient_id, 
  gender,
  birth_date,
  TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) AS age, 
  DENSE_RANK() OVER (
    PARTITION BY gender 
    ORDER BY birth_date ASC
  ) AS age_rank
FROM patients;
```
### 118. Find the doctor who treated the tallest patient in each province using window ranking.
* **Concepts Covered:** Table Joins (`JOIN`), Common Table Expressions (`WITH`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Joins `patients` with `admissions` and uses `DENSE_RANK()` partitioned by `province_id` and ordered by `height DESC` to rank admissions by patient height within each province. Filtering for `height_rank = 1` isolates the attending doctor(s) who treated the tallest patient(s) in every province.

```sql
WITH RankedPatients AS (
  SELECT 
    a.attending_doctor_id, 
    p.province_id, 
    p.height, 
    DENSE_RANK() OVER (
      PARTITION BY p.province_id 
      ORDER BY p.height DESC
    ) AS height_rank
  FROM patients p 
  JOIN admissions a 
    ON p.patient_id = a.patient_id
)
SELECT 
  attending_doctor_id,
  province_id,
  height
FROM RankedPatients 
WHERE height_rank = 1;
```
### 119. Partition patients by city and rank them by BMI ($\text{weight} / \text{height}^2$).
* **Concepts Covered:** Mathematical Functions (`POWER`, `ROUND`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### Method 1: Direct Window Calculation
Calculates BMI using `weight / POWER(height / 100.0, 2)` and applies `DENSE_RANK()` partitioned by `city` in descending order of BMI.

```sql
SELECT 
  patient_id, 
  city, 
  ROUND(weight / POWER(height / 100.0, 2), 2) AS bmi, 
  DENSE_RANK() OVER (
    PARTITION BY city 
    ORDER BY weight / POWER(height / 100.0, 2) DESC
  ) AS bmi_rank 
FROM patients;
```
### 120. Identify ties in admission counts among doctors and display them using both `RANK()` and `DENSE_RANK()` to show the difference.
* **Concepts Covered:** Aggregation (`GROUP BY`), Window Functions (`RANK()`, `DENSE_RANK()`), Sorting (`ORDER BY`), Tie Handling.

#### SQL Method
Groups admissions by `attending_doctor_id` to compute total admissions per doctor. Applies both `RANK()` and `DENSE_RANK()` ordered by `COUNT(admission_date) DESC` to clearly highlight how `RANK()` introduces gaps in sequence after tied values while `DENSE_RANK()` keeps rankings consecutive.

```sql
SELECT 
  attending_doctor_id, 
  COUNT(admission_date) AS admission_count, 
  RANK() OVER (
    ORDER BY COUNT(admission_date) DESC
  ) AS justrank,
  DENSE_RANK() OVER (
    ORDER BY COUNT(admission_date) DESC
  ) AS densrrank
FROM admissions 
GROUP BY attending_doctor_id;
```
### 121. Rank admissions by length of stay (`discharge_date - admission_date`) per diagnosis category.
* **Concepts Covered:** Date Functions (`DATEDIFF`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Calculates the length of stay for each admission using `DATEDIFF(discharge_date, admission_date)`. Uses `DENSE_RANK()` partitioned by `diagnosis` and sorted by length of stay in descending order to rank patient stays within each medical category.

```sql
SELECT 
  patient_id,
  diagnosis,
  admission_date,
  discharge_date,
  DATEDIFF(discharge_date, admission_date) AS length_of_stay,
  DENSE_RANK() OVER (
    PARTITION BY diagnosis 
    ORDER BY DATEDIFF(discharge_date, admission_date) DESC
  ) AS stay_rank
FROM admissions;
```
### 122. Select the top 1 most frequent attending doctor for each patient.
* **Concepts Covered:** Common Table Expressions (`WITH`), Aggregation (`GROUP BY`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Groups admissions by `patient_id` and `attending_doctor_id` to calculate total visit counts. Uses `DENSE_RANK()` partitioned by `patient_id` and ordered by visit count descending to rank doctors per patient, then filters for `doctor_rank = 1`.

```sql
WITH DoctorVisits AS (
  SELECT 
    patient_id, 
    attending_doctor_id, 
    COUNT(*) AS total_visits 
  FROM admissions 
  GROUP BY 
    patient_id, 
    attending_doctor_id
),
RankedDoctors AS (
  SELECT 
    patient_id, 
    attending_doctor_id, 
    total_visits, 
    DENSE_RANK() OVER (
      PARTITION BY patient_id 
      ORDER BY total_visits DESC
    ) AS doctor_rank 
  FROM DoctorVisits
)
SELECT 
  patient_id, 
  attending_doctor_id, 
  total_visits 
FROM RankedDoctors 
WHERE doctor_rank = 1;
```
### 123. Assign a row number to patients ordered by `last_name, first_name` within each province.
* **Concepts Covered:** Window Functions (`ROW_NUMBER()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Uses `ROW_NUMBER()` partitioned by `province_id` and ordered by `last_name, first_name` to assign sequential row numbers to patients sorted alphabetically within each province group.

```sql
SELECT 
  patient_id,
  first_name,
  last_name,
  province_id,
  ROW_NUMBER() OVER (
    PARTITION BY province_id 
    ORDER BY last_name ASC, first_name ASC
  ) AS rows1
FROM patients;
```
### 124. Find the 5th oldest patient in each city.
* **Concepts Covered:** Common Table Expressions (`WITH`), Date Functions (`TIMESTAMPDIFF`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Calculates each patient's age using `TIMESTAMPDIFF(YEAR, birth_date, CURDATE())`. Uses `DENSE_RANK()` partitioned by `city` and ordered by age descending (or `birth_date ASC`) to rank patients by age within their respective city. Filters the CTE for `age_rank = 5` to select the 5th oldest patient in each city.

```sql
WITH RankedPatients AS (
  SELECT 
    patient_id, 
    first_name, 
    last_name, 
    city, 
    birth_date,
    TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) AS age, 
    DENSE_RANK() OVER (
      PARTITION BY city 
      ORDER BY TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) DESC
    ) AS age_rank 
  FROM patients
)
SELECT 
  patient_id, 
  first_name, 
  last_name, 
  city, 
  birth_date,
  age 
FROM RankedPatients 
WHERE age_rank = 5;
```
### 125. Partition admissions by year and rank the peak admission days per year.
* **Concepts Covered:** Date Functions (`YEAR`), Aggregation (`GROUP BY`), Window Functions (`DENSE_RANK()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Groups admissions by `admission_date` to determine daily admission counts, then uses `DENSE_RANK()` partitioned by `YEAR(admission_date)` and ordered by daily total descending to isolate peak admission days for every year.

```sql
WITH DailyAdmissions AS (
  SELECT 
    admission_date, 
    YEAR(admission_date) AS admission_year, 
    COUNT(*) AS total_admissions 
  FROM admissions 
  GROUP BY 
    admission_date, 
    YEAR(admission_date)
),
RankedDays AS (
  SELECT 
    admission_date, 
    admission_year, 
    total_admissions, 
    DENSE_RANK() OVER (
      PARTITION BY admission_year 
      ORDER BY total_admissions DESC
    ) AS peak_rank 
  FROM DailyAdmissions
)
SELECT 
  admission_date, 
  admission_year, 
  total_admissions 
FROM RankedDays 
WHERE peak_rank = 1;
```
### 126. Divide doctors into 3 tiers based on their total patient volume using `NTILE(3)`
* **Concepts Covered:** Common Table Expressions (`WITH`), Aggregation (`GROUP BY`), Window Functions (`NTILE()`), Sorting (`ORDER BY`).

#### SQL Method
Groups admissions by `attending_doctor_id` to compute each doctor's total patient volume. Applies `NTILE(3) OVER (ORDER BY total_patients DESC)` to divide doctors evenly into 3 performance tiers based on volume.

```sql
WITH DoctorVolumes AS (
  SELECT 
    attending_doctor_id, 
    COUNT(patient_id) AS total_patients 
  FROM admissions 
  GROUP BY attending_doctor_id
)
SELECT 
  attending_doctor_id, 
  total_patients, 
  NTILE(3) OVER (
    ORDER BY total_patients DESC
  ) AS volume_tier 
FROM DoctorVolumes;
```
### 127. For each admission, calculate the number of days since the patient's previous admission (`LAG`).
* **Concepts Covered:** Date Functions (`DATEDIFF`), Window Functions (`LAG()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Uses `LAG(admission_date, 1)` partitioned by `patient_id` and ordered chronologically by `admission_date ASC` to fetch the previous admission date, then applies `DATEDIFF()` to calculate the day gap between consecutive visits.

```sql
SELECT 
  patient_id,
  admission_date,
  LAG(admission_date, 1) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS previous_admission_date,
  DATEDIFF(
    admission_date, 
    LAG(admission_date, 1) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    )
  ) AS days_since_last_visit
FROM admissions;
```
####  Method step by step understanding

```sql
with tab as (select patient_id, admission_date, lag(admission_date,1)
 over(partition by patient_id order by admission_date asc) as previous_date
from admissions)
select *, datediff(admission_date,previous_date) as no_of_days from tab;
```
### 128. Identify readmitted patients who were readmitted within 30 days of their prior discharge date.
* **Concepts Covered:** Common Table Expressions (`WITH`), Window Functions (`LEAD()`), Date Functions (`DATEDIFF()`), Deduplication (`DISTINCT`).

#### SQL Method
Uses `LEAD(admission_date)` with chronological ordering (`ASC`) partitioned by `patient_id` to look forward to the subsequent admission date, then calculates the gap from the current stay's `discharge_date` using `DATEDIFF()`.

```sql
WITH NextAdmissions AS (
  SELECT 
    patient_id,
    DATEDIFF(
      LEAD(admission_date) OVER (
        PARTITION BY patient_id 
        ORDER BY admission_date ASC
      ),
      discharge_date
    ) AS days_to_next_admission
  FROM admissions
)
SELECT DISTINCT 
  patient_id
FROM NextAdmissions
WHERE days_to_next_admission BETWEEN 0 AND 30;
```
### 129. Compare each patient's current admission diagnosis with their immediately preceding diagnosis.
* **Concepts Covered:** Window Functions (`LAG()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Partitions records by `patient_id` and sorts chronologically by `admission_date ASC`, using `LAG(diagnosis)` to retrieve the previous visit's diagnosis for direct side-by-side comparison.

```sql
SELECT 
  patient_id, 
  admission_date, 
  diagnosis AS current_diagnosis, 
  LAG(diagnosis) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS previous_diagnosis
FROM admissions;
```
### 130. Display each patient's height alongside the height of the next patient admitted in the same hospital.
* **Concepts Covered:** `JOIN`, Window Functions (`LEAD()`), Sorting (`ORDER BY`).

#### SQL Method
Joins `patients` and `admissions` on `patient_id` and uses `LEAD(p.height, 1) OVER (ORDER BY a.admission_date ASC)` to display each admitted patient's height next to the height of the patient admitted immediately after them.

```sql
SELECT 
  a.patient_id, 
  p.height, 
  a.admission_date,
  LEAD(p.height, 1) OVER (
    ORDER BY a.admission_date ASC
  ) AS lead_height
FROM patients p 
JOIN admissions a 
  ON p.patient_id = a.patient_id;
```
### 131. Find the primary attending doctor assigned to a patient's very first admission (`FIRST_VALUE`).
* **Concepts Covered:** Window Functions (`FIRST_VALUE()`), Partitioning (`PARTITION BY`), Sorting (`ORDER BY`).

#### SQL Method
Partitions records by `patient_id` and sorts chronologically by `admission_date ASC` so `FIRST_VALUE(attending_doctor_id)` anchors to and returns the attending doctor from the patient's earliest admission.

```sql
SELECT 
  patient_id, 
  admission_date, 
  attending_doctor_id, 
  FIRST_VALUE(attending_doctor_id) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS first_attending_doctor_id
FROM admissions;
```
### 132. Calculate the weight difference between each patient's current record and the overall heaviest patient in their city.
* **Concepts Covered:** Window Functions (`FIRST_VALUE` / `MAX() OVER`), In-query Arithmetic Subtraction, Partitioning (`PARTITION BY`).

#### SQL Method 1: Using FIRST_VALUE
Partitions by `city`, orders by `weight DESC` to put the max weight first, and subtracts the current row's `weight`.

```sql
SELECT 
  patient_id, 
  city, 
  weight,
  FIRST_VALUE(weight) OVER (
    PARTITION BY city 
    ORDER BY weight DESC
  ) - weight AS weight_diff 
FROM patients;
```
### 133. Detect cases where a patient changed primary attending doctors between consecutive admissions.
* **Concepts Covered:** Window Functions (`LAG()`), Conditional Logic (`CASE WHEN`), Handling `NULL`s, Partitioning (`PARTITION BY`).

#### SQL Method
Uses `LAG(attending_doctor_id)` partitioned by `patient_id` and ordered chronologically by `admission_date ASC`, then applies a `CASE WHEN` statement to identify whether the attending physician differs from the previous visit.

```sql
SELECT 
  patient_id, 
  admission_date, 
  attending_doctor_id, 
  LAG(attending_doctor_id) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS previous_doctor_id,
  CASE 
    WHEN LAG(attending_doctor_id) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) IS NULL THEN 'First Admission'
    WHEN attending_doctor_id <> LAG(attending_doctor_id) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) THEN 'Doctor Changed'
    ELSE 'Same Doctor'
  END AS doctor_change_status
FROM admissions;
```
### 134. Calculate the change in total daily hospital admission count compared to the previous day.
* **Concepts Covered:** Common Table Expressions (`WITH`), Aggregation (`COUNT` / `GROUP BY`), Window Functions (`LAG()`), Day-over-Day Math.

#### SQL Method
Aggregates admissions count by `admission_date`, then applies `LAG()` ordered chronologically to calculate the day-over-day net change (`today - yesterday`).

```sql
WITH DailyAdmissions AS (
  SELECT 
    admission_date, 
    COUNT(*) AS total_admissions
  FROM admissions
  GROUP BY admission_date
)
SELECT 
  admission_date, 
  total_admissions, 
  total_admissions - LAG(total_admissions, 1) OVER (
    ORDER BY admission_date ASC
  ) AS daily_change
FROM DailyAdmissions;
```
### 135. For each patient, calculate the time gap (in days) between their first ever admission and their most recent admission.
* **Concepts Covered:** Date Difference (`DATEDIFF`), Aggregations (`MIN`/`MAX`), Window Functions (`FIRST_VALUE`, `LAST_VALUE`, `MIN() OVER`), Window Framing (`ROWS BETWEEN`), Subqueries / Self-Joins (`ROW_NUMBER()`).

---

#### Method 1: Standard Aggregation (Most Optimized & Production Standard)
Groups records by `patient_id`, identifies the boundary dates using `MIN(admission_date)` and `MAX(admission_date)`, and computes the day span using `DATEDIFF`.

```sql
SELECT 
  patient_id,
  MIN(admission_date) AS first_admission_date,
  MAX(admission_date) AS most_recent_admission_date,
  DATEDIFF(MAX(admission_date), MIN(admission_date)) AS total_days_span
FROM admissions
GROUP BY patient_id;
```
#### Method 2: Windowed Aggregates (MIN() / MAX() OVER)
Calculates the patient-level date span without collapsing individual visit records, preserving all underlying admission rows.

```sql
SELECT 
  patient_id,
  admission_date,
  DATEDIFF(
    MAX(admission_date) OVER (PARTITION BY patient_id),
    MIN(admission_date) OVER (PARTITION BY patient_id)
  ) AS total_days_span
FROM admissions;
```
#### Method 3: FIRST_VALUE() with Dual Ordering
Uses FIRST_VALUE() twice: once ordered ASC for the earliest date, and once ordered DESC for the most recent date. Uses DISTINCT to return one row per patient.

```sql
SELECT DISTINCT
  patient_id,
  DATEDIFF(
    FIRST_VALUE(admission_date) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date DESC
    ),
    FIRST_VALUE(admission_date) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    )
  ) AS total_days_span
FROM admissions;
```
### 136. Find the last recorded diagnosis for each patient using `LAST_VALUE()` with proper window frame bounds.
* **Concepts Covered:** Window Functions (`LAST_VALUE()`), Window Frame Bounds (`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`), Partitioning (`PARTITION BY`).

#### SQL Method
Partitions records by `patient_id` ordered chronologically by `admission_date ASC`. An explicit window frame `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` expands the window beyond the default current row boundary, allowing `LAST_VALUE()` to accurately return the latest diagnosis.

```sql
SELECT DISTINCT
  patient_id, 
  LAST_VALUE(diagnosis) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS last_recorded_diagnosis
FROM admissions;
```
### 137. Find the previous admission date for each doctor's patients.
* **Concepts Covered:** Window Functions (`LAG()`), Multi-Column Partitioning (`PARTITION BY`), Chronological Sorting.

#### SQL Method
Partitions records simultaneously by `attending_doctor_id` and `patient_id` ordered by `admission_date ASC` to track consecutive visit timelines per doctor-patient relationship using `LAG()`.

```sql
SELECT 
  attending_doctor_id, 
  patient_id, 
  admission_date, 
  LAG(admission_date, 1) OVER (
    PARTITION BY attending_doctor_id, patient_id 
    ORDER BY admission_date ASC
  ) AS previous_admission_date
FROM admissions;
```
### 138. Calculate the percentage change in admission counts month-over-month using `LAG()`.
* **Concepts Covered:** Common Table Expressions (`CTE`), Window Functions (`LAG()`), Monthly Aggregations (`GROUP BY`), Percentage Difference Formula, Floating-point division (`100.0`), `ROUND()`.

#### SQL Method
First aggregates admission counts per month inside a CTE, then computes month-over-month (MoM) percentage change using `LAG()` to reference the prior month's count.

```sql
WITH MonthlyCounts AS (
  SELECT 
    MONTH(admission_date) AS admission_month,
    COUNT(*) AS total_admissions
  FROM admissions
  GROUP BY MONTH(admission_date)
)
SELECT 
  admission_month,
  total_admissions,
  LAG(total_admissions) OVER (ORDER BY admission_month ASC) AS previous_month_admissions,
  ROUND(
    (total_admissions - LAG(total_admissions) OVER (ORDER BY admission_month ASC)) * 100.0 
    / LAG(total_admissions) OVER (ORDER BY admission_month ASC), 
    2
  ) AS mom_pct_change
FROM MonthlyCounts;
```
### 139. Identify patients whose diagnosis changed between every consecutive visit.
* **Concepts Covered:** Window Functions (`LAG()`), Conditional Aggregation (`MIN(CASE ...)`), Filtering Aggregates (`HAVING`), Edge-case handling for single-admission patients.

#### SQL Method
Uses `LAG()` inside a CTE to find each prior visit's diagnosis. In the outer query, groups by `patient_id` and filters via `HAVING` to verify that the patient has multiple visits (`COUNT(*) > 1`) and zero repeat diagnoses on consecutive admissions (`MIN(...) = 1`).

```sql
WITH DiagnosisTransitions AS (
  SELECT 
    patient_id,
    diagnosis,
    LAG(diagnosis) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) AS prev_diagnosis
  FROM admissions
)
SELECT 
  patient_id
FROM DiagnosisTransitions
GROUP BY patient_id
HAVING 
  COUNT(*) > 1
  AND MIN(
    CASE 
      WHEN prev_diagnosis IS NULL THEN 1
      WHEN diagnosis != prev_diagnosis THEN 1 
      ELSE 0 
    END
  ) = 1;
```
### 140. Retrieve the `first_name` and `last_name` of the doctor assigned to a patient's latest admission using `FIRST_VALUE()`.
* **Concepts Covered:** Window Functions (`FIRST_VALUE()`), `JOIN`, Partitioning & Reverse Chronological Sorting, `DISTINCT`.

#### SQL Method
Joins `admissions` with `doctors` on `attending_doctor_id`. Applies `FIRST_VALUE()` partitioned per `patient_id` and ordered by `admission_date DESC` to retrieve the latest attending doctor, deduplicating records with `DISTINCT`.

```sql
SELECT DISTINCT
  a.patient_id,
  FIRST_VALUE(d.first_name) OVER (
    PARTITION BY a.patient_id 
    ORDER BY a.admission_date DESC
  ) AS doctor_first_name,
  FIRST_VALUE(d.last_name) OVER (
    PARTITION BY a.patient_id 
    ORDER BY a.admission_date DESC
  ) AS doctor_last_name
FROM admissions a
JOIN doctors d 
  ON a.attending_doctor_id = d.doctor_id;
```
### 141. Find admissions where the length of stay was shorter than the patient's previous admission's length of stay.
* **Concepts Covered:** Common Table Expressions (`CTE`), Date Functions (`DATEDIFF`), Window Functions (`LAG()`).

#### SQL Method
Calculates length of stay in days and retrieves the preceding visit's duration per patient using `LAG()`. The outer query filters for records where the current stay is strictly shorter than the prior stay.

```sql
WITH StayComparison AS (
  SELECT 
    patient_id,
    admission_date,
    discharge_date,
    DATEDIFF(discharge_date, admission_date) AS length_of_stay,
    LAG(DATEDIFF(discharge_date, admission_date)) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) AS prev_length_of_stay
  FROM admissions
)
SELECT 
  patient_id,
  admission_date,
  discharge_date,
  length_of_stay,
  prev_length_of_stay
FROM StayComparison
WHERE length_of_stay < prev_length_of_stay;
```
### 142. Show the next 2 upcoming admission dates for each patient using LEAD(col, 1) and LEAD(col, 2).
* **Concepts Covered:** Window Functions (`LEAD()`), Multi-step Offsets, Partitioning & Chronological Ordering.

#### SQL Method
Uses `LEAD()` with explicit offset parameters `1` and `2` partitioned by `patient_id` and ordered chronologically by `admission_date`.

```sql
SELECT 
  patient_id, 
  admission_date, 
  LEAD(admission_date, 1) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS upcoming_first,
  LEAD(admission_date, 2) OVER (
    PARTITION BY patient_id 
    ORDER BY admission_date ASC
  ) AS upcoming_second
FROM admissions;
```
### 143. Determine if a patient's weight increased or decreased between consecutive hospital visits.
* **Concepts Covered:** Common Table Expressions (`CTE`), Window Functions (`LAG()`), Conditional Categorization (`CASE WHEN`).

#### SQL Method
Retrieves the previous visit's weight per patient using `LAG()` ordered chronologically by `admission_date`. Categorizes each subsequent visit into 'Increased', 'Decreased', or 'No Change' using a `CASE WHEN` expression.

```sql
WITH WeightTransitions AS (
  SELECT 
    patient_id,
    admission_date,
    weight,
    LAG(weight) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ) AS prev_weight
  FROM admissions
)
SELECT 
  patient_id,
  admission_date,
  weight AS current_weight,
  prev_weight,
  CASE 
    WHEN prev_weight IS NULL THEN 'Initial Visit'
    WHEN weight > prev_weight THEN 'Increased'
    WHEN weight < prev_weight THEN 'Decreased'
    ELSE 'No Change'
  END AS weight_trend
FROM WeightTransitions;
```
### 144. Find the first and last admission diagnosis for every patient in a single row.
* **Concepts Covered:** Window Functions (`FIRST_VALUE()`, `LAST_VALUE()`), Window Frame Specification (`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`), Output Deduplication (`DISTINCT`), String Concatenation (`CONCAT`).

#### SQL Method
Extracts the earliest diagnosis using `FIRST_VALUE()` and the final diagnosis using `LAST_VALUE()` with a full-partition frame specification. Deduplicates per patient via `DISTINCT` and formats the output into a single string.

```sql
SELECT DISTINCT
  patient_id,
  CONCAT(
    FIRST_VALUE(diagnosis) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
    ),
    ' and ',
    LAST_VALUE(diagnosis) OVER (
      PARTITION BY patient_id 
      ORDER BY admission_date ASC
      ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    )
  ) AS first_and_last_diagnosis
FROM admissions;
```
### 145. Calculate the difference between the current patient's height and the average height of the next 3 admitted patients.
* **Concepts Covered:** Table Joins (`INNER JOIN`), Window Functions (`AVG()`), Explicit Window Frames (`ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING`), Numeric Rounding (`ROUND()`).

#### SQL Method
Joins `admissions` to `patients` to access height data, then uses an explicit forward-looking window frame `ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING` ordered by `admission_date` to calculate the moving average and difference.

```sql
SELECT 
  a.patient_id,
  a.admission_date,
  p.height AS current_height,
  ROUND(
    AVG(p.height) OVER (
      ORDER BY a.admission_date ASC
      ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING
    ), 
    2
  ) AS next_3_avg_height,
  ROUND(
    p.height - AVG(p.height) OVER (
      ORDER BY a.admission_date ASC
      ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING
    ), 
    2
  ) AS height_diff
FROM admissions a
JOIN patients p ON a.patient_id = p.patient_id;
```
### 146. Compare each doctor's monthly admission count against their own previous month's count.
* **Concepts Covered:** Common Table Expressions (`CTE`), Aggregate Grouping (`GROUP BY`), Window Navigation (`LAG()`), Window Partitioning (`PARTITION BY`).

#### SQL Method
Aggregates monthly admissions per doctor using a CTE, then calculates Month-over-Month (MoM) variance by subtracting the previous month's count (`LAG()`) from the current month's count partitioned by doctor.

```sql
WITH tab AS (
  SELECT 
    attending_doctor_id,
    MONTH(admission_date) AS month1, 
    COUNT(*) AS count1 
  FROM admissions 
  GROUP BY 
    attending_doctor_id,
    MONTH(admission_date)
)
SELECT 
  attending_doctor_id,
  month1,
  count1 AS current_m_count,
  LAG(count1, 1) OVER (
    PARTITION BY attending_doctor_id 
    ORDER BY month1 ASC
  ) AS previous_m_count,
  count1 - LAG(count1, 1) OVER (
    PARTITION BY attending_doctor_id 
    ORDER BY month1 ASC
  ) AS diff
FROM tab;
```
### 147. Compute a daily cumulative running total of hospital admissions over time.
* **Concepts Covered:** Cumulative Aggregates (`SUM() OVER`), Common Table Expressions (`CTE`), Window Framing (`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`), Group Aggregation (`GROUP BY`).

#### Industry standard SQL Method
Aggregates admissions by `admission_date` in a CTE, then applies `SUM(daily_count) OVER (ORDER BY admission_date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` to generate a strict row-by-row running total.

```sql
WITH DailyAdmissions AS (
  SELECT 
    admission_date,
    COUNT(*) AS daily_count
  FROM admissions
  GROUP BY admission_date
)
SELECT 
  admission_date,
  daily_count,
  SUM(daily_count) OVER (
    ORDER BY admission_date ASC
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_admissions
FROM DailyAdmissions;
```
#### simple Method
```sql
SELECT DISTINCT 
  admission_date, 
  COUNT(patient_id) OVER (ORDER BY admission_date) AS cumulativecount 
FROM admissions;
```
### 148. Display each patient's weight alongside their city's average weight and the difference between them.
* **Concepts Covered:** Window Aggregate Partitioning (`AVG() OVER (PARTITION BY ...)`), Cumulative vs Static Framing, Numeric Precision (`ROUND()`).

#### SQL Method
Uses `AVG(weight) OVER (PARTITION BY city)` without an `ORDER BY` clause to calculate the static overall city average across all rows, then computes the patient variance.

```sql
SELECT 
  patient_id,
  city,
  weight,
  ROUND(AVG(weight) OVER (PARTITION BY city), 2) AS city_avg_weight,
  ROUND(
    weight - AVG(weight) OVER (PARTITION BY city), 
    2
  ) AS weight_diff
FROM patients;
```
### 149. Calculate a 7-day moving average of daily admission counts.
* **Concepts Covered:** Common Table Expressions (`CTE`), Group Aggregations (`GROUP BY`), Rolling Window Frames (`ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`), Numeric Rounding (`ROUND()`).

#### SQL Method
Aggregates daily admissions in a CTE, then computes a 7-day trailing moving average by defining a window frame across the previous 6 days and the current day.

```sql
WITH DailyAdmissions AS (
  SELECT 
    admission_date,
    COUNT(*) AS daily_count
  FROM admissions
  GROUP BY admission_date
)
SELECT 
  admission_date,
  daily_count,
  ROUND(
    AVG(daily_count) OVER (
      ORDER BY admission_date ASC
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ),
    2
  ) AS moving_avg_7day
FROM DailyAdmissions;
```
### 150. Display each admission along with the percentage contribution it represents toward that doctor's total admissions.
* **Concepts Covered:** Window Partition Aggregates (`SUM() OVER (PARTITION BY ...)`), Ratio-to-Report / Percentage Contribution, Decimal Precision Handling (`100.0`), Common Table Expressions (`CTE`).

#### SQL Method
Aggregates daily patient visits per doctor in a CTE, then calculates the percentage contribution of each date against the doctor's grand total using an un-ordered partition window sum.

```sql
WITH DailyDoctorAdmissions AS (
  SELECT 
    attending_doctor_id,
    admission_date,
    COUNT(*) AS daily_admissions
  FROM admissions
  GROUP BY 
    attending_doctor_id,
    admission_date
)
SELECT 
  attending_doctor_id,
  admission_date,
  daily_admissions,
  SUM(daily_admissions) OVER (
    PARTITION BY attending_doctor_id
  ) AS doctor_total_admissions,
  ROUND(
    100.0 * daily_admissions / SUM(daily_admissions) OVER (PARTITION BY attending_doctor_id),
    2
  ) AS daily_pct_contribution
FROM DailyDoctorAdmissions;
```
### 151. Calculate the running total count of admissions handled by each doctor, ordered by admission date.
* **Concepts Covered:** Common Table Expressions (`CTE`), Aggregate Grouping (`GROUP BY`), Cumulative Window Aggregates (`SUM() OVER`), Window Partitioning (`PARTITION BY`).

#### SQL Method
Pre-aggregates daily admissions per doctor inside a CTE, then applies `SUM(daily_admissions) OVER (PARTITION BY attending_doctor_id ORDER BY admission_date ASC)` to calculate a cumulative running total across dates.

```sql
WITH DailyDoctorAdmissions AS (
  SELECT 
    attending_doctor_id,
    admission_date,
    COUNT(*) AS daily_admissions
  FROM admissions
  GROUP BY 
    attending_doctor_id,
    admission_date
)
SELECT 
  attending_doctor_id,
  admission_date,
  daily_admissions,
  SUM(daily_admissions) OVER (
    PARTITION BY attending_doctor_id 
    ORDER BY admission_date ASC
  ) AS running_total
FROM DailyDoctorAdmissions;
```
