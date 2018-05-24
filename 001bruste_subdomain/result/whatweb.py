import os, subprocess
import csv

global result_path
result_path = './result/'

if __name__ == "__main__":
    dns = 'yunjiweidian.com'
    csv_fp = csv.reader(open(result_path+dns+'.csv')) 
    for row in csv_fp:
        try:
            cmd = 'whatweb '+ row[0]
            res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            print("*****************"+row[0]+"**************")
            out = res.stdout.readlines()
            for line in out:
                print(line)
        except:
            print("##################"+row[0]+"error!##############")
            pass

