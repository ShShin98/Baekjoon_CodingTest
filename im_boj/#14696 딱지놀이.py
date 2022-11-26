n = int(input())

for _ in range(n):
    cards = []

    for i in range(2):
        arr = list(map(int, input().split()))
        cards.append(arr[1:])
    
    if cards[0].count(4) == cards[1].count(4):
        if cards[0].count(3) == cards[1].count(3):
            if cards[0].count(2) == cards[1].count(2):
                if cards[0].count(1) == cards[1].count(1):
                    print("D")
                elif cards[0].count(1) > cards[1].count(1):
                    print("A")
                else:
                    print("B")    
            elif cards[0].count(2) > cards[1].count(2):
                print("A")
            else:
                print("B")
        elif cards[0].count(3) > cards[1].count(3):
            print("A")
        else:
            print("B")
    elif cards[0].count(4) > cards[1].count(4):
        print("A")
    else:
        print("B")