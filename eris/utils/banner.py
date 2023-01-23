#!/usr/bin/env python3

import re
from .colors import Color


def banner():
    design = (
        "\n"
        "\n"
        "\n"
        "        ___          ___                     ___        \n"
        "       /  /\        /  /\       ___         /  /\       \n"
        "      /  /:/_      /  /::\     /  /\       /  /:/_      \n"
        "     /  /:/ /\    /  /:/\:\   /  /:/      /  /:/ /\     \n"
        "    /  /:/ /:/_  /  /:/~/:/  /__/::\     /  /:/ /::\    \n"
        "   /__/:/ /:/ /\/__/:/ /:/___\__\/\:\__ /__/:/ /:/\:\   \n"
        "   \  \:\/:/ /:/\  \:\/:::::/   \  \:\/\\  \:\/:/~/:/   \n"
        "    \  \::/ /:/  \  \::/~~~~     \__\::/ \  \::/ /:/    \n"
        "     \  \:\/:/    \  \:\         /__/:/   \__\/ /:/     \n"
        "      \  \::/      \  \:\        \__\/      /__/:/      \n"
        "       \__\/        \__\/                   \__\/       \n"
        "\n"
    )

    print(
        Color.set(
            design,
            "r",
        )
    )
    tag = Color.set("           @hackedbyagirl  ", "b")
    split = Color.set(" | ", "wh")
    title = Color.set("Hack the World \n", "cy")

    print(f"{tag} {split} {title}")
