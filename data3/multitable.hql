from (select severity, diagnosis
      from hospital join diagcodemap
      on hospital.diagnosiscode = diagcodemap.code) a
insert overwrite table diagnoses_by_severity
  select distinct severity, diagnosis
insert overwrite table diagnosis_count
  select severity, count(*)
  group by severity;
