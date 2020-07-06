# from lab.hotel_rooms.project.hotel import Hotel
# from lab.hotel_rooms.project.room import Room
#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()

from lab.hotel_rooms.project.hotel import Hotel
from lab.hotel_rooms.project.room import Room

hotel = Hotel('asd')

room = Room(1, 3)
hotel.add_room(room)
hotel.take_room(1, 3)
hotel.print_status()