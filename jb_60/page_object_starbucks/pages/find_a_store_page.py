import time


class findAStorePage():

    def __init__(self,page):
        print("Into init")
        self.page = page


    def search_location(self, location_text):
        print("Start Find a Store")
        search = self.page.locator("[name='place']")
        search.click()
        search.clear()
        search.fill(location_text)
        self.page.keyboard.press('Enter')


    def search_store_with_no_result(self):
        print("Start No Result")
        no_result = self.page.locator("[class='flex-shrink-none flex-grow']")
        no_result_text = no_result.text_content()
        print(no_result_text)
        return no_result_text


    def order_here_button(self):
        print("Start Order Button")
        order_button = self.page.get_by_role("button", name="Order Here")
        order_button.click() #This button not work in automation test


    def get_store_opening_times(self):
        print("Start Store Opening Times")
        info = self.page.get_by_role("button", name="Store details for Harris Teeter Chapel Hill 137")
        info.click()
        opening_times = self.page.locator("[class='px4 lg-px6 pt4 pb5']")
        opening_times_text = opening_times.text_content()
        open_today_index = opening_times_text.index('PM')
        open_today_text = opening_times_text [0:open_today_index+2]
        print(open_today_text)
        return open_today_text


