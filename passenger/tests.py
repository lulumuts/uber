from django.test import TestCase
from .models import Passenger


class PassengerTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016',phone='0735831632')
        self.user.save()

        self.passenger=Passenger(rider_image=
    '/posts',name='lulu',rider_user=self.user,email_confirmed="False",phone='0758493857')


    def test_instance(self):
        self.assertTrue(isinstance(self.username,Passenger))

    def test_save_method(self):
        self.username.save_username()
        passenger =Passenger.objects.all()
        self.assertTrue(len(username) > 0)


    def test_delete_passenger(self):
        self.passenger.save_passenger()
        self.passenger.delete_passenger()
        passenger = Passenger.objects.all()
        self.assertTrue(len(username) == 0)

    def tearDown(self):
        Passenger.objects.all().delete()
