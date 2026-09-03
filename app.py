import string
import random

# Dictionary to store shortened URLs
url_database = {}


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def shorten_url(long_url):
    short_code = generate_short_code()

    while short_code in url_database:
        short_code = generate_short_code()

    url_database[short_code] = long_url

    return short_code


def get_original_url(short_code):
    return url_database.get(short_code)


def main():
    print("=" * 40)
    print("       PYTHON URL SHORTENER")
    print("=" * 40)

    while True:
        print("\n1. Shorten URL")
        print("2. Open Shortened URL")
        print("3. Show All URLs")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            long_url = input("Enter the long URL: ")

            if long_url.strip() == "":
                print("URL cannot be empty.")
            else:
                short_code = shorten_url(long_url)
                print("\nShortened URL: http://short.url/" + short_code)

        elif choice == "2":
            short_code = input("Enter the short code: ")
            original_url = get_original_url(short_code)

            if original_url:
                print("Original URL:", original_url)
            else:
                print("Short URL not found.")

        elif choice == "3":
            if not url_database:
                print("No URLs stored.")
            else:
                print("\n--- Stored URLs ---")
                for code, url in url_database.items():
                    print("http://short.url/" + code, "->", url)

        elif choice == "4":
            print("Thank you for using URL Shortener!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
