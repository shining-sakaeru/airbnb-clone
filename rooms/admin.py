from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse"),  # 접었다 폈다
                "fields": ("amenities", "facilies", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    # ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilies",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")

    # filter_horizontal : many-to-many Only
    filter_horizontal = ("amenities", "facilies", "house_rules")

    def count_amenities(self, obj):  # obj = 객실
        print(obj.amenities.all())
        return "Potato"

    count_amenities.short_description = "hello there!"  # 클릭 안되게


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
