import argparse
import random
import json

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--a', default='10000')
parser.add_argument('-b', '--b', default='50')
parser.add_argument('-s', '--nonsort', action='store_false')
args = parser.parse_args()
data = {}
num1 = int(args.a)
num2 = int(args.b)

for i in range(num2):
    data[i+1] = {}
    data[i+1]["num"] = 0
    data[i+1]["ranking"] = 0
for i in range(num1):
    y = random.randint(1, num2)
    data[y]["num"] += 1
if args.nonsort is True:
    data_sorted = sorted(data.items(), reverse=True, key=lambda x: x[1]["num"])
    for i in range(num2):
        data_sorted[i][1]["ranking"] = i + 1
    with open('./data_pppc.json', 'w') as f:
        json.dump(data_sorted, f, indent=4)
else:
    with open('./data_pppc.json', 'w') as f:
        json.dump(data, f, indent=4)
