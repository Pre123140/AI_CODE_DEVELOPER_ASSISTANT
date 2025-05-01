def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

nums = [1, 2, 3, 4, 2, 5, 6, 3, 1, 7]
print("Duplicate numbers:", find_duplicates(nums))
