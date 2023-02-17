# Copyright © 2023 Province of British Columbia
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
"""Test Suite to ensure affiliated businesses schema works as expected."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import AFFILIATED_BUSINESSES


def test_valid_affiliated_businesses_schema():
    """Assert that a valid affiliated businesses object passes validation."""
    is_valid, errors = validate(AFFILIATED_BUSINESSES, 'affiliated_businesses')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

@pytest.mark.parametrize('test_name, field, value', [
    ('businessAffiliations_None', 'businessAffiliations', None),
    ('businessAffiliations_del', 'businessAffiliations', '-'),
    ('draftAffiliations_bool', 'draftAffiliations', True),
    ('draftAffiliations_del', 'draftAffiliations', '-'),
    ('businessAffiliations_identifier', 'businessAffiliations', {'identifier': '1'}),
    ('draftAffiliations_identifier', 'draftAffiliations', {'identifier': '1'}),
    ('businessAffiliations_legalType', 'businessAffiliations', {'identifier': 'BC1234567', 'legalType': 'g'}),
    ('draftAffiliations_legalType', 'draftAffiliations', {'identifier': 'TS123456', 'legalType': 'g'}),
    ('draftAffiliations_nrNumber', 'draftAffiliations', {'identifier': 'TS123456', 'legalType': 'BC', 'nrNumber': True}),
])
def test_invalid_affiliated_businesses_schema(test_name, field, value):
    """Assert that a validation catches invalid iterations of the schema."""
    invalid_schema = copy.deepcopy(AFFILIATED_BUSINESSES)
    invalid_schema[field] = value
    is_valid, errors = validate(invalid_schema, 'affiliated_businesses')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
