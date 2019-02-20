register 'pig.py' using org.apache.pig.scripting.jython.JythonScriptEngine as myfuncs;

admits = LOAD 'hospital_data.csv' USING PigStorage(',')
         AS (facility:CHARARRAY, lengthofstay: INT, totalcharges: FLOAT);

func_ex = FOREACH admits
          GENERATE myfuncs.cvtToEuros(totalcharges),
                   myfuncs.concat(facility);
                   -- add call to to_hours here

dump func_ex;
describe func_ex;
