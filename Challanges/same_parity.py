"""Реализуйте функцию same_parity_filter(), которая принимает на вход список и возвращает новый список, состоящий из элементов, у которых такая же чётность, как и у первого элемента исходного списка."""

# BEGIN
def is_even(number):
    return number % 2 == 0


def same_parity_filter(numbers):
    if not numbers:
        return []

    first_number_parity = is_even(numbers[0])

    filtered_numbers = filter(
        lambda number: is_even(number) == first_number_parity,
        numbers,
    )

    return list(filtered_numbers)
# END

# BEGIN (write your solution here)
def same_parity_filter_2(eq_list):
    """Get the same parity list."""
    return [x for x in eq_list if x % 2 == eq_list[0] % 2]

# END