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
    Config seed tools
"""

import importlib
import pkgutil

from dusty.tools import log


def unseed(config_seed):
    """ Get config from config seed """
    seeds_module = importlib.import_module("dusty.tools.seeds")
    for _, name, pkg in pkgutil.iter_modules(seeds_module.__path__):
        if not pkg:
            continue
        seed = importlib.import_module(
            "dusty.tools.seeds.{}.seed".format(name)
        )
        if seed.Seed.can_handle(config_seed):
            try:
                return seed.Seed().handle(config_seed)
            except:  # pylint: disable=W0702
                log.exception("Failed to unseed config, skipping seed")
                return None
    return None
