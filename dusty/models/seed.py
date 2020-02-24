#!/usr/bin/python3
# coding=utf-8
# pylint: disable=I0011,R0201,W0613

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
    Config seed models
"""
from dusty.models.module import ModuleModel
from dusty.models.meta import MetaModel


class SeedModel(ModuleModel, MetaModel):  # pylint: disable=W0223
    """ Config seed base class """

    @staticmethod
    def can_handle(config_seed):
        """ Check if seed can be handled by this helper """
        return False

    def handle(self, config_seed):
        """ Unseed config from seed, return None on error """
        return None
