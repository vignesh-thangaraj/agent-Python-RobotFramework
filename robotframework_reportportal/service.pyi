from logging import Logger
from reportportal_client.client import RPClient
from .model import Keyword as Keyword, Launch as Launch, LogMessage as LogMessage, Suite as Suite, Test as Test
from typing import List, Optional, Text, Union

logger: Logger

def to_epoch(date: Optional[Text]) -> Optional[Text]: ...

class RobotService:
    agent_name: Text = ...
    agent_version: Text = ...
    rp: Optional[RPClient] = ...
    def __init__(self) -> None: ...
    def _get_launch_attributes(self, cmd_attrs: List) -> List: ...
    def init_service(self, endpoint: Text, project: Text, uuid: Text, log_batch_size: int, pool_size: int, skipped_issue: bool, verify_ssl: Union[Text, bool]) -> None: ...
    def terminate_service(self) -> None: ...
    def start_launch(self, launch: Launch, mode: Optional[Text] = ..., rerun: bool = ...,
                     rerun_of: Optional[Text] = ..., ts: Optional[Text] = ..., skip_analytics: Optional[bool] = ...) -> Text: ...
    def finish_launch(self, launch: Launch, ts: Optional[Text] = None) -> None: ...
    def start_suite(self, suite: Suite, ts: Optional[Text] = None): ...
    def finish_suite(self, suite: Suite, issue: Optional[Text] = ..., ts: Optional[Text] = None) -> None: ...
    def start_test(self, test: Test, ts: Optional[Text] = None): ...
    def finish_test(self, test: Test, issue: Optional[Text] = ..., ts: Optional[Text] = None) -> None: ...
    def start_keyword(self, keyword: Keyword, ts: Optional[Text] = None): ...
    def finish_keyword(self, keyword: Keyword, issue: Optional[Text] = ..., ts: Optional[Text] = None) -> None: ...
    def log(self, message: LogMessage, ts: Optional[Text] = None) -> None: ...
