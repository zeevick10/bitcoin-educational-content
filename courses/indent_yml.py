import os

def process_yaml(file_path):
    print(f"Checking file: {file_path}")
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    in_explanation = False
    modified = False
    
    for i, line in enumerate(lines):
        if line.startswith('explanation:'):
            print(f"Found explanation: at line {i+1}")
            in_explanation = True
            new_lines.append(line)
        elif line.startswith('reviewed:'):
            print(f"Found reviewed: at line {i+1}")
            in_explanation = False
            new_lines.append(line)
        elif in_explanation and line.strip():  # if line is not empty
            if not line.startswith('  '):  # if line doesn't start with double space
                print(f"Adding indentation to line {i+1}: {line.strip()}")
                new_lines.append('  ' + line)
                modified = True
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    if modified:
        print(f"Writing changes to {file_path}")
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

def main():
    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.yml'):
                yaml_path = os.path.join(root, file)
                process_yaml(yaml_path)

if __name__ == '__main__':
    main()
