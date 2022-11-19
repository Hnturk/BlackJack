logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
from turtle import clear
print(logo)
cash = 2500 
print(f"You have {cash}$")
while True: 
 
 a= 11
 q= 10  
 k= 10  
 j= 10  
 deck=[1,2,3,4,5,6,7,8,9,a,q,k,j]  
 card1=random.choice(deck)
 card2=random.choice(deck) 
 mydeck=[]
 pcdeck=[]
 mydeck.append(card1)
 mydeck.append(card2)
 firstcard=random.choice(deck)
 secretcard1=random.choice(deck) 
 totalcards=int(card1)+int(card2)  
 pcdeck.append(firstcard)
 pcdeck.append(secretcard1)
 totalcards2=int(firstcard)+int(secretcard1)
 c=input("Do you want to play a game of BlackJack? Type'y' or 'n':").lower()
 if c =="y":
     bet=int(input("How much do you want to bet:"))
     if totalcards==21:
       print("BlackJack You Win") 
       cash+=(bet*3/2)
       print(f"Your current amount {cash}")

     else:
      print(f"Your cards:{mydeck}  current skor:{totalcards}")
      print(f"Computer's first card:{firstcard} ")
     while True:
      b=input("Type 'y' to get another card? Type'n' to pass:").lower()
      if b =="y":
        card3=random.choice(deck) 
        mydeck.append(card3)
        totalcards += card3     
        if totalcards > 21:
           print(f"Your final hand: {mydeck} final skor: {totalcards}")
           print("You went over")
           cash -= bet
           print(f"Your remaining amount {cash}")
           break 
        elif totalcards <=21:
         print(f"Your cards: {mydeck} current skor: {totalcards}")
         print(f"Computer's first card:{firstcard} ")
      else:
        while totalcards2 <= 16:
         thirdcardpc=random.choice(deck) 
         totalcards2 += thirdcardpc
         pcdeck.append(thirdcardpc)  
        print(f"Your final hand: {mydeck} final skor: {totalcards}")
        print(f"Computer's final hand:{pcdeck} final skor: {totalcards2} ")
        if totalcards2>totalcards and totalcards2 <= 21:
          print("You lost")
          cash-=bet
          print(f"Your remaining amount {cash}")
        elif totalcards2>totalcards and totalcards2 > 21:
          print("You win")
          cash+=bet
          print(f"Your current amount {cash}")
        elif totalcards>totalcards2 and totalcards <= 21: 
          print("You win")
          cash+=bet
          print(f"Your current amount {cash}")
        elif totalcards>totalcards2 and totalcards > 21:
          print("You lost")
          cash-=bet
          print(f"Your remaining amount {cash}")
        elif totalcards==totalcards2:
          print("Draw")   
          print(f"Your current amount {cash}")
        break  

 else:
   break    
    
   