cipher = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"
result = ""
for i in range(2, len(cipher), 3):
    result += cipher[i] + cipher[i-2] + cipher [i-1]
    print(result)
