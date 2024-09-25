import requests

# task 1
def greet():
    return "Hello, DevEdu!"

# test task 1
def test_greet(capsys):
    # Capture output
    greet()
    captured = capsys.readouterr()

    # Verify that the output is as expected
    assert captured.out == ""
    assert greet() == "Hello, DevEdu!"

# task 2
def integer_example():
    return 42  # Integer

def float_example():
    return 3.14159  # Floating-point number

def string_example():
    return "Hello, DevEdu!"  # String

def boolean_example():
    return True  # Boolean

# test task 2
def test_integer_example():
    assert isinstance(integer_example(), int)
    assert integer_example() == 42

def test_float_example():
    assert isinstance(float_example(), float)
    assert float_example() == 3.14159

def test_string_example():
    assert isinstance(string_example(), str)
    assert string_example() == "Hello, DevEdu!"

def test_boolean_example():
    assert isinstance(boolean_example(), bool)
    assert boolean_example() == True


# task 3
def check_number(num):
    """Check if the number is positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def first_n_primes(n):
    """Return a list of the first n prime numbers."""
    primes = []
    num = 2  # Start checking for prime from 2
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_of_numbers():
    """Return the sum of all numbers from 1 to 100."""
    total = 0
    for num in range(1, 101):
        total += num
    return total
# test task 3
def test_check_number():
    assert check_number(5) == "Positive"
    assert check_number(-3) == "Negative"
    assert check_number(0) == "Zero"

def test_first_n_primes():
    assert first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert first_n_primes(5) == [2, 3, 5, 7, 11]

def test_sum_of_numbers():
    assert sum_of_numbers() == 5050  # Sum from 1 to 100


# task 4
def calculate_discount(price, discount):
    """Calculate the final price after applying the discount."""
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount must be numeric types.")

    final_price = price - (price * (discount / 100))
    return final_price

# test task 4
def test_calculate_discount():
    # Test with integer price and integer discount
    assert calculate_discount(100, 20) == 80

    # Test with float price and integer discount
    assert calculate_discount(100.0, 25) == 75.0

    # Test with integer price and float discount
    assert calculate_discount(200, 10.5) == 179.0  # Update expected value to 179.0

    # Test with float price and float discount
    assert calculate_discount(150.75, 30.0) == 105.525

    # Test with zero discount
    assert calculate_discount(50, 0) == 50

    # Test with zero price
    assert calculate_discount(0, 20) == 0


def test_invalid_inputs():
    # Test with invalid price types
    try:
        calculate_discount("100", 20)
    except ValueError as e:
        assert str(e) == "Price and discount must be numeric types."

    # Test with invalid discount types
    try:
        calculate_discount(100, "20")
    except ValueError as e:
        assert str(e) == "Price and discount must be numeric types."


# task 5
# List of favorite books with titles and authors
favorite_books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"}
]

# Function to get the first three books
def get_first_three_books():
    return favorite_books[:3]

# Student database as a dictionary
student_database = {
    "001": "Alice Smith",
    "002": "Bob Johnson",
    "003": "Charlie Brown",
}

# Function to get a student's name by ID
def get_student_name(student_id):
    return student_database.get(student_id, "Student ID not found.")

# test task 5
def test_get_first_three_books():
    expected_books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    ]
    assert get_first_three_books() == expected_books

def test_get_student_name():
    assert get_student_name("001") == "Alice Smith"
    assert get_student_name("002") == "Bob Johnson"
    assert get_student_name("003") == "Charlie Brown"
    assert get_student_name("004") == "Student ID not found."  # Test with a non-existent ID


# task 6
def count_words_in_file(filename):
    """Read a text file and count the number of words in it."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

# test task 6
# Sample text files and expected word counts
test_files = {
    "sample1.txt": 13,  # 13 words in sample1.txt
    "sample2.txt": 15   # 15 words in sample2.txt
}

def pytest_generate_tests(metafunc):
    """Dynamically generate test cases based on the text files."""
    if "filename" in metafunc.fixturenames:
        metafunc.parametrize("filename, expected_count", test_files.items())

def test_word_count(filename, expected_count):
    """Test the word count function."""
    assert count_words_in_file(filename) == expected_count


# task 7
def fetch_post_title(post_id):
    """Fetch a post title by its ID from the JSONPlaceholder API."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code == 200:
        post = response.json()
        return post['title']
    else:
        return "Post not found."

# test task 7
def test_fetch_post_title():
    # Test for a valid post ID
    assert fetch_post_title(1) == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

    # Test for an invalid post ID
    assert fetch_post_title(999) == "Post not found."

if __name__ == "__main__":
    print(greet())