import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    errors = []
    negatives = []
    delimiter = ",|\n"
    body = numbers

    if numbers.startswith("//"):
        match = re.match(r"//(.+)\n", numbers)
        if match:
            delimiter = re.escape(match.group(1))
            body = numbers[match.end():]

    tokens = re.split(delimiter, body)
    total = 0
    position = 0

    for token in tokens:
        if token == "":
            errors.append(f"Separator at position {position} is invalid")
        else:
            try:
                num = int(token)
                if num < 0:
                    negatives.append(num)
                elif num <= 1000:
                    total += num
            except ValueError:
                errors.append(f"Invalid number at position {position}")
        position += len(token) + 1

    if negatives:
        errors.append(f"Negative number(s) not allowed: {', '.join(map(str, negatives))}")

    if errors:
        raise ValueError("\n".join(errors))

    return total