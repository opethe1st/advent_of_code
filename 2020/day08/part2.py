'''
What is the order in which instructions are currently visted?
instead of trying to repeat the instruction we are going to repeat,
change it to be a jump to the bottom if bottom is a
positive jump, acc or nop
if bottom is a negative jump, then that is what must be
changed to a nop.
'''

def instructions_terminate(instructions):
    run_instructions = set()
    program_counter = 0
    accummulator = 0
    while True:
        if program_counter in run_instructions:
            return False, accummulator
        if len(instructions) == program_counter:
            return True, accummulator

        run_instructions.add(program_counter)

        if instructions[program_counter][0] == 'nop':
            program_counter += 1
        elif instructions[program_counter][0] == 'acc':
            accummulator += int(instructions[program_counter][1])
            program_counter += 1
        elif instructions[program_counter][0] == 'jmp':
            program_counter += int(instructions[program_counter][1])


if __name__ == '__main__':
    instructions = [line.strip().split() for line in open('input.txt')]

    for i, instruction in enumerate(instructions):
        if instructions[i][0] == 'nop':
            instructions[i] = ['jmp', instruction[1]]
        elif instructions[i][0] == 'jmp':
            instructions[i] = ['nop', instruction[1]]

        terminates, value = instructions_terminate(instructions)
        if terminates:
            print(value)
            # break

        if instructions[i][0] == 'nop':
            instructions[i] = ['jmp', instruction[1]]
        elif instructions[i][0] == 'jmp':
            instructions[i] = ['nop', instruction[1]]
