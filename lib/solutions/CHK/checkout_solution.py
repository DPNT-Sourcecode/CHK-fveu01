# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
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
            else:
                total_price += 50
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
        else:
            return -1

    return total_price

# assert(checkout("ABCDCBAABCABBAAA") == 505)
# assert(checkout("") == -1)
# assert(checkout("-") == -1)
# assert(checkout("-1") == -1)
# assert(checkout("AABAB") == 175)

