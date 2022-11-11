import collections
import csv
import glob

ip_counter_all = collections.Counter()

for filename in glob.glob('ip*.csv'):
    ip_counter = collections.Counter()

    with open(filename) as input_file:
        csv_input = csv.reader(input_file)
        header = next(csv_input)

        for row in csv_input:
            ip_counter[row[2]] += 1

    ip_counter_all.update(ip_counter)

    print('\nSource IPs most common in: {}'.format(filename))

    for ip_addr, count in ip_counter.most_common():
        print("  {}  {}".format(ip_addr, count))

print('\nOverall IPs most common:')

for ip_addr, count in ip_counter_all.most_common():
    print("  {}  {}".format(ip_addr, count))
