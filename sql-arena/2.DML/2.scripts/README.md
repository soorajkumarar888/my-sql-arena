# ETL Transformation Scripts

This directory acts as our active code pipeline workbench.

## Functional Goal
The `.py` files inside are customized scripts built to read their matching raw targets in `1.source/`. They sanitize inputs (escaping dangerous single quotes, filtering empty strings into true database `NULL` markers), map index arrays, and output perfectly structured SQL data rows.
