


def negative_between_extremes(values: list[int]) -> int:
    if not values:
        raise ValueError("Массив не должен быть пустым")
    max_pos = values.index(max(values))
    min_pos = values.index(min(values))
    left, right = sorted((max_pos, min_pos))
    return sum(x for x in values[left + 1:right] if x < 0)


def main() -> None:
    n = int(input().strip())
    if n <= 0:
        raise ValueError("N должно быть положительным")
    values = list(map(int, input().split()))
    if len(values) != n:
        raise ValueError(f"Ожидалось {n} элементов, получено {len(values)}")
    print(negative_between_extremes(values))


if __name__ == "__main__":
    main()
