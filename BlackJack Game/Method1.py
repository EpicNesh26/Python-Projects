import random 

# Method 1
# This is one method of doing it but it will not tell us which card we have got only the rank and its value 
cards = []
suits = ["Spades","clubs","hearts","diamonds"]
ranks = ["A" , "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

random.shuffle(cards)


def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []

    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt = deal(4)
card = cards_dealt[0]

rank = card[1]

if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank 

rank_dict = {"rank":rank, "value" :value}

print(rank_dict["rank"] , rank_dict["value"])