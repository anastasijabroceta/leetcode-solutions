from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        words = set(wordList)

        # Ako krajnja riječ nije u listi, transformacija nije moguća.
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        # beginWord označavamo kao već posjećenu riječ.
        if beginWord in words:
            words.remove(beginWord)

        while queue:
            current_word, length = queue.popleft()

            # Ako smo stigli do krajnje riječi,
            # vraćamo broj riječi u najkraćoj sekvenci.
            if current_word == endWord:
                return length

            # Pokušavamo promijeniti svako slovo trenutne riječi.
            for i in range(len(current_word)):

                # Na svakoj poziciji pokušavamo sva slova a-z.
                for letter in "abcdefghijklmnopqrstuvwxyz":

                    if letter == current_word[i]:
                        continue

                    new_word = (
                        current_word[:i]
                        + letter
                        + current_word[i + 1:]
                    )

                    # Ako nova riječ postoji u rječniku,
                    # ona je susjed trenutne riječi u grafu.
                    if new_word in words:
                        queue.append((new_word, length + 1))

                        # Odmah je uklanjamo da je ne bismo
                        # ponovo dodavali u red.
                        words.remove(new_word)

        return 0
if __name__ == "__main__":
    solution = Solution()

    print(
        solution.ladderLength(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"]
        )
    )  # 5

    print(
        solution.ladderLength(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"]
        )
    )  # 0