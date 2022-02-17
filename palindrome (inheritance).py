class Check :

    def __init__(self,number) :
        self.num = number
        
  def isPalindrome(self) :
      temp = self.num
      result = 0

       while(temp != 0) :
            
            rem = temp % 10
            result =  result * 10 + rem
            temp //= 10

        
        if self.num == result :
            print(self.num,"is Palindrome")
        else :
            print(self.num,"is not Palindrome")



if __name__ == "__main__" :
    
    
    num = 151
    
    
    check_Palindrome = Check(num)
    
    
    check_Palindrome.isPalindrome()
    
    num = 127
    check_Palindrome = Check(num)
    check_Palindrome.isPalindrome()
