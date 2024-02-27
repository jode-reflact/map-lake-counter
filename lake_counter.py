class LakeCounter:
    def __init__(self) -> None:
        pass

    def mark_all_neighbours(self, map: list[list[int]], row_idx: int, col_idx: int):
        """Marks all lake pieces which are connected to the current lake by setting there value to 0.
        Uses an recursive search in 4 possible directions (vertical and horizontal) after checking for valid indeces in these directions

        Args:
            map (list[list[int]]): list representation of the map
            row_idx (int): current row idx
            col_idx (int): current col idx
        """
        value = map[row_idx][col_idx]
        if value == 0:
            return
        # sets the current entry to 0 to prevent an endless loop in combination with the next neighbour
        map[row_idx][col_idx] = 0

        # check if there is another row above the current position
        if row_idx >= 1:
            self.mark_all_neighbours(map, row_idx - 1, col_idx)
        # check if there is another row below the current position
        if row_idx < len(map) - 1:
            self.mark_all_neighbours(map, row_idx + 1, col_idx)
        
        # check if there is another col to the left
        if col_idx >= 1:
            self.mark_all_neighbours(map, row_idx, col_idx - 1)
        # check if there is another col to the right
        if col_idx < len(map[row_idx]) - 1:
            self.mark_all_neighbours(map, row_idx, col_idx + 1)

    def count_lakes(self, map: list[list[int]]) -> int:
        """Counts lakes on a 2D-map representing lakes with the value 1 and land with 0
        example:
            map = [
                [0,1,1,0,0,1,1,0],
                [0,0,0,0,1,1,0,0],
                [0,1,1,1,1,1,1,1]
            ]
        The example consists of two lakes.

        Args:
            map (list[list[int]]): list representation of the map

        Returns:
            int: lake count
        """
        counter: int = 0
        for row_idx in range(len(map)):
            for col_idx in range(len(map[row_idx])):
                value = map[row_idx][col_idx]
                if value == 1:
                    counter += 1
                    self.mark_all_neighbours(map, row_idx, col_idx)
        return counter