from collections import OrderedDict
import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name, 'r') as rfile:
        with open(output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(rfile)
            writer = csv.writer(wfile)
            dic = OrderedDict()
            for password in range(1000,10000):
                temp = str(password)
                password = str(password).encode('utf-8')
                h = hashlib.sha256(password)
                h = h.hexdigest()
                dic[h] = temp
            list1 = []
            for row in reader:
                username = row.pop(0)
                password = dic[row[0]]
                list1 = [username ,password]
                writer.writerow(list1)
