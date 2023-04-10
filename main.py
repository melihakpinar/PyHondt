import csv

def preprocess_input(input_file):
    votes = {}
    seats = {}
    parties = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file)) # read the file into a list of lists
        header = reader[0] # get the header
        parties = header[2:] # get the parties
        for line in reader[1:]:
            if len(line[2:]) != len(parties): 
                print("Please check the input file. The number of parties is not consistent for all constituencies.")
                exit()
            votes[line[0]] = [int(i) for i in line[2:]]
            seats[line[0]] = int(line[1])
    return votes, seats, parties

def main():
    input_file = "sample/sample_input.csv"
    output_file = "sample/sample_output.csv"

    votes, seats, parties = preprocess_input(input_file)
    result = []
    total = len(parties) * [0]

    for key in votes.keys():
        if sum(votes[key]) == 0:
            print("No votes were found for " + key)
            continue
        result.append({})
        result[len(result) - 1]['constituency'] = key
        rates = len(parties) * [1]
        for i in range(seats[key]):
            tmp = [(votes[key][i] / rates[i]) for i in range(len(parties))]
            rates[tmp.index(max(tmp))] += 1
        for i in range(len(parties)):
            result[len(result) - 1][parties[i]] = rates[i] - 1
            total[i] += (rates[i] - 1)
        print(key + " seats have been calculated successfully.")
        print([rates[i] - 1 for i in range(len(rates))])

    result.append({})
    result[len(result)-1]['constituency'] = "total"
    for i in range(len(parties)):
        result[len(result) - 1][parties[i]] = total[i]

    with open(output_file, 'w', newline='') as file:
        field_names = ['constituency'] + parties
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for result in result:
            writer.writerow(result)

if __name__ == "__main__":
    main()