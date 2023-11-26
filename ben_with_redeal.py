import random

from redeal import *

maxium_small_cards = 8
all_cards = "23456789TJQKA"


def replace_small_cards(suit, available_cards):
    suit = list(suit)
    for i, card in enumerate(suit):
        if card == "x":
            random_card = random.choice(available_cards)
            suit[i] = random_card
            available_cards.remove(random_card)
    return "".join(suit)


def process_input(sample):
    all_small_cards = [
        [str(i) for i in range(2, maxium_small_cards)] for _ in range(4)
    ]
    hands = sample.split()

    all_result = []
    cards = [""] * 4
    fourth_hand = [""] * 4
    print(cards)
    for i in range(len(hands)):
        suits = hands[i].split(".")
        new_hands = []

        for index, suit in enumerate(suits):
            new_suit = replace_small_cards(suit, all_small_cards[index])
            cards[index] = cards[index] + new_suit
            new_hands.append(new_suit)
        all_result.append(" ".join(new_hands))
    print(cards)

    for i in range(4):
        for card in all_cards:
            if card not in cards[i]:
                fourth_hand[i] = fourth_hand[i] + card
    all_result.append(" ".join(fourth_hand))

    # return " ".join(result)
    return dict(zip("NESW", all_result))


# Call the function with the corrected sample input
result = process_input("QTxx.J8x.9x.Q9xx 9xxx.AKT.J8xx.8x AK.Qxxx.ATxx.ATx")

predeal = result
# predeal = {"N": "QT67 J82 95 Q972", "E": "9532 AKT J873 83", "S": "AK Q543 AT42 AT5", "W": "J84 976 KQ6 KJ64"}
print(predeal)
dealer = Deal.prepare(predeal)
deal = dealer()
Deal.set_str_style("long")
print(deal)
