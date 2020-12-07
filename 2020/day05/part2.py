
def compute_seat_id(raw_data):
    row_data, column_data = raw_data[:7], raw_data[7:]
    return (compute_row(row_data=row_data) << 3) + compute_column(column_data=column_data)


def compute_row(row_data):
    row = 0
    for letter in row_data:
        row <<= 1
        if letter == 'B':
            row |= 1
    return row


def compute_column(column_data):
    column = 0
    for letter in column_data:
        column <<= 1
        if letter == 'R':
            column |= 1
    return column


if __name__ == '__main__':
    seat_ids = set([compute_seat_id(data.strip()) for data in open('input.txt')])
    for possible_seat_id in range(min(seat_ids), max(seat_ids) + 1):
        if possible_seat_id not in seat_ids:
            print(possible_seat_id)
