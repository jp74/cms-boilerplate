from django.test import TestCase


class FooBar(object):
    name = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class FooBarTestCase(TestCase):
    def test_set_name(self):
        name = 'Fred'
        foo = FooBar()
        foo.set_name(name)

        self.assertEqual(foo.get_name(), name)
