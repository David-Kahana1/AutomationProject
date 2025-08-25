

class homePage():

    def __init__(self,page):
        print("Into init")
        self.page = page


    def go_to_find_a_store(self):
        print("Go To Find Page")
        find_button = self.page.get_by_role("link", name="Find a store")
        find_button.click()


    def go_to_menu_page(self):
        print("Go To Manu Page")
        manu_button= self.page.get_by_role("link", name="Menu")
        manu_button.click()


