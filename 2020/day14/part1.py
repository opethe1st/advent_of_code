import re

MASK_RE = re.compile(r'^mask = (.*)$')
MEM_RE = re.compile(r'^mem\[(\d+)\] = (\d+)$')


def ones(mask):
    value = 0
    power = 0
    for bit in mask[::-1]:
        if bit == '1':
            value += (1 << power)
        power += 1
    return value


def zeros(mask):
    value = 0
    power = 0
    for bit in mask[::-1]:
        if bit != '0':
            value += (1 << power)
        power += 1
    return value


def apply_mask(mask, value):
    value |= ones(mask)
    value &= zeros(mask)
    return value


def solve(instructions):
    memory = dict()
    mask = None
    for instruction in instructions:
        match = MASK_RE.match(instruction)
        if match:
            mask = match.group(1)
        else:
            match = MEM_RE.match(instruction)
            if match:
                address = int(match.group(1))
                value = int(match.group(2))
                memory[address] = apply_mask(mask, value)
    return sum(memory.values())


if __name__ == '__main__':
    instructions = [line.strip() for line in open('input.txt')]
    ans = solve(instructions)
    print(ans)
