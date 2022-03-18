import logging
from typing import List

class SpecialOffer:
    def __init__(self, count_cursor: int, incremented_price: int, description: str):
        self.logger = logging.getLogger(__name__)
        self.count_cursor = count_cursor
        self.incremented_price = incremented_price
        self.description = description

class ProductConsumptionContainer:
    def __init__(self, item: str, price: int, special_offers: List[SpecialOffer] = []):
        self.logger = logging.getLogger(__name__)
        self.item = item
        self.price = price
        self.count = 0
        self.special_offers = special_offers

    def get_price(self):
        return self.price

    def set_count(self, count: int):
        self.count = count

    def find_special_offer(self, count_cursor):
        for special_offer in self.special_offers:
            if special_offer.count_cursor == count_cursor:
                return special_offer

        raise Exception("Could not find special offer")

    def get_count(self):
        return self.count

    def increment_count(self):
        assert(self.count > -1)
        self.count = self.count + 1

    def decrement_count(self):
        assert(self.count > 0)
        self.count = self.count - 1

    def get_special_offers(self):
        return self.special_offers

    def get_special_offers_cursors(self):
        return sorted(
            list(
                map(lambda offer: offer.count_cursor, self.special_offers)
            ),
            reverse=True
        )

class Checkout:
    def __init__(self, product_consumption_containers, skus):
        self.logger = logging.getLogger(__name__)
        self.product_consumption_containers = product_consumption_containers
        self.skus = skus
        self.prev_price = 0
        self.total_price = 0

        self.special_case_applied = ""

        self.e_multipriced_offer_to_stack = 0
        self.n_multipriced_offer_to_stack = 0
        self.r_multipriced_offer_to_stack = 0

    def get_product(self, c):
        return self.product_consumption_containers[c]

    def apply_default_price(self, c):
        self.total_price += self.get_product(c).get_price()

    def do_special_offers_apply(self, c):
        applied_special_offer = False
        for i, special_offer_cursor in enumerate(self.get_product(c).get_special_offers_cursors()):
            if self.get_product(c).get_count() % special_offer_cursor == 0:
                special_offer = self.get_product(c).find_special_offer(special_offer_cursor)
                self.total_price += special_offer.incremented_price
                if i == 0:
                    self.get_product(c).set_count(0)
                applied_special_offer = True
                self.special_case_applied = special_offer.description
                break

        if not applied_special_offer:
            self.special_case_applied = ""

        return applied_special_offer

    def print_diff(self, c):
        special_case_out = "" if self.special_case_applied == "" else f", Special case applied: {self.special_case_applied}"
        print(f"Diff: {c}({self.get_product(c).get_count()}) => +{self.total_price - self.prev_price}{special_case_out}")

    def process_item(self, c):
        self.prev_price = self.total_price
        self.get_product(c).increment_count()
        if(self.do_special_offers_apply(c)):
            pass
        else:
            self.apply_default_price(c)

        self.print_diff(c)

    def run(self):
        if self.skus == "":
            return 0
        if self.skus == "-":
            return -1
        for c in self.skus:
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYV":
                return -1

            self.process_item(c)


        return self.total_price

        # while(e_multipriced_offer_to_stack > 0 and counts["B"] >= e_multipriced_offer_to_stack):
        #     if counts["B"] % 2 == 0:
        #         total_price -= 15
        #     else:
        #         total_price -= 30
        #     counts["B"] -= 1
        #     e_multipriced_offer_to_stack -= 1

        # while(n_multipriced_offer_to_stack > 0 and counts["M"] >= n_multipriced_offer_to_stack):
        #     total_price -= 15
        #     counts["M"] -= 1
        #     n_multipriced_offer_to_stack -= 1

        # while(r_multipriced_offer_to_stack > 0 and counts["Q"] >= r_multipriced_offer_to_stack):
        #     if counts["Q"] % 3 == 0:
        #         total_price -= 20
        #         counts["Q"] -= 1
        #     else:
        #         total_price -= 30
        #         counts["Q"] -= 1
        #     r_multipriced_offer_to_stack -= 1





# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(f"TRACE: checkout({skus})")

    product_consumption_containers = {
        "A": ProductConsumptionContainer("A", 50, [SpecialOffer(3, 30, "3A for 130"), SpecialOffer(5, 20, "5A for 200")]),
        "B": ProductConsumptionContainer("B", 30, [SpecialOffer(2, 15, "2B for 45")]),
        "C": ProductConsumptionContainer("C", 20),
        "D": ProductConsumptionContainer("D", 15),
        "E": ProductConsumptionContainer("E", 40),
        "F": ProductConsumptionContainer("F", 10),
        "G": ProductConsumptionContainer("G", 20),
        "H": ProductConsumptionContainer("H", 10),
        "I": ProductConsumptionContainer("I", 35),
        "J": ProductConsumptionContainer("J", 60),
        "K": ProductConsumptionContainer("K", 70),
        "L": ProductConsumptionContainer("L", 90),
        "M": ProductConsumptionContainer("M", 15),
        "N": ProductConsumptionContainer("N", 40),
        "O": ProductConsumptionContainer("O", 10),
        "P": ProductConsumptionContainer("P", 50),
        "Q": ProductConsumptionContainer("Q", 30),
        "R": ProductConsumptionContainer("R", 50),
        "S": ProductConsumptionContainer("S", 20),
        "T": ProductConsumptionContainer("T", 20),
        "U": ProductConsumptionContainer("U", 40),
        "V": ProductConsumptionContainer("V", 50),
        "W": ProductConsumptionContainer("W", 20),
        "X": ProductConsumptionContainer("X", 17),
        "Y": ProductConsumptionContainer("Y", 20),
        "Z": ProductConsumptionContainer("Z", 21),
    }
    checkout_ = Checkout(product_consumption_containers, skus)
    return checkout_.run()

assert(checkout("") == 0)
assert(checkout("-") == -1)
assert(checkout("-1") == -1)
assert(checkout("A") == 50)
assert(checkout("AAA") == 130)
assert(checkout("AAAAA") == 200)
assert(checkout("AAAAABB") == 245)
# assert(checkout("AABAB") == 175)
# assert(checkout("AABABAA") == 245)
# assert(checkout("AABABAAE") == 285)
# assert(checkout("AABABAAEE") == 310)
# assert(checkout("AABAAAEE") == 280)
# assert(checkout("AABAAAEED") == 295)
# assert(checkout("AAAAAA") == 250)
# assert(checkout("AAAAAAA") == 300)
# assert(checkout("AAAAAAAAA") == 380)
# assert(checkout("EE") == 80)
# assert(checkout("EEB") == 80)
# assert(checkout("EEEB") == 120)
# assert(checkout("BEBEEE") == 160)
# assert(checkout("FFF") == 20)
# assert(checkout("FFAAAFAA") == 220)
# assert(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 50 + 30 + 20 + 15 + 40 + 10 + 20 + 10 + 35 + 60 + 80 + 90 + 15 + 40 + 10 + 50 + 30 + 50 + 30 + 20 + 40 + 50 + 20 + 90 + 10 + 50)
# assert(checkout("UUU") == 120)
# assert(checkout("RRRQ") == 150)
# assert(checkout("RRRRQ") == 200)
# assert(checkout("VV") == 90)
# assert(checkout("VVV") == 130)
# assert(checkout("VVVV") == 180)
# assert(checkout("NNN") == 120)
# assert(checkout("PPPPQRUVPQRUVPQRUVSU") == 740)
