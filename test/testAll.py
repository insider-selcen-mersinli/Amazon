from Amazon.test.baseTest import BaseTest


class TestAmazon(BaseTest):

    def test(self):
        self.assertTrue(self.home.homepage_banner_is_displayed(), "Wrong page")

        self.home.click_signin_page()
        self.login.login("selcenfethiyemersinli@gmail.com", "4518205eM*")

        self.home.search_product("Samsung")

        self.assertEqual(self.category.get_search_keyword(), "Samsung", "Search failed")

        self.category.select_page()
        self.assertEqual(self.category.get_page_number(), "2", "Could not switch page")

        self.category.select_product()

        product_name = self.product.get_product_name()

        self.product.add_to_wishlist()

        self.assertEqual(product_name, self.wishlist.get_product_name(), "The product is not on the list")

        self.wishlist.delete_product_from_wishlist()

        self.assertTrue(self.wishlist.delete_product_button_is_displayed(), "The product could not be deleted")
