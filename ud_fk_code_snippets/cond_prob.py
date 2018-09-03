from numpy import random

# random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])

    # purchaseProbability = float(ageDecade) / 100.0
    purchaseProbability = random.random()
    totals[ageDecade] += 1

    if random.random() < purchaseProbability:
        totalPurchases += 1
        purchases[ageDecade] += 1

print(totals)
print(purchases)
print(totalPurchases)


# p(purchase/30s)
prob_ef = float(purchases[30])/float(totals[30])
print(prob_ef)

# p(30)
p_30 = float(totals[30])/100000.0

# p(purchase)
p_purchase = float(totalPurchases)/100000.0

# p(30)p(purchase)
print(p_30*p_purchase)

# p(30, purchase)
print(float(purchases[30])/100000.0)

# p(e/f) = p(e,f)/p(f) p(e) - prob of buying something regardless af age
# p(f) - just the probability of being 30 in the dataset
print((float(purchases[30])/100000.0)/(float(totals[30])/100000.0))
