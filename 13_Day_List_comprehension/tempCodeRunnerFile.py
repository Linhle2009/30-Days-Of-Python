calculate_y_intercept = lambda x, y, m: y - m * x

# --- Examples ---
print("\n--- Y-intercept Calculation ---")

# Example 1: Line with slope m=2 passing through (5, 9)
# b = 9 - 2 * 5 = 9 - 10 = -1
y_intercept1 = calculate_y_intercept(5, 9, 2)
print(f"Y-intercept for point (5,9) and slope 2: {y_intercept1}") # Output: -1

# Example 2: Line with slope m=-2 passing through (1, 5)
# b = 5 - (-2) * 1 = 5 + 2 = 7
y_intercept2 = calculate_y_intercept(1, 5, -2)
print(f"Y-intercept for point (1,5) and slope -2: {y_intercept2}") # Output: 7

# Example 3: Line with slope m=0.5 passing through (4, 7)
# b = 7 - 0.5 * 4 = 7 - 2 = 5
y_intercept3 = calculate_y_intercept(4, 7, 0.5)
print(f"Y-intercept for point (4,7) and slope 0.5: {y_intercept3}") # Output: 5.0