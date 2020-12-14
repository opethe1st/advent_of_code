

if __name__ == '__main__':
    earliest_time_to_depart = int(input())
    bus_ids = list(map(int, (num for num in input().split(',') if num != 'x')))
    # print(list(bus_ids))
    departure_time = earliest_time_to_depart
    found = False
    while departure_time < earliest_time_to_depart + min(bus_ids) + 1:
        for bus_id in bus_ids:
            if (departure_time % bus_id == 0):
                print(bus_id*(departure_time-earliest_time_to_depart))
                found = True
                break
        if found:
            break
        departure_time += 1
