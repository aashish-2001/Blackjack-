import random



cards = [11,2,3,4,5,6,7,8,9,10,10,10]



def s_card(card):
	x=random.choice(card)
	return x



my_cards=[]
dealer_card=[]


for _ in range(0,2):
	my_cards.append( s_card(cards))

for _ in range(0,2):
	dealer_card.append(s_card(cards))

print (f"your cards is {my_cards} sum is {sum(my_cards)} ")
print (f"computer cards is x,{ dealer_card[0]} ")


a =sum(my_cards)
b= sum(dealer_card)
if a<=21:
	select= input("did you want to show press s or add new card press n ")
	if select == "y":
		print (f"computer cards is{ dealer_card} sum is {sum(dealer_card)} ")
		if b<=21 and b>a and b>17:
			print ("you loss")
		elif b<17:
			dealer_card.append(random.choice(cards))
			print (dealer_cards)
	if select == "n":
		my_cards.append(random.choice(cards))
		print (my_cards)

