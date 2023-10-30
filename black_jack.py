import os
os.system("clear")
import random
import time





start = '''


!                                                                                                                                          
!  88888888ba   88                  db           ,ad8888ba,   88      a8P               88         db           ,ad8888ba,   88      a8P   
!  88       8b  88                 d88b         d8**    **8b  88    ,88*                88        d88b         d8**    **8b  88    ,88"    
!  88       8P  88                d8**8b       d8*            88  ,88*                  88       d8**8b       d8*            88  ,88*      
!  88aaaaaa8b   88               d8*  *8b      88             88,d88*                   88      d8*  *8b      88             88,d88*       
!  88*******8b  88              d8YaaaaY8b     88             8888*88,                  88     d8YaaaaY8b     88             8888*88,      
!  88       8b  88             d8********8b    Y8,            88P   Y8b                 88    d8********8b    Y8,            88P   Y8b     
!  88       8P  88            d8*        *8b    Y8a.    .a8P  88     *88,       88,   ,d88   d8*        *8b    Y8a.    .a8P  88     *88,   
!  88888888P*   88888888888  d8*          *8b    **Y8888Y**   88       Y8b       *Y8888P*   d8*          *8b    **Y8888Y**   88       Y8b  
!                                                                                                                                          
!                                                                                                                                          

'''


h= ""
for _ in range(7):
	print (start)
	h= h+("#"*20)
	print (h)
	time.sleep(1)
	os.system("clear")






m = [".------.","|$.--. |","| (\/) |","| :\/: |","| '--'$|","`------'"]


cards = [11,2,3,4,5,6,7,8,9,10,10,10]



def s_card(card):
	x=random.choice(card)
	return x



my_cards=[]
dealer_card=[]


for _ in range(0,2):
	my_cards.append( s_card(cards))
	dealer_card.append(s_card(cards))

def dis_cards():
	os.system("clear")
	for k in m:
		print (f"{(k*len(my_cards))}       {(k*len(dealer_card))}")




dis_cards()
print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
print (f"computer cards is { dealer_card[0:len(dealer_card)-1]} ,x ")

a=sum(my_cards)
b=sum(dealer_card)

if a<=21:
	Game = True
else:
	print("you loss")
	Game = False

while Game :


	select= input("did you want to show press s or add new card press n ")
	if select == "s":
		print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
		dis_cards()
		if b<=21 and b>a and b>17:
			dis_cards()
			print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
			print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
			print ("you loss")
			Game  = False


		elif b<17:
			n_card = s_card(cards)
			if n_card == 11 and sum(dealer_card)<11:
				dealer_card.append(n_card)
				dis_cards()
				print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
				print (f"computer cards is { dealer_card[0:len(dealer_card)-1]} , x ")
			elif n_card== 11 and sum(dealer_card)>11:
				dealer_card.append(1)
				dis_cards()
				print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
				print (f"computer cards is { dealer_card[0:len(dealer_card)-1]} ,x ")
				if sum(dealer_card) > 21:
					dis_cards()
					print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
					print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
					print ("you win")
					Game = False
			else:
				dealer_card.append(n_card)
				dis_cards()
				print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
				print (f"computer cards is { dealer_card[0:len(dealer_card)-1]} ,x")
				if sum(dealer_card) > 21:
					dis_cards()
					print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
					print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
					print ("you win")
					Game = False



	if select == "n":
		n_card = s_card(cards)
		if n_card == 11 and sum(my_cards)<11:
			my_cards.append(n_card)
			dis_cards()

			print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
			if sum(my_cards) > 21:
				print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
				print ("you loss")
				Game = False

		elif n_card == 11 and sum(my_cards)>11:
			my_cards.append(1)
			dis_cards()
			print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
			if sum(my_cards) > 21:
				print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
				print ("you loss")
				Game = False
		else:
			my_cards.append(n_card)
			dis_cards()
			print(f"your cards is {my_cards} sum is {sum(my_cards)} ")
			if sum(my_cards) > 21:
				print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
				print ("you loss")
				Game = False

