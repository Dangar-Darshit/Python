status = input("""<--- Food Delivery Order Status--->
placed
confirmed
preparing
out_for_delivery
delivered
cancelled
Enter status: """).lower()

match status:
    case "placed":
        print("Order Placed Sucessfully")
    case "confirmed":
        print("Your order is Confirmed")
    case "preparing":
        print("Your Order is Preparing")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your Order Is Deliverd")
    case "cancelled":
        print("Your Order Is Cancelled")