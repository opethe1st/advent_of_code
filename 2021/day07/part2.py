
if __name__ == '__main__':
    crab_positions = list(map(int, input().split(',')))
    min_position, max_position = min(crab_positions), max(crab_positions)
    min_fuel = float('inf')
    for i in range(min_position, max_position+1):
        min_fuel = min(
            min_fuel,
            sum((abs(x-i)*(abs(x-i)+1)//2) for x in crab_positions)
        )
    print(min_fuel)
