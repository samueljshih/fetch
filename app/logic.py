import math

def calculate_points(receipt):
    points = 0
    points += sum(c.isalnum() for c in receipt.retailer)

    total = float(receipt.total)
    if receipt.total.endswith(".00"):
        points += 50
    if (total * 100) % 25 == 0:
        points += 25

    points += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    if total > 10.00:
        points += 5

    day = int(receipt.purchaseDate.split("-")[2])
    if day % 2 == 1:
        points += 6

    hour = int(receipt.purchaseTime.split(":")[0])
    if hour == 14:
        points += 10

    return points
