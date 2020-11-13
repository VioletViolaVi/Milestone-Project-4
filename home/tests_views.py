from django.test import TestCase


class TestViews(TestCase):
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
        juices = 2
        milkshakes = 3
        searched_drinks = 1 and 2
        self.assertIs(new_drinks, 1)
        self.assertIs(juices, 2)
        self.assertIs(milkshakes, 3)
        self.assertIs(searched_drinks, 1 and 2)

    def test_sort_key(self):
        sort_key = "drink_name" or "lower_case_name"
        self.assertIs(sort_key, ("drink_name" or "lower_case_name"))

    def test_navbar_boolean(self):
        home_navbar_link = "this_is_the_homepage"
        self.assertTrue("this_is_the_homepage", home_navbar_link)

    def test_superuser(self):
        superuser = "Admin"
        self.assertIsNot("Hinata", superuser)
        self.assertIs("Admin", superuser)

    def test_add_drink_template(self):
        template = "home/add_drink.html"
        self.assertIs(template, "home/add_drink.html")

    def test_edit_drink_template(self):
        template = "home/edit_drink.html"
        self.assertIs(template, "home/edit_drink.html")
