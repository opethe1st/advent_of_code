import re


MASK_RE = re.compile(r"^mask = (.*)$")
MEM_RE = re.compile(r"^mem\[(\d+)\] = (\d+)$")


def ones(mask):
    value = 0
    power = 0
    for bit in mask[::-1]:
        if bit == "1":
            value += 1 << power
        power += 1
    return value


def zeros(mask):
    value = 0
    power = 0
    for bit in mask[::-1]:
        if bit != "0":
            value += 1 << power
        power += 1
    return value


def generate_address(address, mask):
    address_in_bit = bin(address)[2:]
    address_in_bit = "0" * (36 - len(address_in_bit)) + address_in_bit
    # print('a, m', address_in_bit, mask)
    address_in_bit = [
        "1" if mask_bit == "1" else "X" if mask_bit == "X" else address_bit
        for address_bit, mask_bit in zip(address_in_bit, mask)
    ]
    # print('after mask', "".join(address_in_bit))
    count = 1 << address_in_bit.count("X")
    for i in range(count):
        value = ""
        for letter in address_in_bit:
            if letter == "1":
                value += "1"
            elif letter == "0":
                value += letter
            elif letter == "X":
                value += str(i & 1)
                i >>= 1
        yield value


def apply_mask(mask: str, value: int, address: int, memory):
    for generated_address in generate_address(address, mask):
        # print(generated_address)
        memory[generated_address] = value


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
                apply_mask(mask, value, address, memory)
    return sum(memory.values())


if __name__ == "__main__":
    instructions = [line.strip() for line in open("test.txt")]
    ans = solve(instructions)
    print(ans)
