
-- add table hospital
DROP TABLE IF EXISTS default.hospital;

CREATE TABLE default.hospital (
  facility STRING,
  age STRING,
  gender STRING,
  lengthofstay INT,
  admissiontype STRING,
  diagnosiscode INT,
  severity INT,
  paymentsource STRING,
  totalcharges DECIMAL(10, 2)
)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ',';

LOAD DATA INPATH 'hospital-data.csv' OVERWRITE INTO TABLE default.hospital;

-- add table diagcodemap
DROP TABLE IF EXISTS default.diagcodemap;

CREATE TABLE default.diagcodemap (
  code INT,
  diagnosis STRING
)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ', ';

LOAD DATA INPATH 'diagcodemap.csv' OVERWRITE INTO TABLE default.diagcodemap;
