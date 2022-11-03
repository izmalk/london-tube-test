# london-tube-test app

## About

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

The program has two main functions:

1. To find lines (one or many) that contain chosen station.
2. To find stations on the chosen line (**not implemented yet**).

So far only manual input of station and line names is supported.

This is a test project intended to explore basic SQL operations.

Test data provided in the `train-network.json` file. It includes some London subway 
stations and lines.

## Table of contents

- [About](#About)
- [Prerequisites](#Prerequisites)
- [Usage](#Usage)

## Prerequisites

[(Back to top)](#table-of-contents)

To work with the program you need the following:

1. Python interpreter (v. 3.7+).
2. `mysql.connector for python` module.
3. MySQL (v. 8.0.30+).

## Preparations

[(Back to top)](#table-of-contents)

### MySQL settings

Make sure to set up your MySQL with the following parameters or adjust the sourcecode 
accordingly:

- address: `localhost`
- port: *default* or 3306
- username: `root`
- password: *(empty)*
- database name: `tube`

The tube database shall include the following tables and columns:

- stations: ID(varchar255), Name(varchar255)
- line: line_id(int), ID(varchar255), name(varchar255)
- joins: station_id(varchar255), line(varchar255)

To create this tables in MySQL database you can use the following SQL commands:

1. `CREATE TABLE stations (
    ID varchar(255) NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL)`

2. `CREATE TABLE line (
      line_id int(11) NOT NULL PRIMARY KEY Auto_increment,
    ID varchar(255) NOT NULL,
    name varchar(255) NOT NULL)`

3. `CREATE TABLE joins (
    station_id varchar(255) NOT NULL,
    line varchar(255) NOT NULL)`

### Uploading test data

To load the data from the `train-network.json` file into the MySQL database you can use the 
`init.py` file.

There are three commented sections of a code in the `init.py` file with the following titles:

- Uploading stations
- Uploading lines
- Uploading connections (joins table)

Uncomment the first one by deleting the multiple double quotes `"""` before and after the 
first commented. Then run the script `init.py` once. No error messages shall be present in the output.

You can check now the `stations` table in the `tube` database of the MySQL. It shall have some records now.

Don't forget to comment the first section back again. And then repeat the process for the second and third commented sections.

After launching every of the three sections exactly once you will have three populated tables in tube database:

## Usage

[(Back to top)](#table-of-contents)

Launch the `main.py` script file. The CLI will have instructions on how to proceed.

**WARNING**: Make sure to type in station or line name correctly when prompted. Any typo can result in failing to find any results.
