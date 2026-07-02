# Database Definition Language (DDL)

This directory handles the foundational structure of the database.

## Contents
* **`DDL-file.sql`**: The master script containing database creation schema and table setups.

## Important Note
The tables within the SQL file are organized in a **strict, specific creation order** based on relational dependencies. Do not alter the execution sequence inside the file, as parent lookup tables must exist before child tables can reference them via foreign keys.
