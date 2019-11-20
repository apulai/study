class Solution(object):

    def largestTable(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def willfit(grid, x, y, sizex, sizey):
            #print("\n-({}{})-----------\n".format(x,y))
            for i in range(1+sizex):
                for j in range(1+sizey):
                    #print("({}{})".format((x+i),(y+j)),end="")
                    if grid[y+j][x+i]=='0':
                      return 0
            return 1

        largest=0
        for y in range(len(grid)):
            #print("\n")
            for x in range(len(grid[0])):
                #print("{}{} ".format(x,y))
                for sizey in range(0,len(grid)-y):
                    for sizex in range(0,len(grid[0])-x):
                        #print("Trying to fit a table at {},{} size {},{}".format(x,y,sizex,sizey),end =" ")
                        retval=willfit(grid,x,y,sizex,sizey)
                        if( retval == 1):

                            if( (sizex+1)*(sizey+1) > largest):
                                largest=(sizex+1)*(sizey+1)
                                #print("will fit {}".format(largest))
                            else:
                                largest=largest
                                #print("will fit ")
                        else:
                            #print("will not fit")
                            break
        return largest


def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"] * col] * row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid

def prettyprint(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == "__main__":
    sol = Solution()
    #matrix = get_matrix()
    #matrix = [[ '1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]

    #matrix = [['1','1','1','1','1'],['1','0','0','0','1'],['1','0','0','0','0'],['1','1','1','0','1']]

    #matrix = [['1', '0', '1', '1', '1'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'],['1', '0', '0', '1', '0']]

    matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'],['1', '0', '0', '1', '0']]


    biggest = sol.largestTable(matrix)
    print(biggest)
    prettyprint(matrix)

    # for y in range(len(matrix)):
    #    print("\n")
    #    for x in range(len(matrix[0])):
    #             print("{}{} ".format(x,y),end="")
