#1277. Count Square Submatrices with All Ones
#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxrow=len(matrix)
        maxcol=len(matrix[0])
        maxdim=min(maxrow,maxcol)
        valid_squares=0
        for dim in range(maxdim,0,-1):
            #print("side: {}".format(dim))
            #valid_squares = 0
            for row in range(0,maxrow+1-dim):
                for col in range(0,maxcol+1-dim):
                    #print("Row {} Col {}".format(row,col))
                    ok = 1
                    for i in range(0,dim):
                        for j in range (0,dim):
                            if(matrix[row+i][col+j] == 0):
                                ok=0
                                break
                        if ok == 0:
                            break
                    if ok == 1:
                        valid_squares = valid_squares + 1
                    #print(valid_squares)

        return valid_squares

if __name__ == "__main__":
    sol = Solution()

    rv = sol.countSquares(matrix =[ [0,1,1,1],  [1,1,1,1],  [0,1,1,1]])
    print("Expected result 15 - {}".format(rv))

    rv = sol.countSquares(matrix=[[1,0,1],[1,1,0],[1,1,0]])
    print("Expected result 7 - {}".format(rv))


