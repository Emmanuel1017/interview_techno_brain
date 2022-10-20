import csv
import statistics


def read_cvs():


    ips = []

    with open('ip.csv', 'r') as csv_rf:

        cvs_reader = csv.DictReader(csv_rf)

        for row in  cvs_reader:
            for col in row:
                if(col[2]):
                 ip=col
                 #print(ip)
                 ips.append(ip)

    print(statistics.mode(ips))

read_cvs()
