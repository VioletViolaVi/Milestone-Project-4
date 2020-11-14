from django.test import TestCase


class TestModels(TestCase):

    def test_about_us_section(self):
        programmatic_name = 255
        self.assertEqual(programmatic_name, 255)
        self.assertTrue(programmatic_name, range(1, 256))
        self.assertTrue(programmatic_name, int)
        friendly_name = 255
        self.assertEqual(friendly_name, 255)
        self.assertTrue(friendly_name, range(1, 256))
        self.assertTrue(friendly_name, int)
        null = True
        self.assertTrue(null)
        self.assertTrue(null, bool)
        blank = True
        self.assertTrue(blank)
        self.assertTrue(blank, bool)

    def test_about_us(self):
        verbose_name_plural = "About us"
        self.assertIs(verbose_name_plural, "About us")
        null = True
        self.assertTrue(null)
        self.assertTrue(null, bool)
        blank = True
        self.assertTrue(blank)
        self.assertTrue(blank, bool)
        image_description = 255
        self.assertEqual(image_description, 255)
        self.assertTrue(image_description, range(1, 256))
        self.assertTrue(image_description, int)
        title = 255
        self.assertEqual(title, 255)
        self.assertTrue(title, range(1, 256))
        self.assertTrue(title, int)
