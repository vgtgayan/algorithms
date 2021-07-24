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
def can_sum(n, arr):
    if n == 0:
        return True
    for i in arr:
        if i<=n:
            return can_sum(n-i, arr)
            
    return False




def can_sum_memo(n, arr, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    for i in arr:
        if i<=n:
            memo[n] = can_sum_memo(n-i, arr, memo)
            return memo[n]
    memo[n] = False
    return memo[n]

    return False



def main():
    print(can_sum(5,[5,3,4,7])) # 
    print(can_sum_memo(5,[5,3,4,7])) # 
    print(can_sum(4,[5,3])) # 
    print(can_sum_memo(4,[5,3])) # 
    print(can_sum_memo(500,[5,3,4,7])) # 
    print(can_sum(500,[5,3,4,7])) # 
#    print(can_sum(50,50)) # Hang

if __name__ == "__main__":
    main()