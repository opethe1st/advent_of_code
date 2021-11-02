from dataclasses import dataclass

@dataclass
class Reindeer:
    name: str
    speed: int
    duration: int
    rest: int

    def __post_init__(self):
        self.rest_left = self.rest
        self.duration_left = self.duration
        self.position = 0
        self.status = 'flying'

    @classmethod
    def from_string(cls, string: str):
        match string.split():
            case [name, "can", "fly", speed, "km/s", "for", duration, "seconds,", "but", "then", "must", "rest", "for", rest, "seconds."]:
                return cls(
                    name,
                    int(speed),
                    int(duration),
                    int(rest),
                )
            case _:
                raise Exception('cant parse')


if __name__ == '__main__':
    reindeers = []
    for line in open('input.txt'):
        reindeers.append(Reindeer.from_string(line))

    for second in range(2503):
        for reindeer in reindeers:
            if reindeer.status == 'flying':
                reindeer.position += reindeer.speed
                reindeer.duration_left -= 1
                if reindeer.duration_left == 0:
                    reindeer.status = 'resting'
                    reindeer.duration_left = reindeer.duration
            elif reindeer.rest_left:
                reindeer.rest_left -= 1
                if reindeer.rest_left == 0:
                    reindeer.status = 'flying'
                    reindeer.rest_left = reindeer.rest
        # print([reindeer.position for reindeer in reindeers])
    print(max(reindeer.position for reindeer in reindeers))
