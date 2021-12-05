matrix_type = list[list[int]]


def get_matrix(lines: list[str], start: int) -> tuple[matrix_type, int]:
    matrix = []
    for _ in range(5):
        matrix.append(
            list(map(int, filter(lambda x: x != "", lines[start].split(" "))))
        )
        start += 1
    return matrix, start


def get_matrices(lines: list[str], start: int) -> list[matrix_type]:
    matrices = []
    i = start
    while i < len(lines):
        matrix, i = get_matrix(lines, i)
        matrices.append(matrix)
        i += 1
    return matrices


def mark(matrix: matrix_type, num: int) -> matrix_type:
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == num:
                matrix[i][j] = "Marked"
    return matrix


def all_marked_row(matrix: matrix_type) -> bool:
    return any(set(row) == {"Marked"} for row in matrix)


def all_marked_column(matrix: matrix_type) -> bool:
    transpose = zip(*matrix)
    return all_marked_row(transpose)


def score(matrix: matrix_type, num: int) -> int:
    return (
        sum(sum(filter(lambda item: isinstance(item, int), row)) for row in matrix)
        * num
    )


def play_bingo(drawn_numbers: list, matrices: list[matrix_type]):
    winning_board_and_score: list[tuple[int, int]] = []
    winning_boards = set()
    for num in drawn_numbers:
        for i, matrix in enumerate(matrices):
            if i not in winning_boards:
                matrix = mark(matrix, num)
                if all_marked_column(matrix) or all_marked_row(matrix):
                    winning_board_and_score.append((i, score(matrix, num)))
                    winning_boards.add(i)
    return winning_board_and_score[-1][1]


if __name__ == "__main__":
    lines = [line.strip() for line in open("input.txt")]
    random_order = map(int, lines[0].split(","))
    matrices = get_matrices(lines, 2)
    print(play_bingo(drawn_numbers=random_order, matrices=matrices))
