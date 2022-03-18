# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(f"TRACE: checkout({skus})")
    counts = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }

    total_price = 0
    prev_price = 0

    special_case_applied = ""

    e_multipriced_offer_to_stack = 0
    n_multipriced_offer_to_stack = 0
    r_multipriced_offer_to_stack = 0

    if skus == "":
        return 0
    if skus == "-":
        return -1
    for i, c in enumerate(skus):
        if c == 'A':
            counts[c] +=1
            if counts[c] % 3 == 0:
                total_price += 30
            elif counts[c] % 5 == 0:
                counts[c] = 0
                total_price += 20
            else:
                total_price += 50
        elif c == 'B':
            counts[c] +=1
            if counts[c] % 2 == 0:
                total_price += 15
            else:
                total_price += 30
        elif c == 'C':
            counts[c] +=1
            total_price += 20
        elif c == 'D':
            counts[c] +=1
            total_price += 15
        elif c == 'E':
            counts[c] += 1
            if counts[c] % 2 == 0:
                if counts["B"] > 0 and counts["B"] % 2 == 0:
                    total_price += 25  # 15 off for B special offer (don't apply B special offer)
                    counts["B"] -= 1
                elif counts["B"] > 0:
                    total_price += 10
                    counts["B"] -= 1
                else:
                    e_multipriced_offer_to_stack += 1
                    total_price += 40
            else:
                total_price += 40
        elif c == 'F':
            counts[c] += 1
            if counts[c] % 3 == 0:
                counts[c] = 0
                pass
            else:
                total_price += 10
        elif c == 'G':
            counts[c] += 1
            total_price += 20
        elif c == 'H':
            counts[c] += 1
            if counts[c] > 1 and counts[c] % 10 == 0:
                total_price -= 5
                counts[c] = 0
            elif counts[c] % 5 == 0:
                total_price += 5
            else:
                total_price += 10
        elif c == 'I':
            counts[c] += 1
            total_price += 35
        elif c == 'J':
            counts[c] += 1
            total_price += 60
        elif c == 'K':
            counts[c] += 1
            if counts[c] % 2 == 0:
                total_price += 70
                counts[c] = 0
            else:
                total_price += 80
        elif c == 'L':
            counts[c] += 1
            total_price += 90
        elif c == 'M':
            counts[c] += 1
            total_price += 15
        elif c == 'N':
            counts[c] += 1
            if counts[c] % 3 == 0:
                if counts["M"] > 0:
                    counts["M"] -= 1
                    total_price += 25
                else:
                    n_multipriced_offer_to_stack += 1
                    total_price += 40
            else:
                total_price += 40
        elif c == 'O':
            counts[c] += 1
            total_price += 10
        elif c == 'P':
            counts[c] += 1
            if counts[c] % 5 == 0:
                counts[c] = 0
                special_case_applied = "Applied 5P for 200"
                pass
            else:
                total_price += 50
        elif c == 'Q':
            counts[c] += 1
            if counts[c] % 3 == 0:
                special_case_applied = "Applied 3Q for 80"
                total_price += 20
                pass
            else:
                total_price += 30
        elif c == 'R':
            counts[c] += 1
            if counts[c] % 3 == 0:
                if counts["Q"] > 0:
                    if counts["Q"] % 3 == 0:
                        total_price += 30
                    else:
                        total_price += 20
                    counts["Q"] -= 1
                    special_case_applied = "Applied 3R get one Q free"
                else:
                    total_price += 50
                    r_multipriced_offer_to_stack += 1
            else:
                total_price += 50
        elif c == 'S':
            counts[c] += 1
            total_price += 30
        elif c == 'T':
            counts[c] += 1
            total_price += 20
        elif c == 'U':
            counts[c] += 1
            if counts[c] % 4 == 0:
                counts[c] = 0
                special_case_applied = "Applied 3U get one U free"
                pass
            else:
                total_price += 40
        elif c == 'V':
            counts[c] += 1
            if counts[c] % 2 == 0:
                total_price += 40
                special_case_applied = "Applied 2V for 90"
            elif counts[c] % 3 == 0:
                counts[c] = 0
                total_price += 40
                special_case_applied = "Applied 3V for 130"
            else:
                total_price += 50
        elif c == 'W':
            counts[c] += 1
            total_price += 20
        elif c == 'X':
            counts[c] += 1
            total_price += 90
        elif c == 'Y':
            counts[c] += 1
            total_price += 10
        elif c == 'Z':
            counts[c] += 1
            total_price += 50
        else:
            return -1

        special_case_out = "" if special_case_applied == "" else f"special case: {special_case_applied}"
        print(f"c: {c}({counts[c]}) => +{total_price - prev_price}, {special_case_out}")
        prev_price = total_price
        special_case_applied = ""
        #print(f"e stacked: {e_multipriced_offer_to_stack}")
        #print(f"n stacked: {n_multipriced_offer_to_stack}")
        #print(f"r stacked: {r_multipriced_offer_to_stack}")

    # print(f"e stacked: {e_multipriced_offer_to_stack}")
    #print(f"n stacked: {n_multipriced_offer_to_stack}")
    # print(f"r stacked: {r_multipriced_offer_to_stack}")
    # print(f"total price before operating on offer stack: {total_price}")
    # print(f"b_count: {b_count}")

    while(e_multipriced_offer_to_stack > 0 and counts["B"] >= e_multipriced_offer_to_stack):
        if counts["B"] % 2 == 0:
            total_price -= 15
        else:
            total_price -= 30
        counts["B"] -= 1
        e_multipriced_offer_to_stack -= 1

    while(n_multipriced_offer_to_stack > 0 and counts["M"] >= n_multipriced_offer_to_stack):
        total_price -= 15
        counts["M"] -= 1
        n_multipriced_offer_to_stack -= 1

    while(r_multipriced_offer_to_stack > 0 and counts["Q"] >= r_multipriced_offer_to_stack):
        if counts["Q"] % 3 == 0:
            total_price -= 20
            counts["Q"] -= 1
        else:
            total_price -= 30
            counts["Q"] -= 1
        r_multipriced_offer_to_stack -= 1

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
assert(checkout("BEBEEE") == 160)
assert(checkout("FFF") == 20)
assert(checkout("FFAAAFAA") == 220)
assert(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 50 + 30 + 20 + 15 + 40 + 10 + 20 + 10 + 35 + 60 + 80 + 90 + 15 + 40 + 10 + 50 + 30 + 50 + 30 + 20 + 40 + 50 + 20 + 90 + 10 + 50)
assert(checkout("UUU") == 120)
assert(checkout("RRRQ") == 150)
assert(checkout("RRRRQ") == 200)
assert(checkout("VV") == 90)
assert(checkout("VVV") == 130)
assert(checkout("VVVV") == 180)
assert(checkout("NNN") == 120)
assert(checkout("PPPPQRUVPQRUVPQRUVSU") == 740)
