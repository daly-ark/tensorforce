# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Generic baseline value function for policy gradient methods.
"""

import numpy as np


class ValueFunction(object):

    def get_features(self, path):
        states = path["states"]
        states = states.reshape(states.shape[0], -1)

        path_length = len(path["rewards"])
        al = np.arange(path_length).reshape(-1, 1) / 100.0

        return np.concatenate([states, states ** 2, al, al ** 2, np.ones((path_length, 1))], axis=1)

    def get_features_size(self, state_size):
        return 2 * state_size + 3

    def predict(self, path):
        raise NotImplementedError

    def fit(self, paths):
        raise NotImplementedError
