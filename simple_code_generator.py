
def generate_code(instruction):
    instruction = instruction.strip()

    if not instruction or "=" not in instruction:
        return ["; Invalid instruction: " + instruction]

    destination, expression = instruction.split("=", 1)
    destination = destination.strip()
    expression = expression.strip()

    parts = expression.split()

    # Example: t1 = a
    if len(parts) == 1:
        return [
            f"LOAD R1, {parts[0]}",
            f"STORE {destination}, R1"
        ]

    # Example: t1 = a + b
    if len(parts) == 3:
        left, operation, right = parts

        operations = {
            "+": "ADD",
            "-": "SUB",
            "*": "MUL",
            "/": "DIV"
        }

        if operation not in operations:
            return ["; Unsupported operator: " + operation]

        return [
            f"LOAD R1, {left}",
            f"{operations[operation]} R1, {right}",
            f"STORE {destination}, R1"
        ]

    return ["; Unsupported expression: " + expression]


def generate_program(source_code):
    assembly = []

    for instruction in source_code.splitlines():
        instruction = instruction.strip()

        if instruction:
            assembly.append(f"; {instruction}")
            assembly.extend(generate_code(instruction))
            assembly.append("")

    return assembly


if __name__ == "__main__":
    print("===== SIMPLE CODE GENERATOR =====")
    print("Enter three-address code, one instruction per line.")
    print("Example: t1 = a + b")
    print("Enter a blank line to finish.\n")

    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    print("\n--- Generated Pseudo-Assembly Code ---")
    print("\n".join(generate_program("\n".join(lines))))
