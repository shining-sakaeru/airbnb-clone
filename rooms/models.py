from django.db import models
from django.db.models import manager
from django.db.models.deletion import SET_NULL
from django.db.models.fields import files
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models
import users

# 0 import 가장먼저 (ex, import os)
# 1 django 관련 모든 pkg import
# 2 외부 pkg import
# 3 내 pkg import


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        # ordering = ["name"]    # created, name ..


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="rooms_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE)
    # user 와 room 연결. host는 user 이기도 하기때문
    # ForeignKey : many-to-on (host 1명 - room 10개 예약)
    # user_models.User, on_delete=models.CASCADE : user 삭제시 아랫것(rooms)도 함께 삭제
    room_type = models.ForeignKey("RoomType", related_name="rooms", on_delete=SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilies = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)