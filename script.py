from argument_parser import parse_arguments, list_days
from path_handler import generate_csv_files, read_csv_files

def main():

    # Parse command-line arguments into a dictionary.

    args = parse_arguments()

    # Choose the correct action and process paths for generated lists.

    if (args["create"]):
        generate_csv_files(args["months"], list_days(args["days"]), args["times"])
    else:
        read_csv_files(args["months"], list_days(args["days"]), args["times"])

if __name__ == "__main__":
    main()
