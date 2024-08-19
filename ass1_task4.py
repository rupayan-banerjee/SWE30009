def check_for_fault(A, B):
    # Original calculation
    correct_C = ((A + B) * B) - 5

    fault_cases = [
        ((A + B) + B) + 5,
        ((A + B) + B) - 5,
        ((A + B) + B) * 5,
        ((A + B) - B) + 5,
        ((A + B) - B) - 5,
        ((A + B) - B) * 5,
        ((A + B) * B) + 5,
        ((A + B) * B) * 5,
        ((A - B) + B) + 5,
        ((A - B) + B) - 5,
        ((A - B) + B) * 5,
        ((A - B) - B) + 5,
        ((A - B) - B) - 5,
        ((A - B) - B) * 5,
        ((A - B) * B) + 5,
        ((A - B) * B) - 5,
        ((A - B) * B) * 5,
        ((A * B) + B) + 5,
        ((A * B) + B) - 5,
        ((A * B) + B) * 5,
        ((A * B) - B) + 5,
        ((A * B) - B) - 5,
        ((A * B) - B) * 5,
        ((A * B) * B) + 5,
        ((A * B) * B) - 5,
        ((A * B) * B) * 5
    ]

    # Check if any of the incorrect cases give the same result as the correct one
    for fault_C in fault_cases:
        if correct_C == fault_C:
            return True
    return False


def find_values_of_A(B):
    A_values = []
    for A in range(-100, 101):  # Checking within a reasonable range of A values
        if check_for_fault(A, B):
            A_values.append(A)
    return A_values


# Set B to 2 and find all the hidden A values
B = 2
hidden_A_values = find_values_of_A(B)
print(f"Values of A that hide faults when B = {B}: {A_values}")
