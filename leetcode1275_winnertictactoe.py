# Problem: 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/contest/weekly-contest-165/problems/find-winner-on-a-tic-tac-toe-game/

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        player = 'A'
        grid=[['','',''],['','',''],['','','']]


        def nextplayer(player):
            if player=='A':
                player='B';
            else:
                player='A'
            return player

        def checkwinner():
            #check rows
            for row in range(0,3):
                if(grid[0][row] == grid[1][row] and grid[1][row]==grid[2][row]):
                    return grid[0][row]
            # check rows
            for col in range(0, 3):
                if (grid[col][0] == grid[col][1] and grid[col][1] == grid[col][2]):
                    return grid[col][0]
            #check cross1
            if( grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]):
                return grid[1][1]
            #check cross1
            if (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]):
                return grid[1][1]
            #no winner so far
            return ''

        def pprintgrid():
            print(grid[0])
            print(grid[1])
            print(grid[2])

        player='A'
        for move in moves:
            grid[move[0]][move[1]]=player;
            #print(move,player)
            #pprintgrid()
            winner = checkwinner()
            if( winner == 'A'):
                return 'A'
            if( winner == 'B'):
                return 'B'
            player=nextplayer(player)

        if(len(moves)>=9 and winner ==''):
            return 'Draw'

        return 'Pending'


if __name__ == "__main__":
    sol = Solution()

    rv = sol.tictactoe(moves=[[0,0],[2,2],[1,0],[2,0],[0,1],[1,2],[1,1],[0,2]])
    print(rv)


    rv = sol.tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]])
    print(rv)

    rv = sol.tictactoe(moves=[[0, 2], [1, 0], [1, 1], [2, 1], [2, 0]])
    print(rv)

    rv = sol.tictactoe(moves=[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
    print(rv)

    rv = sol.tictactoe(moves=[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
    print(rv)

    rv = sol.tictactoe([[0, 0], [1, 1]])
    print(rv)
