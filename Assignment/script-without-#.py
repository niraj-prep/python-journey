#Copy Python script to another file, excluding comments

source_file = input("Enter the source Python file name: ")
dest_file = input("Enter the destination Python file name: ")

try:
    with open(source_file, 'r') as f:
        lines = f.readlines()

    # Filter out full-line comments and inline comments
    filtered_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            continue  # Skip comment lines
        # Remove inline comments
        if '#' in line:
            line = line[:line.index('#')] + '\n'
        if line.strip():  # Skip blank lines left after removing inline comments
            filtered_lines.append(line)

    with open(dest_file, 'w') as f:
        f.writelines(filtered_lines)

    print("\n--- Source File Contents ---")
    with open(source_file, 'r') as f:
        print(f.read())

    print("\n--- Destination File Contents (No Comments) ---")
    with open(dest_file, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print(f"Error: File '{source_file}' not found.")