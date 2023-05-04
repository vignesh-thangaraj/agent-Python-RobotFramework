"""This package contains tests for the project.

Copyright (c) 2021 https://reportportal.io .
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
"""

from six import add_move, MovedModule

add_move(MovedModule('mock', 'mock', 'unittest.mock'))

REPORT_PORTAL_SERVICE = 'robotframework_reportportal_updated.service.RPClient'
