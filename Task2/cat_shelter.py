import sys

def cat_shelter(filename):
    try:
        with open(filename, 'r') as file:
            read_file = file.readlines()

        our_cats = 0
        other_cats = 0
        total_time_in_house = 0
        longest_visit = 0
        shortest_visit = sys.maxsize

        for read in read_file:
            if read == "END":
                break

            parts = read.split(',')
            cat_name = parts[0]
            entry_time = int(parts[1])
            exit_time = int(parts[2])


            duration = exit_time - entry_time

            if cat_name == "OURS":
                our_cats += 1
                total_time_in_house += duration

                if duration > longest_visit:
                    longest_visit = duration

                if duration < shortest_visit:
                    shortest_visit = duration
            else:
                other_cats += 1

        average_visit_length = total_time_in_house / our_cats 

        # Converting total time to hours and minutes
        total_hours = total_time_in_house // 60
        total_minutes = total_time_in_house % 60

        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {our_cats}")
        print(f"Other Cats: {other_cats}\n")
        print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
        print(f"Average Visit Length: {int(average_visit_length)} Minutes")
        print(f"Longest Visit: {longest_visit} Minutes")
        print(f"Shortest Visit: {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{filename}"!')

if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    cat_shelter(sys.argv[1])

