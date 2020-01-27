import re
from collections import Counter

#test

def reader(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.readlines()
        a = [x.split() for x in log]  # построчно загоняю в лист
        # print (a)
        ips_list = [i[1] for i in a]  # записываю в ips_list только перв. столбец IP
        # print (ips_list)
        new_list = []
        for i in ips_list:
            ipf = re.findall(regexp, i)
            if ipf in new_list:
                continue
            elif len(ipf) > 0:
                new_list.append(ipf[0])
        # print (new_list)
        count = Counter (new_list)
        # print (count)
        for i in count:
        	print (i, '\t', count[i])




if __name__ == '__main__':
    reader('69mb3.txt')
