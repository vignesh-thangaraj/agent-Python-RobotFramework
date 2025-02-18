#  Copyright 2022 EPAM Systems
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Dict, List, Any, Optional, Tuple, Text

DEFAULT_VARIABLES: Dict[str, Any] = ...


def run_robot_tests(tests: List[str],
                    listener: str = 'robotframework_reportportal_updated.listener',
                    variables: Optional[Dict[str, Any]] = None,
                    arguments: Optional[Dict[str, Any]] = None) -> int: ...


def get_launch_log_calls(mock) -> List[Tuple[List[Any], Dict[str, Any]]]: ...

def item_id_gen(**kwargs) -> Text:...
