import art
print(art.logo)
continue_to_bid = True
name_to_bid = {}
max_bid = float("-inf")
max_name = ""

while continue_to_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    if bid > max_bid:
        max_name = name
        max_bid = bid
    name_to_bid[name] = bid
    ans = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if ans == "no":
        continue_to_bid = False
        print(f'The winner is {max_name} with a bid of ${max_bid}')
    else:
        #clear the screen
        print("\n" * 1000)