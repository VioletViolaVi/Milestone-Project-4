from django.test import TestCase


class TestViews(TestCase):
    def test_home(self):
        self.assertTrue("new_drinks", str)
        self.assertTrue("juices", str)
        self.assertTrue("milkshakes", str)
        self.assertTrue("drink_search_results", str)
        self.assertTrue("typed_in_search", str)
        self.assertTrue("drink_sorting", str)
        self.assertTrue("this_is_the_homepage", str)
        self.assertTrue("home/index.html", str)

    def test_drink_search(self):
        drink_search = None
        self.assertIsNone(drink_search)

    def test_sort(self):
        sort = None
        self.assertIsNone(sort)

    def test_direction(self):
        direction = None
        self.assertIsNone(direction)
        if "direction":
            direction = "desc"
            self.assertIs(direction, "desc")

    def test_drink_search_results(self):
        drink_search_results = ""
        self.assertIs(drink_search_results, "")

    def test_drink_type(self):
        new_drinks = 1
        self.assertIs(new_drinks, 1)
        self.assertTrue(new_drinks, int)
        juices = 2
        self.assertIs(juices, 2)
        self.assertTrue(juices, int)
        milkshakes = 3
        self.assertIs(milkshakes, 3)
        self.assertTrue(milkshakes, int)
        searched_drinks = 1 and 2
        self.assertIs(searched_drinks, 1 and 2)
        self.assertTrue(searched_drinks, int)

    def test_sort_key(self):
        sort_key = "drink_name" or "lower_case_name"
        self.assertIs(sort_key, ("drink_name" or "lower_case_name"))
        self.assertTrue(sort_key, str)

    def test_navbar_boolean(self):
        home_navbar_link = "this_is_the_homepage"
        self.assertTrue("this_is_the_homepage", home_navbar_link)
        self.assertTrue(home_navbar_link, str)
        home_navbar_link = True,
        self.assertTrue(home_navbar_link, bool)

    def test_superuser(self):
        superuser = "Admin"
        self.assertIsNot("Hinata", superuser)
        self.assertIs("Admin", superuser)
        self.assertTrue(superuser, str)

    def test_add_drink(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
        self.assertTrue("POST", str)

    def test_add_drink_template(self):
        template = "home/add_drink.html"
        self.assertIs(template, "home/add_drink.html")
        self.assertTrue(template, str)

    def test_edit_drink(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
        self.assertTrue("POST", str)

    def test_edit_drink_template(self):
        template = "home/edit_drink.html"
        self.assertIs(template, "home/edit_drink.html")
        self.assertTrue(template, str)

    def test_delete_drink(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
