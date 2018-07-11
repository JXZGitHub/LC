from collections import defaultdict
def enoughChange(bills):
    """
    A seller of apples sells each apple at 5 dollars, and only accepts bills in 5,10,20 dollar denominations.
    A list of customers line up to buy apples, each buying only one apple.
    For each transaction, each customer will pay in 5,10,or 20 dollar bills, the seller will accept the payment
    if there's enough change to give back to the customer.

    The seller starts with 0 change.

    Given an array of integers representing the bill denomination paid by each customer, determine whether it's possible
    for the seller to accept all transactions with sufficient change.

    Example: Given [5,5,5], return True, because all 3 transactions can go through without the need for change.
    Given [5,5,10] return True, because the last transaction can go through by giving a single $5 received previously as change
    Given [10,5,5] return False, because there's not enough change for the first $10.
    Given [5,5,5,5,20,20] return False, because there's not enough change for the last $20.

    :param bills:
    :return: boolean
    """

    received = defaultdict(int)
    for b in bills:
        if b == 10: #Check if there's at least one 5 dollar bill
            if received.get(5):
                received[5] -= 1
                received[10] += 1
            else:
                return False #Not enough change!
        elif b == 20: #Check if there's either at least one 5 + one 10, or three 5's, in that order.
            if received.get(5) and received.get(10):
                received[5] -=1
                received[10] -=1
                received[20] += 1
            elif received.get(5) >= 3:
                received[5] -= 3
                received[20] +=1
            else:
                return False #Not enough change!
        else: #No change needed
            received[5] +=1
    return True

print (enoughChange([5,5,5,5,20,20]))
print (enoughChange([5,5,5,5,10,20,20]))
print (enoughChange([10,5,5]))
print (enoughChange([5,5,10]))
print (enoughChange([5,5,5]))

