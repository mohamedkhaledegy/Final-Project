import psutil

addrs = psutil.net_if_addrs()
cards = addrs.keys()
list_cards = []
for card in cards:
    print(card)
    list_cards.append(card)
