import os
import csv

global subdomain3_path
subdomain3_path = "./subdomain3/"
global subDomainsBrute_path
subDomainsBrute_path = './subDomainsBrute/'
global result_path
result_path = './result/'

if __name__ == "__main__":
    dns = "yunjiweidian.com"
    subdomain = dict()
    csf = csv.reader(open(subdomain3_path+dns+'/deal_'+dns+'.csv', 'r'))
    count = 0
    subdomain3 = dict()
    for  row in csf:
        #print(row)
        if row[0] == "domain":
            continue
        count += 1
        subdomain3[row[0]] = row[2].replace("'", "").replace("[", "").replace("]", "")
    subdomain3ip = dict()
    count2 = 0
    csf2 = csv.reader(open(subdomain3_path+dns+"/"+dns+".csv", "r"))
    for row in csf2:
        if row[0] == 'IP':
            continue
        count2 += 1
        subdomain3ip[row[0]] = row[2]
    csf3 = open(subDomainsBrute_path+dns+'.txt')
    count3 = 0
    subDomainsBrute = dict()
    for rows in csf3:
        rows = rows.strip().replace('\t', '')
        row = rows.split(" ")
        row = filter(None, row)
        #print(row)
        subDomainsBrute[row[0]] = row[1]

    res = dict()
    res.update(subDomainsBrute)
    res.update(subdomain3)
    for  sb in  res.keys():
        subdomain[sb] = res[sb]

    print(len(subdomain))
    for key in subdomain:
        print(key + "   "+ subdomain[key])

    domain_csv = csv.writer(open(result_path+dns+".csv", "w"))
    for key in subdomain.keys():
        domain_csv.writerow([key, subdomain[key]])
    ips_csv = csv.writer(open(result_path+dns+"_ips.csv", "w"))
    for key in subdomain3ip.keys():
        ips_csv.writerow([key, subdomain3ip[key]])



