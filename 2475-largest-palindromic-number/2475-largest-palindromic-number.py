class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import defaultdict

        # Step 1: Create a dictionary to count the occurrences of each digit.
        digit_count = defaultdict(int)
        for x in num:
            digit_count[x] += 1

        # Step 2: Create a list of digits in decreasing order (from 9 to 0).
        digits = [str(x) for x in range(9, -1, -1)]

        # Step 3: Initialize a list to build the largest palindromic integer.
        palindrome = []

        # Step 4: Iterate through the digits in decreasing order.
        for digit in digits:
            count = digit_count[digit]
            n = len(palindrome)

            if n % 2 == 0:
                # If the current palindrome length is even:
                if count > 0:
                    # Add the digit to both sides of the palindrome.
                    palindrome = palindrome[:n // 2] + [digit] * count + palindrome[n // 2:]
            else:
                # If the current palindrome length is odd:
                if digit == '0':
                    if len(palindrome) != 1:
                        # If there is more than one digit in the palindrome, add '0' in the middle.
                        palindrome = palindrome[:n // 2] + ['0'] * (count // 2) + [palindrome[n // 2]] + ['0'] * (count // 2) + palindrome[n // 2 + 1:]
                else:
                    # Add the digit to both sides of the palindrome.
                    if count >= 2:
                        palindrome = palindrome[:n // 2] + [digit] * (count // 2) + [palindrome[n // 2]] + [digit] * (count // 2) + palindrome[n // 2 + 1:]

        # Step 5: Convert the list to a string and remove leading zeroes.
        result = ''.join(palindrome).lstrip('0')

        # Step 6: Return the largest palindromic integer as a string.
        return result if result else '0'



        