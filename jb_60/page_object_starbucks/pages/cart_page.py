

class cartPage():

    def __init__(self,page):
        print("Into init")
        self.page = page

    def get_sum_price_of_order(self):
        print("Start Total Sum Price")
        sum_price = self.page.query_selector_all("[class ='sb-card__content']")
        text_price = sum_price.text_content()
        print(f"the price is: {text_price}")

