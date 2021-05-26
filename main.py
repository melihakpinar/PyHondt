import csv

votes = {}
seats = {}
parties = []
ans = []
partyCount = 0
header = True

input_file = 'input.csv'
output_file = 'output.csv'

###

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    for il in reader:    
        if header:
            parties = il[2:]
            partyCount = len(il[2:])
            header = False
            continue    
        votes[il[0]] = [int(i) for i in il[2:2 + partyCount]]
        seats[il[0]] = int(il[1])

###

total = partyCount * [0]

for key in votes.keys():
    if sum(votes[key]) == 0:
        print("No votes were found for " + key)
        continue
    ans.append({})
    ans[len(ans)-1]['constituency'] = key
    rates = partyCount * [1]
    for i in range(seats[key]):
        tmp = [(votes[key][i] / rates[i]) for i in range(partyCount)]
        rates[tmp.index(max(tmp))] += 1
    for i in range(partyCount):
        ans[len(ans)-1][parties[i]] = rates[i]-1
        total[i] += (rates[i]-1)
    print("\n" + key + " seats have been calculated successfully.")
    print([rates[i]-1 for i in range(len(rates))])

ans.append({})
ans[len(ans)-1]['constituency'] = "total"
for i in range(partyCount):
    ans[len(ans)-1][parties[i]] = total[i]

###

with open(output_file, 'w', newline='') as file:
    fieldnames = ['constituency'] + parties
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for result in ans:
        writer.writerow(result)