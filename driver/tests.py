from django.test import TestCase
from .models import Driver,Car,Pickup_Location,Destination


class CarTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016',phone='0735831632')
        self.user.save()

        self.car=Car(car_user=self.user,car_photo='/rider',brand='Nissan',num_plate='KAC9337',num_of_seats='8')


    def test_instance(self):
        self.assertTrue(isinstance(self.brand,Car))

    def test_save_method(self):
        self.brand.save_brand()
        car =Car.objects.all()
        self.assertTrue(len(brand) > 0)


    def test_delete_car(self):
        self.car.save_car()
        self.car.delete_car()
        car = Car.objects.all()
        self.assertTrue(len(brand) == 0)

    def tearDown(self):
        Car.objects.all().delete()


class Pickup_LocationTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016',phone='0735831632')
        self.user.save()

        self.pickup_location=Pickup_Location(pointer=self.user,name='lulu',longitude='-1.499508',latitude='36.098654',geom='POINT(-96.1 45.2)')


    def test_instance(self):
        self.assertTrue(isinstance(self.name,Pickup_Location))

    def test_save_method(self):
        self.name.save_name()
        pickup_location =Pickup_Location.objects.all()
        self.assertTrue(len(name) > 0)


    def test_delete_pickup_location(self):
        self.pickup_location.save_pickup_location()
        self.pickup_location.delete_pickup_location()
        pickup_location = Pickup_Location.objects.all()
        self.assertTrue(len(name) == 0)

    def tearDown(self):
        Pickup_Location.objects.all().delete()


class DestinationTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016',phone='0735831632')
        self.user.save()

        self.destination=Destination(driver_place=self.user,place='westlands',pickups='CDB,roundabout,delta')


    def test_instance(self):
        self.assertTrue(isinstance(self.place,Destination))

    def test_save_method(self):
        self.place.save_place()
        destination =Destination.objects.all()
        self.assertTrue(len(place) > 0)


    def test_delete_destination(self):
        self.destination.save_destination()
        self.destination.delete_destination()
        destination = Destination.objects.all()
        self.assertTrue(len(place) == 0)

    def tearDown(self):
        Destination.objects.all().delete()

class DriverTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016',phone='0735831632')
        self.user.save()

        self.driver=Driver(rider_image=
    '/posts',name='lulu',rider_user=self.user,email_confirmed="False",phone='0758493857')


    def test_instance(self):
        self.assertTrue(isinstance(self.username,Driver))

    def test_save_method(self):
        self.username.save_username()
        driver =Driver.objects.all()
        self.assertTrue(len(username) > 0)


    def test_delete_driver(self):
        self.driver.save_driver()
        self.driver.delete_driver()
        driver = Driver.objects.all()
        self.assertTrue(len(username) == 0)

    def tearDown(self):
        Driver.objects.all().delete()
