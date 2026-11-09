"""Point d'entrée : python -m blackout."""

from blackout.game import Game


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
