# Copyright (c) 2021, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import os
import sys

import nusex
from nusex import CONFIG_DIR, Profile
from nusex.helpers import cprint
from nusex.utils import Downloader

DIRS = ("extensions", "licenses", "profiles", "templates")


def run():
    if os.path.isfile(CONFIG_DIR / "config"):
        cprint("err", "You've already initialised nusex!")
        sys.exit(2)

    for d in DIRS:
        os.makedirs(CONFIG_DIR / d, exist_ok=True)

    for t in ("templates", "licenses"):
        Downloader(t).download(display_progress=True)

    profile_name = input(f"🎤 Profile name [default]: ").strip() or "default"
    profile = Profile(profile_name)
    profile.setup()
    cprint("prc", "Saving profile...", end=" ")
    profile.save()
    print("done")

    cprint("prc", "Creating config files...", end=" ")
    with open(CONFIG_DIR / "config", "w") as f:
        settings = {"profile": profile_name, "last_update": nusex.__version__}
        json.dump(settings, f)
    with open(CONFIG_DIR / "ignore", "w"):
        ...
    print("done")

    cprint("aok", "Initialisation complete!")


def setup(subparsers):
    subparsers.add_parser("init", description="Initialise nusex.")
    return subparsers
