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
