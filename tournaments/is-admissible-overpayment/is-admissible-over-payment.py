def isAdmissibleOverpayment(P, N, X):
    t = 0
    for p, n in zip(P, N):
        d = 0
        s = n.split('%')
        if s[1:]:
            d = float(s[0]) / 100
            if 'lo' in n:
                d *= -1
        d += 1
        t += round(p - p / d, 8);
    return t <= X


# notes = ["20.00% lower than in-store",  "10.00% higher than in-store"]
# prices = [48, 165]
# x = 2

prices = [110, 95, 70]
notes = ["10.0% higher than in-store", "5.0% lower than in-store", "Same as in-store"]
x = 5
# prices = [40, 40, 40, 40]
# notes = ["0.001% higher than in-store", "0.0% lower than in-store", "0.0% higher than in-store", "0.0% lower than in-store"]
# x = 0
print(isAdmissibleOverpayment(prices, notes, x))