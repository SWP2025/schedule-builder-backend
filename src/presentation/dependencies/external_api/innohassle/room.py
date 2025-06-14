from dishka import Provider, Scope, provide

from src.application.external_api.innohassle.interfaces.room import (
    IRoomService,
)
from src.infrastructure.external_api.innohassle.room import RoomService


class RoomServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_room_service(self) -> IRoomService:
        return RoomService()
