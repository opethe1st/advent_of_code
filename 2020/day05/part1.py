
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
    # print(compute_seat_id('BBFFBBFRLL'))
    highest_seat_id = 0
    for data in open('input.txt'):
        highest_seat_id = max(highest_seat_id, compute_seat_id(data.strip()))
    print(highest_seat_id)
