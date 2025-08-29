from page_object_starbucks.pages.cart_page import cartPage
from page_object_starbucks.pages.find_a_store_page import findAStorePage
from page_object_starbucks.pages.home_page import homePage
from page_object_starbucks.pages.menu_page import menuPage


class TestGetOrder():


    def test_take_order_end_to_end(self,setup_starbucks):
        print("Test Take Order End-to-End Start")
        page = setup_starbucks
        home_page = homePage(page)
        menu_page = menuPage(page)
        find_page = findAStorePage(page)
        cart_page = cartPage(page)
        home_page.go_to_menu_page()
        menu_page.take_order_e2e()
        find_page.search_location("New York, NY, USA")
        find_page.press_on_order_here_button()
        # In automation test have a failure (bug) here. can't press on 'Order Here'.
        cart_page.get_sum_price_of_order()
        assert page.url == "https://www.starbucks.com/menu/cart","The order failed"


    def test_get_cold_coffee(self,setup_starbucks):
        print("Test Get Cold Coffee Start")
        page = setup_starbucks
        home_page = homePage(page)
        menu_page = menuPage(page)
        home_page.go_to_menu_page()
        menu_page.get_drink_name('/menu/drinks/cold-coffee')
        assert page.url == "https://www.starbucks.com/menu/drinks/cold-coffee","don't found cold coffee"


    def test_get_hot_tea(self,setup_starbucks):
        print("Test Get Hot Tea Start")
        page = setup_starbucks
        home_page = homePage(page)
        menu_page = menuPage(page)
        home_page.go_to_menu_page()
        menu_page.get_drink_name('/menu/drinks/hot-tea')
        assert page.url == "https://www.starbucks.com/menu/drinks/hot-tea","don't found hot tea"


    def test_get_hot_chocolate(self,setup_starbucks):
        print("Test Get Hot Chocolate Start")
        page = setup_starbucks
        home_page = homePage(page)
        menu_page = menuPage(page)
        home_page.go_to_menu_page()
        menu_page.get_drink_name('/menu/drinks/hot-chocolate-lemonade-more')
        assert page.url == "https://www.starbucks.com/menu/drinks/hot-chocolate-lemonade-more","don't found hot chocolate"