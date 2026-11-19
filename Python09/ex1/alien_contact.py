from enum import Enum
from pydantic import Field, BaseModel, ValidationError, model_validator
import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime.datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_id(self) -> "AlienContact":
        if self.contact_id.startswith("AC"):
            return self
        raise ValueError("ID must start with 'AC'")

    @model_validator(mode="after")
    def check_verified(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def check_witness(self) -> "AlienContact":
        if (
            self.contact_type == ContactType.TELEPATHIC
            and not self.witness_count >= 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode="after")
    def check_include(self) -> "AlienContact":
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.value}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: {valid.message_received!r}")
        print()
        print("=" * 40)

        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.0,
            duration_minutes=45,
            witness_count=2,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
