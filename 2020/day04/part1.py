from dataclasses import dataclass

@dataclass
class Passport:
    # didn't use the descriptive names because I wanted to convert to the object easily. :)
    iyr: str = None     # (Issue Year)
    byr: str = None     # (Birth Year)
    eyr: str = None     # (Expiration Year)
    hgt: str = None     # (Height)
    hcl: str = None     # (Hair Color)
    ecl: str = None     # (Eye Color)
    pid: str = None     # (Passport ID)
    cid: str = None  # (Country ID)


def passport_from_string(string):
    kwargs = dict([field.split(':') for field in string.strip().split(' ')])
    return Passport(**kwargs)


def is_valid(passport: Passport):
    return (
        passport.iyr is not None and
        passport.byr is not None and
        passport.eyr is not None and
        passport.hgt is not None and
        passport.hcl is not None and
        passport.ecl is not None and
        passport.pid is not None
    )


if __name__ == '__main__':
    with open('input.txt') as file:
        passports = [passport_from_string(passport.replace('\n', ' ')) for passport in file.read().split('\n\n')]
    no_valid = 0
    for passport in passports:
        no_valid += int(is_valid(passport=passport))
    print(no_valid)
