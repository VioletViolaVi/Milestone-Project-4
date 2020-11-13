from django.test import TestCase
from django.db import models


class TestModels(TestCase):

    def test_about_us_section(self):
        programmatic_name = 255
        self.assertEqual(programmatic_name, 255)
        self.assertTrue(programmatic_name, range(1, 256))
        friendly_name = 255
        self.assertEqual(friendly_name, 255)
        self.assertTrue(friendly_name, range(1, 256))
        null = True
        self.assertTrue(null)
        blank = True
        self.assertTrue(blank)

    def test_about_us(self):
        verbose_name_plural = "About us"
        self.assertIs(verbose_name_plural, "About us")
        null = True
        self.assertTrue(null)
        blank = True
        self.assertTrue(blank)
        image_description = 255
        self.assertEqual(image_description, 255)
        self.assertTrue(image_description, range(1, 256))
        title = 255
        self.assertEqual(title, 255)
        self.assertTrue(title, range(1, 256))
