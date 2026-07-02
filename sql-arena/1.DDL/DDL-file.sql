CREATE DATABASE hospital_db; 
USE hospital_db;

-- 1. Create province_names table first (It has no foreign keys pointing elsewhere)
CREATE TABLE province_names (
    province_id CHAR(2),
    province_name TEXT,
    PRIMARY KEY (province_id)
);

-- 2. Create doctors table (It has no foreign keys pointing elsewhere)
CREATE TABLE doctors (
    doctor_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    speciality TEXT,
    PRIMARY KEY (doctor_id)
);

-- 3. Create patients table (Links to province_names via province_id)
CREATE TABLE patients (
    patient_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    gender VARCHAR(1),
    birth_date DATE,
    city TEXT,
    allergies TEXT,
    height INTEGER,
    weight INTEGER,
    province_id CHAR(2),
    PRIMARY KEY (patient_id),
    FOREIGN KEY (province_id) REFERENCES province_names(province_id)
);

-- 4. Create admissions table last (Links to both patients and doctors)
CREATE TABLE admissions (
    patient_id INTEGER,
    admission_date DATE,
    discharge_date DATE,
    diagnosis TEXT,
    attending_doctor_id INTEGER,
    PRIMARY KEY (patient_id, admission_date), -- Composite key since a patient can have multiple admissions on different dates
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (attending_doctor_id) REFERENCES doctors(doctor_id)
);