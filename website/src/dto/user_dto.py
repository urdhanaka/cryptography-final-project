from typing import Any


class UserLoginDTO:
    def __init__(self, json: Any) -> None:
        self.email = ""
        self.password = ""

        if "email" in json:
            self.email = json["email"]
        if "password" in json:
            self.email = json["password"]

    def is_valid(self) -> bool:
        if self.email == "" or self.password == "":
            return False

        return True
