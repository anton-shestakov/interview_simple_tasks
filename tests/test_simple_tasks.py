from simple_tasks.functions import count_divisible, count_letters_digits, sort_persons


def test_count_divisible():
    assert count_divisible(1, 10, 2) == 5


def test_count_letters_digits():
    assert count_letters_digits("Hello world! 123!") == {"letters": 10, "digits": 3}


def test_sort_persons():
    input_list = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
    ]

    output_list = [
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("Tom", "19", "167", "54"),
    ]

    assert sort_persons(input_list) == output_list
