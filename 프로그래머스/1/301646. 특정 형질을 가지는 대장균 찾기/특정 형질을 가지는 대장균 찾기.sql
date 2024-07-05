select count(*) as COUNT
  from ECOLI_DATA
 where GENOTYPE%8 in(1,4,5);