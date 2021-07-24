"""
/*******************************************************
 * Project   : DP_MASTER
 * Summary   : Master Dynamic Programming Concepts
 * Author(s) : VGT GAYAN
 * Date      : 2021/07/24
 * Copyright (C) 2020-2021 {VGT GAYAN} <{gayanvgt@gmail.com}>
 * 
 * This code cannot be copied and/or distributed without the express
 * permission of {VGT GAYAN}

 **      **   ********  **********
/**     /**  **//////**/////**/// 
/**     /** **      //     /**    
//**    ** /**             /**    
 //**  **  /**    *****    /**    
  //****   //**  ////**    /**    
   //**     //********     /**    
    //       ////////      //     
 *******************************************************/                                    
"""

""" PROBLEM:
Kelvin the Frog lives at the origin, and wishes to visit his friend at (5,5). 
At any point, Kelvin the Frog can only hop 1 unit up or 1 unit to the right. 
How many paths are there from Kelvin to his friend?
 """


""" 
Brute force implementation
Time complexity: O(2**(m+n))
Space complexity: O(m+n)
"""
def grid_traveller(m,n):
    if (m==1 and n==1):
        return 1
    if (m==0 or n==0):
        return 0
    return grid_traveller(m-1,n) + grid_traveller(m,n-1)

"""
# Dynamic Programming implementation - Memoization
Time complexity: O(m*n)
Space complexity: O(m+n)
"""
def grid_traveller_memo(m,n, memo={}):
    
    key = "{},{}".format(m,n)
    key_dup = "{},{}".format(n,m)

    # Memoization
    if key in memo:
        return memo[key]
    # memo[m,n] = memo[n,m]
    if key_dup in memo:
        return memo[key_dup]
    if (m==1 and n==1):
        return 1
    if (m==0 or n==0):
        return 0
    memo[key] = grid_traveller_memo(m-1,n, memo) + grid_traveller_memo(m,n-1, memo)
    return memo[key]


def main():
    print(grid_traveller_memo(5,5)) # 70
    print(grid_traveller(5,5)) # 70
    print(grid_traveller_memo(50,50)) # 25477612258980856902730428600
    print(grid_traveller(50,50)) # Hang 

if __name__ == "__main__":
    main()