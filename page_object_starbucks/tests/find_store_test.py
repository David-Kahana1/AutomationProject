from page_object_starbucks.pages.find_a_store_page import findAStorePage
from page_object_starbucks.pages.home_page import homePage


class TestFindStore():


    def test_search_a_store(self, setup_starbucks):
        print("Test Search a Store Start")
        page = setup_starbucks
        home_page = homePage(page)
        home_page.go_to_find_a_store()
        find_page = findAStorePage(page)
        find_page.search_location("California, USA")
        assert page.url !="https://www.starbucks.com/","the URL not correct"


    def test_no_store_in_the_area(self,setup_starbucks):
        print("Test No Store In The Area Start")
        page = setup_starbucks
        home_page = homePage(page)
        find_page = findAStorePage(page)
        home_page.go_to_find_a_store()
        find_page.search_location("Israel")
        no_result_text = find_page.search_store_with_no_result()
        assert no_result_text == "Zoomed out too farTry searching for a location or zooming in to see results.", "the search was failed"


    def test_take_opening_times(self, setup_starbucks):
        print("Test Take Opening Times Start")
        page = setup_starbucks
        home_page = homePage(page)
        find_page = findAStorePage(page)
        home_page.go_to_find_a_store()
        find_page.search_location("North Carolina, USA")
        open_today = find_page.get_store_opening_times()
        assert open_today == "Open today from 6:00 AM - 8:00 PM" ,"The opening times not true"


    def test_go_to_the_menu(self, setup_starbucks):
        print("Test Go To The Menu Start")
        page = setup_starbucks
        home_page = homePage(page)
        home_page.go_to_menu_page()
        assert page.url =="https://www.starbucks.com/menu" , "it's not the URL of the manu"

