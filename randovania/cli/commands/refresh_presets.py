from argparse import ArgumentParser
import logging

from randovania.games.game import RandovaniaGame
from randovania.layout.versioned_preset import VersionedPreset


def refresh_presets_command_logic(args):
    for game in RandovaniaGame:
        logging.info(f"Refreshing presets for {game.long_name}")
        base_path = game.data_path.joinpath("presets")

        for preset_relative_path in game.data.presets:
            preset_path = base_path.joinpath(preset_relative_path["path"])
            preset = VersionedPreset.from_file_sync(preset_path)
            preset.ensure_converted()
            preset.save_to_file(preset_path)


def add_refresh_presets_command(sub_parsers):
    parser: ArgumentParser = sub_parsers.add_parser(
        "refresh-presets",
        help="Loads the preset files and saves then again with the latest version"
    )

    parser.set_defaults(func=refresh_presets_command_logic)
