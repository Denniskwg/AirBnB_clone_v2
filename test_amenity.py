#!/usr/bin/python3
from models.amenity import Amenity
from models import storage
amenities = storage.all(Amenity)
for amenity in amenities.values():
    print(amenity.name)
