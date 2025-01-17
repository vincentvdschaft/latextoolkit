from pathlib import Path

def create_latex_command(directory, name, value, output_filename="auto_macros.tex"):
    """Add the latex command to the file. If the command already exists, update the value.
    The macros will be stored
    
    Note
    ----
    LaTeX commands may not comtain digits. If the name contains digits,
    they will be replaced by their word representation.
    
    """
    
    output_directory = Path(directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    
    file_path = output_directory / output_filename
    
    # Read the file
    try:
        with file_path.open("r", newline="\n", encoding="ascii") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    # Replace any digits in the name
    new_name = _replace_digits(name)
    if new_name != name:
        print(f"Replaced digits in name: {name} -> {new_name}")
    name = new_name

    # Create the command
    command = r"\newcommand{" + "\\" + name + r"}{" + str(value) + r"}"
    
    # Update the command if it already exists
    for n, line in enumerate(lines):
        if line.startswith(f"\\newcommand{{\\{name}}}"):
            lines[n] = command
            break
    # Add the command if it does not exist
    else:
        lines.append(command)

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    with file_path.open("w", newline="\n", encoding="ascii") as f:
        for line in lines:
            print(line, file=f)




def _replace_digits(text):
    text = text.replace("1", "one")
    text = text.replace("2", "two")
    text = text.replace("3", "three")
    text = text.replace("4", "four")
    text = text.replace("5", "five")
    text = text.replace("6", "six")
    text = text.replace("7", "seven")
    text = text.replace("8", "eight")
    text = text.replace("9", "nine")
    text = text.replace("0", "zero")
    return text
