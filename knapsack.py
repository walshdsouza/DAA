from fractions import Fraction


def greedyKnapsack(m, items):
    u = m
    total = 0
    included = {}

    for idx, p, w in items:
        if w > u:
            frac = u / w
            total += p * frac
            included[idx] = w * frac
            break

        total += p
        u -= w
        included[idx] = w

    return total, included


def format_ratio(r):
    r = Fraction(r)
    return str(r.numerator) if r.denominator == 1 else f"{r.numerator}/{r.denominator}"


def main():
    n = int(input("Enter n: "))

    profits = [Fraction(i) for i in input("Enter profits: ").split()]
    # profits = [Fraction(x) for x in [387, 281, 357, 456, 570, 768, 408, 26, 254, 62, 464]]
    weights = [Fraction(i) for i in input("Enter weights: ").split()]
    # weights = [Fraction(x) for x in [23, 84, 69, 47, 95, 85, 61, 96, 75, 51, 94]]

    m = float(input("Enter knapsack capacity: "))

    elements = list(zip(profits[:n], weights[:n]))

    indexed_elements = list(enumerate(elements, start=1))
    original_weight = {idx: w for idx, (p, w) in indexed_elements}

    scaled_indexed = [
        (idx, (p / (idx + 1), w / (idx + 1))) for idx, (p, w) in indexed_elements
    ]

    cases = [
        ("1 / i Ratio", scaled_indexed),
        ("Maximum Profits", sorted(indexed_elements, key=lambda ie: ie[1][0], reverse=True)),
        ("Minimum Weights", sorted(indexed_elements, key=lambda ie: ie[1][1])),
        (
            "Maximum profit/weight",
            sorted(indexed_elements, key=lambda ie: ie[1][0] / ie[1][1], reverse=True),
        ),
    ]

    print("\nelements :", [(f"{float(p):g}", f"{float(w):g}") for p, w in elements], "(profit, weight)")
    print("capacity :", f"{float(m):g}\n")

    rows = []
    for label, case_items in cases:
        items_for_algo = [(idx, p, w) for idx, (p, w) in case_items]
        profit, included = greedyKnapsack(m, items_for_algo)

        ratios = [
            included.get(idx, Fraction(0)) / original_weight[idx] for idx in range(1, n + 1)
        ]
        ratio_str = "[" + ", ".join(format_ratio(r) for r in ratios) + "]"
        rows.append((label, float(profit), ratio_str))

    ratio_col_width = max(24, max(len(ratio_str) for _, _, ratio_str in rows) + 2)

    header = (
        f"| {'case':<4} | {'ratios of elements':<24} | {'maximum profit':>14} "
        f"| {'weight ratios (original order)':<{ratio_col_width}} |"
    )
    line = (
        "|" + "-" * 6 + "|" + "-" * 26 + "|" + "-" * 16 + "|" + "-" * (ratio_col_width + 2) + "|"
    )

    print(line)
    print(header)
    print(line)

    for k, (label, profit, ratio_str) in enumerate(rows, start=1):
        print(
            f"| {k:<4} | {label:<24} | {profit:>14.2f} "
            f"| {ratio_str:<{ratio_col_width}} |"
        )

    print(line)


if __name__ == "__main__":
    main()