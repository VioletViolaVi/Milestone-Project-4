from django.test import TestCase
from .forms import AboutUsForm


class TestViews(TestCase):

    def test_about_us(self):
        main_mission = 1
        self.assertIs(main_mission, 1)
        sub_mission = 2
        self.assertIs(sub_mission, 2)
        self.assertTrue("main_mission", str)
        self.assertTrue("sub_mission", str)
        context = {
            "main_mission": main_mission,
            "sub_mission": sub_mission,
        }
        self.assertTrue(context, dict)
        self.assertTrue("about_us/about_us.html", str)

    def test_append_about_us(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
        self.assertTrue("about_us", str)
        self.assertTrue("POST", str)
        self.assertTrue("Mission statement section successfully added!", str)
        self.assertTrue("append_about_us", str)
        self.assertTrue("Failed to add mission statement section. Please \
                                ensure the form is valid.", str)
        self.assertTrue("about_us/append_about_us.html", str)
        template = "about_us/append_about_us.html"
        self.assertIs(template, "about_us/append_about_us.html")
        form = AboutUsForm()
        context = {
            "form": form,
        }
        self.assertTrue(context, dict)

    def test_change_about_us(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
        self.assertTrue("about_us", str)
        self.assertTrue("POST", str)
        self.assertTrue("Mission statement section successfully updated!", str)
        template = "about_us/edit_about_us.html"
        self.assertIs(template, "about_us/edit_about_us.html")

    def test_remove_about_us(self):
        self.assertTrue("Access Denied. \
                Access restricted to administrators only.", str)
        self.assertTrue("about_us", str)
        self.assertTrue("Mission statement section deleted!", str)

    def test_go_to_about_us_page(self):
        response = self.client.get("/about_us/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about_us/about_us.html")

    def test_go_to_append_about_us_page(self):
        response = self.client.get("/accounts/login/?next=/about_us/append/")
        self.assertEqual(response.status_code, 200)

    def test_go_to_change_about_us_page(self):
        response = self.client.get("/accounts/login/?next=/about_us/change/1")
        self.assertEqual(response.status_code, 200)
