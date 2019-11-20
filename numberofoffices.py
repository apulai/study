class Solution(object):






    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def resetNeighbour(grid, x, y):

            if x < 0:
                return

            if y < 0:
                return

            if x == len(grid):
                return
            if y == len(grid[0]):
                return

            # If this is a floor, reset it and it's neighbours'
            if grid[x][y] == '1':
                resetNeighbour(grid, x + 1, y)
                resetNeighbour(grid, x, y + 1)

                grid[x][y] = '0';
                # print(grid)
            return




        retval=0
        for y in range(len(grid[0])):
            #print("\n")
            for x in range(len(grid)):
              #print("{}{} ",x,y)
              if grid[x][y] == '1':
                  # We have found a floor
                  retval = retval +1
                  resetNeighbour(grid,x,y)
                  #print(grid)
        return retval


def prettyprint(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"] * col] * row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid


if __name__ == "__main__":
    sol = Solution()
    #matrix = get_matrix()
    #matrix = [[ '1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    matrix = [['1','1','1','1','1'],['1','0','0','0','1'],['1','0','0','0','0'],['1','1','1','0','1']]
    prettyprint(matrix)
    offices = sol.numOffices(matrix)
    print(offices)