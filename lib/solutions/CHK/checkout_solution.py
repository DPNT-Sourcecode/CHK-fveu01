# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    total_price = 0

    e_multipriced_offer_to_stack = 0

    if skus == "":
        return 0
    if skus == "-":
        return -1
    for i, c in enumerate(skus):
        if c == 'A':
            a_count +=1
            if a_count % 3 == 0:
                total_price += 30
            elif a_count % 5 == 0:
                a_count = 0
                total_price += 20
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
        elif c == 'E':
            e_count += 1
            if e_count % 2 == 0:
                if b_count > 0 and b_count % 2 == 0:
                    total_price += 25  # 15 off for B special offer (don't apply B special offer)
                    b_count -= 1
                elif b_count > 0:
                    total_price += 10
                    b_count -= 1
                else:
                    e_multipriced_offer_to_stack += 1
                    total_price += 40
            else:
                total_price += 40
        elif c == 'F':
            f_count += 1
            if f_count % 3 == 0:
                f_count = 0
                pass
            else:
                total_price += 10
            # print(f"f_count: {f_count}, total_price: {total_price}")
        else:
            return -1

    # print(f"e stacked: {e_multipriced_offer_to_stack}")
    # print(f"total price before operating on offer stack: {total_price}")
    # print(f"b_count: {b_count}")

    while(e_multipriced_offer_to_stack > 0 and b_count >= e_multipriced_offer_to_stack):
        if b_count % 2 == 0:
            total_price -= 15
        else:
            total_price -= 30
        b_count -= 1
        e_multipriced_offer_to_stack -= 1



    return total_price

assert(checkout("") == 0)
assert(checkout("-") == -1)
assert(checkout("-1") == -1)
assert(checkout("AABAB") == 175)
assert(checkout("AABABAA") == 245)
assert(checkout("AABABAAE") == 285)
assert(checkout("AABABAAEE") == 310)
assert(checkout("AABAAAEE") == 280)
assert(checkout("AABAAAEED") == 295)

assert(checkout("AAAAAA") == 250)
assert(checkout("AAAAAAA") == 300)
assert(checkout("AAAAAAAAA") == 380)

assert(checkout("EE") == 80)
assert(checkout("EEB") == 80)

assert(checkout("EEEB") == 120)
# print(f'checkout(BEBEEE) is {checkout("BEBEEE")} and should be 160')
assert(checkout("BEBEEE") == 160)
assert(checkout("FFF") == 20)
assert(checkout("FFAAAFAA") == 220)



