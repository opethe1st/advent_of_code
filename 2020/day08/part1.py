

if __name__ == '__main__':
    instructions = [line.strip().split() for line in open('input.txt')]
    run_instructions = set()
    program_counter = 0
    accummulator = 0
    while True:
        if program_counter in run_instructions:
            print(accummulator)
            break
        run_instructions.add(program_counter)
        if instructions[program_counter][0] == 'nop':
            program_counter += 1
        elif instructions[program_counter][0] == 'acc':
            accummulator += int(instructions[program_counter][1])
            program_counter += 1
        elif instructions[program_counter][0] == 'jmp':
            program_counter += int(instructions[program_counter][1])
