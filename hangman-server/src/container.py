from injector import inject, Module, singleton
from src.application.game_service import GameService
from src.domain.game_repository import GameRepository
from src.infrastructure.in_memory_game_repository import InMemoryGameRepository


class AppModule(Module):
    @singleton
    @inject
    def provide_game_service(
        self, game_repository: InMemoryGameRepository
    ) -> GameService:
        return GameService(game_repository)


class Container(Module):
    def configure(self, binder):
        binder.install(AppModule)
        binder.bind(GameRepository, to=InMemoryGameRepository(), scope=singleton)
