# Background

SQL sublanguage: DDL (Data Definition Language)

A VIEW in SQL is a virtual table created from a predefined SQL statement.

CREATE VIEW view_name AS sql_statement;

For example:

CREATE VIEW stevesview AS SELECT * FROM site_user WHERE firstname = 'Steve';

## Problem 1

Assume the following table already exists.

| id | firstname | lastname | age |
|----|-----------|----------|-----|
| 1 | Steve | Garcia | 23 |
| 2 | Alexa | Smith | 40 |
| 3 | Steve | Jones | 29 |
| 4 | Brandon | Smith | 50 |
| 5 | Adam | Jones | 61 |

Create a view called `firstname_lastname` in `problem1.sql` from the `site_user` table that only has the
firstname and lastname columns. This view should NOT have the id and age columns.
