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

SPEC_VERSION = "1.0"


class NSPEncoder:
    def __init__(self):
        self.map = {
            "author_name": b"\x01",
            "author_email": b"\x02",
            "git_profile_url": b"\x03",
            "starting_version": b"\x04",
            "default_description": b"\x05",
            "preferred_license": b"\x06",
        }

    def write(self, path, data):
        with open(path, "wb") as f:
            for k, v in data.items():
                f.write(self.map[k])
                f.write(v.encode())
                f.write(b"\x00")


class NSPDecoder:
    def __init__(self):
        self.map = {
            b"\x01": "author_name",
            b"\x02": "author_email",
            b"\x03": "git_profile_url",
            b"\x04": "starting_version",
            b"\x05": "default_description",
            b"\x06": "preferred_license",
        }
        self.defaults = {
            "author_name": "John Smith",
            "author_email": "thedoctor@email.com",
            "git_profile_url": "https://github.com/shakespearecode",
            "starting_version": "0.1.0",
            "default_description": "My project, made using nusex",
            "preferred_license": "mit",
        }

    def _scan(self, path):
        with open(path, "rb") as f:
            while f.peek(1):
                key = self.map[f.read(1)]
                value = b""
                while True:
                    char = f.read(1)
                    if char == b"\x00":
                        break
                    value += char

                yield key, value.decode()

    def read(self, path):
        data = self.defaults.copy()
        data.update({k: v for k, v in self._scan(path)})
        return data
