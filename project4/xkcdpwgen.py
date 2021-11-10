import string
import random


def generate(length=35, digits_count=5, upper_count=5, special_count=5):
    lower_count = max(0, length - digits_count - upper_count - special_count)

    digits = random.sample(string.digits, digits_count)
    specials = random.sample(string.punctuation, special_count)
    upper = random.sample(string.ascii_uppercase, upper_count)
    lower = random.sample(string.ascii_lowercase, lower_count)

    password = list(digits + upper + lower + specials)
    random.shuffle(password)
    return "".join(password)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument("-l", '--length', type=int, default=35,
                        help='Password length.')
    parser.add_argument("-d", '--digits_count', type=int, default=5,
                        help='Digits count.')
    parser.add_argument("-u", '--upper_count', type=int, default=5,
                        help='Uppper characters count.')
    parser.add_argument("-s", '--special_count', default=5,
                        type=int, help='Special characters count.')

    args = parser.parse_args()
    password = generate(
        length=args.length,
        upper_count=args.upper_count,
        digits_count=args.digits_count,
        special_count=args.special_count
    )

    print(password)


if __name__ == "__main__":
    main()
