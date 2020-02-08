row_values = "ABCDEFGHI"
column_values = "123456789"

def combined(row, columns):
    return [each_letter + every_number for each_letter in row for every_number in columns]

boxes = combined(row_values, column_values)
row_units = [combined(each_letter, column_values) for each_letter in row_values]
column_units = [combined(row_values, every_number) for every_number in column_values]
square_units = [combined(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)

def grid_values(grid):
    assert len(grid) == 81
    numbers = "123456789"
    values = []
    for string in grid:
        if string == ".":
            values.append(numbers)
        else:
            values.append(string)

    return dict(zip(boxes, values))

def display(values):

    width = 1 + max(len(values[s]) for s in boxes)
    line = "+".join(["-" * (width * 3)] * 3)
    for r in row_values:
        print("".join(values[r + c].center(width) + ("|" if c in "36" else "") for c in column_values))
        if r in "CF": print(line)
    return
