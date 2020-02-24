#!/usr/bin/python3
# coding=utf-8
# pylint: disable=I0011

#   Copyright 2019 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    Base64 config seed
"""

import base64

from dusty.models.seed import SeedModel


class Seed(SeedModel):
    """ Base64 config seed class """

    @staticmethod
    def can_handle(config_seed):
        """ Check if seed can be handled by this helper """
        return config_seed.startswith("base64:")

    def handle(self, config_seed):
        """ Unseed config from seed, return None on error """
        if not self.can_handle(config_seed):
            return None
        return base64.b64decode(config_seed[7:])

    @staticmethod
    def get_name():
        """ Module name """
        return "base64"

    @staticmethod
    def get_description():
        """ Module description or help message """
        return "Base64 seed"
