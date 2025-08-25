

class menuPage():

    def __init__(self,page):
        print("Into init")
        self.page = page


    def take_order_e2e(self):
        print("Start Take Order E2E")
        hot_coffe_button = self.page.locator("[class='block linkOverlay__primary'][href='/menu/drinks/hot-coffee']")
        hot_coffe_button.click()
        cappuccino_button = self.page.locator("[href='/menu/product/409/hot']")
        cappuccino_button.click()
        cup_size = self.page.locator("[class='cursor-pointer mx4 my2 tall-hot___cRf4N sizeImage___W8FSt']")
        cup_size.click()
        add_to_order = self.page.get_by_role("button", name="Add to Order ")
        add_to_order.click()
        pickup_button = self.page.locator("[href='/menu/store-locator']")
        pickup_button.click()
        pickup_button.click() # Need 2 clicks on this button.


    def get_drink_name(self, drink_name):
        print("Start Get Drink Name")
        drink_button = self.page.locator(f"[class='block linkOverlay__primary'][href='{drink_name}']")
        drink_button.click()
        name_of_the_drink = self.page.locator("[class='breadcrumbs___q8Ll7  mb2 color-textBlackSoft']")
        type_text = name_of_the_drink.text_content()
        len_type = len(type_text)
        index_type = type_text.index("/")
        type_name = type_text [index_type+1 : len_type]
        print(f"The type of the drink is:{type_name}")
        return self.page.url


