from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        for right in range(len(s1), len(s2)):
            # Dodaj novi karakter koji ulazi u prozor.
            window[s2[right]] += 1

            # Ukloni karakter koji izlazi iz prozora.
            left_char = s2[right - len(s1)]
            window[left_char] -= 1

            # Ako frekvencija postane 0, uklanjamo ključ.
            if window[left_char] == 0:
                del window[left_char]

            if window == target:
                return True

        return False