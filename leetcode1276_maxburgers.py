#Problem:
#Given two integers tomatoSlices and cheeseSlices.The ingredients of different burgers are as follows:
#Jumbo Burger: 4 tomato slices and 1 cheese slice.
#Small Burger: 2 Tomato slices and 1 cheese slice.
# Return[total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the
#number of remaining cheeseSlices equal to 0.

#If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].
#https://leetcode.com/contest/weekly-contest-165/problems/number-of-burgers-with-no-waste-of-ingredients/


class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # odd number of tomatoes not ok
        if( tomatoSlices % 2 == 1):
            return ( [])
        #too many cheese
        if( cheeseSlices > tomatoSlices / 2 ):
            return([])
        #too few tomato
        if( cheeseSlices < tomatoSlices / 4  ):
            return([])

        tomato_for_bigones = tomatoSlices - 2*cheeseSlices;
        if ( tomato_for_bigones % 2 == 1 ):
            return ([])

        bigburger = int( tomato_for_bigones / 2);
        smallburger = cheeseSlices - bigburger;
        return ([bigburger,smallburger])


        # Long a dumb solution of mine
        #for bigburger in range(cheeseSlices,-1,-1):
        #    smallburger = cheeseSlices-bigburger
        #    if( smallburger *2 + bigburger * 4 > tomatoSlices):
        #        return ([])
        #    if( tomatoSlices-(bigburger*4+smallburger*2)==0):
        #        return ([bigburger,smallburger])
        #return([])

if __name__ == "__main__":
    sol = Solution()
    rv = sol.numOfBurgers(tomatoSlices = 16, cheeseSlices = 7)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices = 4, cheeseSlices = 17)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices = 0, cheeseSlices = 0)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices=2, cheeseSlices=1)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices=520022, cheeseSlices=149765)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices=372885, cheeseSlices=8935448)
    print(rv)

    rv = sol.numOfBurgers(tomatoSlices=1333660, cheeseSlices=535117)
    print(rv)