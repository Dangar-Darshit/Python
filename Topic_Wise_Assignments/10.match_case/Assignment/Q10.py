method = input("""<--- Payment Method--->
upi
card
cash
wallet
Enter Payment Method: """).lower()

match method:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("Card Payment Selected")
    case "cash":
        print("Cash Payment Selected")
    case "wallet":
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method Selected")