use default;

ADD FILE /home/.../normal.sh;

SELECT TRANSFORM(*) USING 'normal.sh'
AS (facility string, age string, gender string,
    lengthofstay int, admissiontype int,
    diagnosiscode int, severity int,
    paymentsource string, perday decimal(10,2))
FROM hospital;
