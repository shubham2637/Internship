WL5, c = ['W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W','W','L','L','W','L','W','W','W','W','L','W','L','W'] , 0
for i in range(len(WL5)):
    t = WL5[i:i+5]
    if t.count("W") >= 3:
        print(t)
        c = c + 1
print(f"Total of {c} wins.")
#WL5,c = ["W","L","L","W","L","W","W","W","W","L","W","L","W"] , 0
