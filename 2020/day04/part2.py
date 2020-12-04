from dataclasses import dataclass
import re


@dataclass
class Passport:
    iyr: str = None     # (Issue Year)
    byr: str = None     # (Birth Year)
    eyr: str = None     # (Expiration Year)
    hgt: str = None     # (Height)
    hcl: str = None     # (Hair Color)
    ecl: str = None     # (Eye Color)
    pid: str = None     # (Passport ID)
    cid: str = None     # (Country ID)


def passport_from_string(string):
    kwargs = dict([field.split(':') for field in string.strip().split(' ')])
    return Passport(**kwargs)


def is_valid(passport: Passport):
    return (
        _is_valid_iyr(passport.iyr) and
        _is_valid_byr(passport.byr) and
        _is_valid_eyr(passport.eyr) and
        _is_valid_hgt(passport.hgt) and
        _is_valid_hcl(passport.hcl) and
        _is_valid_ecl(passport.ecl) and
        _is_valid_pid(passport.pid) and
        _is_valid_cid(passport.cid)
    )


def _is_valid_iyr(year):
    if year is None:
        return False
    return len(year) == 4 and 2010 <= int(year) <= 2020


def _is_valid_byr(year):
    if year is None:
        return False
    return len(year) == 4 and 1920 <= int(year) <= 2002


def _is_valid_eyr(year):
    if year is None:
        return False
    # could have a year validator but overkill
    return len(year) == 4 and 2020 <= int(year) <= 2030


def _is_valid_hgt(height):
    if height is None:
        return False
    if not (height.endswith('cm') or height.endswith('in')):
        return False
    unit = height[-2:]
    value = height[:-2]
    # if not a number then it is false
    match = re.match(pattern=r'^\d+$', string=value)
    if not match:
        return False
    if unit == 'cm':
        return 150 <= int(value) <= 193
    elif unit == 'in':
        return 59 <= int(value) <= 76

    else:
        raise Exception('unknown unit')

def _is_valid_hcl(hcl):
    if hcl is None:
        return False
    return bool(re.match(pattern=r'^#[0-9a-f]{6}$', string=hcl))

def _is_valid_ecl(ecl):
    if ecl is None:
        return False
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def _is_valid_pid(pid):
    if pid is None:
        return False
    return bool(re.match(pattern=r'^[0-9]{9}$', string=pid))

def _is_valid_cid(cid):
    return True

if __name__ == '__main__':
    with open('input.txt') as file:
        passports = [passport_from_string(passport.replace('\n', ' ')) for passport in file.read().split('\n\n')]
    no_valid = 0
    for passport in passports:
        no_valid += int(is_valid(passport=passport))
    print(no_valid)
