# 🔢 Swapped Pairs (1 to N)

This program asks the user for a positive integer and prints all numbers from 1 up to that number, but with a special rule:

👉 Numbers are printed in swapped pairs:

- 2 comes before 1
- 4 comes before 3
- 6 comes before 5
- and so on...

---

## 📌 Example

### Input:

5

### Output:

2
1
4
3
5

---

## 🧠 How it works

The program goes through numbers from 1 to N and groups them in pairs.

For each pair:

- The even number is printed first
- Then the odd number before it

If the total number is odd, the last number is printed as it is.

Example:

- (1, 2) → printed as 2, 1
- (3, 4) → printed as 4, 3
