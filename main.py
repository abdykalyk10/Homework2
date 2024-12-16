from decouple import Config
from logic import play_game


config = Config("config/settings.ini")


min_number = config("game_settings.min_number", default=1, cast=int)
max_number = config("game_settings.max_number", default=100, cast=int)
attempts = config("game_settings.attempts", default=10, cast=int)
starting_capital = config("game_settings.starting_capital", default=1000, cast=int)

# Запуск игры
play_game(min_number, max_number, attempts, starting_capital)
