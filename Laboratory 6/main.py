from Grammar import Grammar
from Parser import Parser


def main():
    while True:
        print("Choose an option:")
        print("1. Run Parser 1")
        print("2. Run Parser 2")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sequence_file = "seq1.txt"
            grammar_file = "g1.txt"
        elif choice == '2':
            sequence_file = "seq2.txt"
            grammar_file = "g2.txt"
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        grammar = Grammar()
        grammar.read_from_file(grammar_file)

        parser = Parser(grammar, sequence_file)
        parser.run()


if __name__ == "__main__":
    main()
