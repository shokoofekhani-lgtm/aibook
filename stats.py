
# just a place holder
def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_min(numbers):
    return min(numbers)


def calculate_max(numbers):
    return max(numbers)


def main():
    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Minimum:", calculate_min(numbers))
    print("Maximum:", calculate_max(numbers))


if __name__ == "__main__":
    main()
