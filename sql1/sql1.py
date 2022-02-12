#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import pymysql
 
con = pymysql.connect(host='mysql-rfam-public.ebi.ac.uk',user='rfamro',password='', db='Rfam',port=4497)
 
with con:
    
    cur = con.cursor()
    cur.execute("SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end FROM full_region fr, rfamseq rf, taxonomy tx WHERE rf.ncbi_id = tx.ncbi_id AND fr.rfamseq_acc = rf.rfamseq_acc AND tx.ncbi_id = 10116  AND is_significant = 1 LIMIT 0,10")
   
   #разремил нижнюю строку для эксперимента увидит jenkins изменения в репозитории или нет
    version = cur.fetchone()
    
    #print("Database version: {}".format(version[0]))

    rows = cur.fetchall()
 
    for row in rows:
        print("{0} {1} {2} {3}".format(row[0], row[1], row[2], row[3]))
