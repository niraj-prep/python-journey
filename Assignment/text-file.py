#Read a file and write its contents in uppercase to a new file

source_file = input("Enter the source file name (with extension): ")
dest_file = input("Enter the destination file name (with extension): ")

try:
    with open(source_file, 'r') as f:
        content = f.read()

    with open(dest_file, 'w') as f:
        f.write(content.upper())

    print(f"\nContents written to '{dest_file}' in uppercase successfully!")

    print("\n--- Contents of Destination File ---")
    with open(dest_file, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print(f"Error: File '{source_file}' not found.")