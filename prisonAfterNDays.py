from copy import copy


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        1) Record each state of cells as you mutate them, and record the iteration that they are seen at (starting at N)
        2) As soon as a given state is seen previously, we will then enter the cycle, and find the previous iteration it was at, and the number of steps it takes to repeat
        3) Then reduce N to be N%(length of cycle), the rest of N is simply finishing the rest of that cycle (less than one full cycle)

        Time: O (min(Length of cycle, N)).
        Space: O(min(length of cycle, N) * len(cells))

        """
        previous = {}
        size = len(cells)
        while N:
            previous.setdefault(tuple(cells),
                                N)  # Save cells in previous only if it does not yet exist in previous, otherwise this does nothing.
            N -= 1
            next_state = [0] * size
            for i in range(1, size - 1):
                next_state[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = copy(next_state)
            if tuple(cells) in previous:
                first_repeat_position = previous[tuple(cells)]
                cycle_length = first_repeat_position - N
                N %= cycle_length  # Once N has been reudced once before, N will be less than cycle length now, so N %=cycle_length will just be N, ie: N will be reduced one by one once a cycle has been seen.
        return cells

    def prisonAfterNDays_2(self, cells: List[int], N: int) -> List[int]:
        first_state = copy(cells)
        N -= 1
        iterations = 1
        size = len(cells)
        next_state = [0] * size
        for i in range(1, size - 1):
            next_state[i] = 1 if cells[i - 1] == cells[i + 1] else 0
        cells = next_state
        while N:
            N -= 1
            next_state = [0] * size
            for i in range(1, size - 1):
                next_state[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            if next_state == first_state:
                N %= iterations
            cells = next_state
            iterations += 1
        return cells