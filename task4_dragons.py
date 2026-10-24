def maximum_power(total_heads: int) -> int:
    if not (1 <= total_heads < 100):
        raise ValueError("N должно удовлетворять 0 < N < 100")
    dp = [0] * (total_heads + 1)
    dp[0] = 1  # neutral element for starting a new partition
    for heads in range(1, total_heads + 1):
        dp[heads] = max(
            dragon_heads * dp[heads - dragon_heads]
            for dragon_heads in range(1, min(7, heads) + 1)
        )
    return dp[total_heads]


def main() -> None:
    print(maximum_power(int(input().strip())))


if __name__ == "__main__":
    main()
