# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    total_price = 0
    if skus == "":
        return 0
    if skus == "-":
        return -1
    for c in skus:
        if c == 'A':
            a_count +=1
            if a_count % 3 == 0:
                total_price += 30
            elif a_count % 5 == 0:
                a_count = 0
                total_price += 20
            else:
                total_price += 50
            print(f"a count: {a_count}, total_price: {total_price}")
        elif c == 'B':
            b_count +=1
            if b_count % 2 == 0:
                total_price += 15
            else:
                total_price += 30
        elif c == 'C':
            c_count +=1
            total_price += 20
        elif c == 'D':
            d_count +=1
            total_price += 15
        elif c == 'E':
            e_count += 1
            if e_count % 2 == 0:
                if b_count % 2 == 0:
                    total_price += 25  # 15 off for B special offer (don't apply B special offer)
                elif b_count > 0:
                    total_price += 10
                else:
                    total_price += 40
            else:
                total_price += 40
        else:
            return -1

    return total_price

# assert(checkout("") == 0)
# assert(checkout("-") == -1)
# assert(checkout("-1") == -1)
# assert(checkout("AABAB") == 175)
# assert(checkout("AABABAA") == 245)
# assert(checkout("AABABAAE") == 285)
# assert(checkout("AABABAAEE") == 310)
# assert(checkout("AABAAAEE") == 280)
# assert(checkout("AABAAAEED") == 295)

print(checkout("AAAAAA"))
#assert(checkout("AAAAAA") == 250)


