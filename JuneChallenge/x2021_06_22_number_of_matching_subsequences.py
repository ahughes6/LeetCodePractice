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

from typing import List, Set, Dict

# Assumptions:
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

class BruteForceSolution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count: int = 0
        word: str
        word_counts = {}
        # Possible improvements -- words may not be unique and/or may be prefix of others.
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        for word, multiplicity in word_counts.items():
            # Handle single character word separately.
            if len(word) == 1:
                for c in s:
                    if c == word[0]:
                        count += multiplicity
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
                if not out_of_bounds: count += multiplicity
        return count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count: int = 0
        word: int
        trie_root = (0,{})
        next_node_id = 1
        valid_node_key = 'count'
        # Build path in trie to each word.
        for word in words:
            current = trie_root
            for c in word:
                if c not in current[1]:
                    current[1][c] = (next_node_id, {})
                    next_node_id += 1
                current = current[1][c]
            if valid_node_key in current[1]:
                # Duplicate word, so count is more than 1.
                current[1][valid_node_key] += 1
            else:
                current[1][valid_node_key] = 1
        # Branch down trie for each valid transition. Only include valid words into count once.
        # Active nodes is a dict holding a set of active node ids mapping to the node.
        active_nodes: Dict[int,Dict] = {}
        active_nodes[trie_root[0]] = trie_root
        for c in s:
            additional_nodes: Dict[int,Dict] = {}
            removal_nodes: Set[int] = set()
            # Transition each possible active node based on current character.
            for node_id, node_pair in active_nodes.items():
                node_children = node_pair[1]
                if c in node_children:
                    # Transition exists from node to child.
                    subpath_root_node_pair = node_children[c]
                    subpath_children = subpath_root_node_pair[1]
                    # Check if we have reached a valid word in the trie.
                    if valid_node_key in subpath_children:
                        count += subpath_children[valid_node_key]
                        #  Remove count to avoid double-counting.
                        del subpath_children[valid_node_key]
                    # Add new path if there is anything to explore.
                    if len(subpath_children) > 0:
                        additional_nodes[subpath_root_node_pair[0]] = subpath_root_node_pair
                    # Disconnect subpath since greedy choice of leftmost appearance in s is sufficient.
                    del node_children[c]
                    # Remove current node from active nodes if it no longer has any children.
                    if len(node_children) == 0:
                        removal_nodes.add(node_id)
            for node_id, node_pair in additional_nodes.items():
                active_nodes[node_id] = node_pair
            for node_id in removal_nodes:
                del active_nodes[node_id]
        return count