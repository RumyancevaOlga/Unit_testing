from random import choice


class HotelService:

    def is_room_available(self, room_id: int) -> bool:
        return choice([True, False])


class BookingService:

    def __init__(self, hotel_service: HotelService):
        self._hotel_service = hotel_service

    @property
    def hotel_service(self):
        return self._hotel_service

    def book_room(self, room_id: int) -> str:
        if self._hotel_service.is_room_available(room_id):
            return 'Комната свободна'
        return 'Комната забронирована'
