import csv

INPUT_FILE = "sample/sample_input.csv"
OUTPUT_FILE = "sample/sample_output.csv"

def preprocess_input(input_file):
    votes, seats, parties = {}, {}, []

    with open(input_file, 'r') as file:
        reader = list(csv.reader(file)) # read the file into a list of lists
        parties = reader[0][2:] # get the parties

        for line in reader[1:]:
            if len(line[2:]) != len(parties): 
                print("Please check the input file. The number of parties is not consistent for all constituencies.")
                exit()

            votes[line[0]] = [int(i) for i in line[2:]]
            seats[line[0]] = int(line[1])

    return votes, seats, parties

def calculate_seats(votes, seats, parties):
    results = []
    total = len(parties) * [0]

    for constituency in votes.keys():
        if sum(votes[constituency]) == 0:
            print("No votes were found for " + constituency)
            continue

        rates = len(parties) * [1]

        for i in range(seats[constituency]):
            tmp = [(votes[constituency][i] / rates[i]) for i in range(len(parties))]
            rates[tmp.index(max(tmp))] += 1

        data_dict = {"constituency": constituency}
        for i in range(len(parties)):
            data_dict[parties[i]] = rates[i] - 1
            total[i] += (rates[i] - 1)
        results.append(data_dict)

        print(constituency + " seats have been calculated successfully.")
        print([rates[i] - 1 for i in range(len(rates))])

    total_seats = {"constituency": "total"}
    for i in range(len(parties)):
        total_seats[parties[i]] = total[i]
    results.append(total_seats)

    return results

def main():
    input_file = INPUT_FILE
    output_file = OUTPUT_FILE

    votes, seats, parties = preprocess_input(input_file)
    seats = calculate_seats(votes, seats, parties)
    
    with open(output_file, "w", newline="") as file:
        field_names = ["constituency"] + parties
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for constituency in seats:
            writer.writerow(constituency)

if __name__ == "__main__":
    main()