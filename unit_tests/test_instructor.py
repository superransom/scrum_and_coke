# created by Jeff

from classes.Instructor import Instructor
from unittest import TestCase


class TestInstructor(TestCase):

    def setup(self):
        self.instructor1 = Instructor("instructor1@uwm.edu", "DEFAULT_PASSWORD")
        # fake TA
        self.ta1 = ("ta1@uwm.edu", "DEFAULT_PASSWORD")
        # fake Course
        self.course1 = ("DEFAULT_ID", 101, self.instructor1, [])

    def test___init__(self):
        self.assertEquals(self.instructor1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.instructor1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.name, "DEFAULT")
        self.assertEquals(self.instructor1.phone_number, "DEFAULT")

    def test_edit_contact(self):
        # still using instructor1
        self.instructor1.edit_contact_info("name", "Bob Ross")
        self.assertNotEquals(self.instructor1.name, "DEFAULT")
        self.assertEquals(self.instructor1.name, "Bob Ross")

        self.instructor1.edit_contact_info("phone", "4145459999")
        self.assertNotEquals(self.instructor1.phone_number, "0000000000")
        self.assertEquals(self.instructor1.phone_number, "4145459999")

        self.instructor1.edit_contact_info("email", "bob_ross@uwm.edu")
        self.assertNotEquals(self.instructor1.email, "instructor1@uwm.edu")
        self.assertEquals(self.instructor1.email, "bob_ross@uwm.edu")

        with self.assertRaises(TypeError):
            self.instructor1.edit_contact_info(2, "Ted")

        with self.assertRaises(TypeError):
            self.instructor1.edit_contact_info("name", 41.6)

    def test_read_public_contact(self):
        self.assertNotEquals(self.instructor1.read_public_contact())
        self.assertEquals(self.instructor1.read_public_contact(), "Bob Ross, bob_ross@uwm.edu")


    def test_send_notification_ta(self):
        self.assertTrue(self.instructor1.send_notification_ta("DEFAULT_TA_EMAIL", "Hi!"))
        self.assertFalse(self.instructor1.send_notification_ta("ROAR", "Woof!"))

    def test_view_course(self):
        self.assertEquals(self.instructor1.view_course_assign(), "DEFAULT_ID - 101")

    def test_view_ta_assign(self):
        self.assertEquals(self.instructor1.view_ta_assign()[0], self.ta1)
