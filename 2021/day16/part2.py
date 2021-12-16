from functools import reduce
import operator
from typing import Optional
from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type_id: int
    subpackets: list["Packet"]
    value: Optional[int] = None

    @classmethod
    def parse(cls, stream):
        packet, _ = cls._parse(stream, 0)
        return packet

    @classmethod
    def _parse(cls, stream: str, cursor: int = 0):
        version, cursor = cls._read_version(stream, cursor=cursor)
        type_id, cursor = cls._read_type_id(stream, cursor)
        if type_id == 4:
            number, cursor = cls._read_number(stream, cursor)
            return Packet(version, type_id, subpackets=[], value=number), cursor
        else:
            length_type_id, cursor = cls._read_length_type_id(stream, cursor)
            if length_type_id == "0":
                total_length, cursor = cls._read_total_length_in_bits(stream, cursor)
                subpackets, cursor = cls._read_subpackets_with_total_length_in_bits(
                    stream, cursor, total_length_in_bits=total_length
                )
            else:
                total_number_of_packets, cursor = cls._read_total_number_of_subpackets(
                    stream, cursor
                )
                subpackets, cursor = cls._read_subpacket_with_number_of_subpackets(
                    stream, cursor, total_number_of_packets
                )
            return Packet(version, type_id, subpackets), cursor

    def compute_value(self):
        if self.value:
            return self.value

        match self.type_id:
            case 0:
                self.value = sum(p.compute_value() for p in self.subpackets)
            case 1:
                self.value = reduce(
                    operator.mul, (p.compute_value() for p in self.subpackets)
                )
            case 2:
                self.value = min(p.compute_value() for p in self.subpackets)
            case 3:
                self.value = max(p.compute_value() for p in self.subpackets)
            case 4:
                pass
            case 5:
                assert len(self.subpackets) == 2
                self.value = int(
                    self.subpackets[0].compute_value()
                    > self.subpackets[1].compute_value()
                )
            case 6:
                assert len(self.subpackets) == 2
                self.value = int(
                    self.subpackets[0].compute_value()
                    < self.subpackets[1].compute_value()
                )
            case 7:
                assert len(self.subpackets) == 2
                self.value = int(
                    self.subpackets[0].compute_value()
                    == self.subpackets[1].compute_value()
                )
        return self.value

    @staticmethod
    def _read_version(stream: str, cursor: int):
        return int(stream[cursor : cursor + 3], 2), cursor + 3

    @staticmethod
    def _read_type_id(stream: str, cursor: int):
        return int(stream[cursor : cursor + 3], 2), cursor + 3

    @staticmethod
    def _read_number(stream: str, cursor: int):
        num = ""
        while stream[cursor] == "1":
            num += stream[cursor + 1 : cursor + 5]
            cursor += 5
        num += stream[cursor + 1 : cursor + 5]
        cursor += 5
        return int(num, 2), cursor

    @staticmethod
    def _read_length_type_id(stream: str, cursor: int):
        return stream[cursor], cursor + 1

    @staticmethod
    def _read_total_length_in_bits(stream: str, cursor: int):
        return int(stream[cursor : cursor + 15], 2), cursor + 15

    @staticmethod
    def _read_total_number_of_subpackets(stream: str, cursor: int):
        return int(stream[cursor : cursor + 11], 2), cursor + 11

    @classmethod
    def _read_subpackets_with_total_length_in_bits(
        cls, stream: str, cursor: int, total_length_in_bits: int
    ):
        subpackets = []
        start = cursor
        while cursor < (start + total_length_in_bits) < len(stream):
            subpacket, cursor = cls._parse(stream, cursor)
            # assert (start + total_length_in_bits) < len(stream)
            subpackets.append(subpacket)
            total_length_in_bits -= 1
        return subpackets, cursor

    @classmethod
    def _read_subpacket_with_number_of_subpackets(
        cls, stream: str, cursor: int, num_of_subpackets: int
    ):
        subpackets = []
        while num_of_subpackets:
            subpacket, cursor = cls._parse(stream, cursor)
            subpackets.append(subpacket)
            num_of_subpackets -= 1
        return subpackets, cursor


hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def convert_to_binary(hex_digits):
    return "".join(hex_to_binary[digit] for digit in hex_digits)


if __name__ == "__main__":
    with open("input.txt") as file:
        message = file.read().strip()

    binary = convert_to_binary(message)
    packet = Packet.parse(binary)
    print(packet.compute_value())
