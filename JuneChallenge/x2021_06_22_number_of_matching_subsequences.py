# MIT License
#
# Copyright (c) 2021 Andrew Hughes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from typing import List


class Solution:
   # Assumptions:
    # 1 <= s.length <= 5 * 10^4
    # 1 <= words.length <= 5000
    # 1 <= words[i].length <= 50
    # s and words[i] consist of only lowercase English letters.
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count: int = 0
        word: int
        # Possible improvements -- words may not be unique and/or may be prefix of others.
        for word in words:
            # Handle single character word separately.
            if len(word) == 1:
                for c in s:
                    if c == word[0]:
                        count += 1
                        break
            else:
                s_pos = 0
                out_of_bounds = False
                for next_char in word:
                    # Find leftmost match for next character in remaining suffix of s.
                    while s_pos < len(s) and next_char != s[s_pos]:
                        s_pos += 1
                    # Check if end of string reached.
                    if s_pos == len(s):
                        # If no character found, then this word is not present.
                        out_of_bounds = True
                        break
                    else:
                        # Match found at s_pos, start looking from next index.
                        s_pos += 1
                # out_of_bounds flag unchanged if end of word reached without incident.
                # Cannot use s_pos at end due to last valid increment moving to s_pos == len(s).
                if not out_of_bounds: count += 1
        return count