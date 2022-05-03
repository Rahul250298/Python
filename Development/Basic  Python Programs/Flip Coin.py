import random
def flipCoin(T):
    heads = 0
    tails = 0
    headspercent = 0
    tailspercent = 0
    for i in range (0,T) :
        Coin = random.random()
        print(Coin)
        if(float(Coin) < 0.5):
            heads += 1
        else:
            tails += 1
    headspercent = (heads/T) * 100
    tailspercent = (tails/T) * 100
    print("Percentage of tail  {}".format(headspercent))
    print("Percentage of head  {}".format(tailspercent))
T = int(input("Enter the number to flip coin :"))
flipCoin(T)

            

 
  

 
            
            
   
        