"""Module providing pydantic models for cv sections"""
import re
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class PersonContact(BaseModel):
    name: str = Field()
    age: Optional[int] = Field(default=None)
    mail: str = Field()
    phone: str = Field()
    location: dict = Field()

    @field_validator("age")
    def validate_age(cls, value):
        if value and (value < 18 or value > 120):
            raise ValueError("Age must be between 0 and 120")
        return value

    @field_validator("mail")
    def validate_mail(cls, value):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if not re.fullmatch(regex, value):
            raise ValueError("Invalid email input")
        return value


class Language(BaseModel):
    language: str = Field()
    fluency: str = Field()


class Languages(BaseModel):
    languages: List[Language]


class TechnicalSkill(BaseModel):
    name: str = Field()
    keywords: List[str]


class TechnicalSkills(BaseModel):
    technical_skills: List[TechnicalSkill]


class Education(BaseModel):
    institution: str = Field()
    area: str = Field()
    start_date: str = Field()
    end_date: Optional[str] = Field(default=None)


class EducationInfo(BaseModel):
    education: List[Education]


class Experience(BaseModel):
    company: str = Field()
    position: str = Field()
    start_date: str = Field()
    end_date: Optional[str] = Field(default=None)
    summary: str = Field()
    contributions: List[str] = Field()


class Experiences(BaseModel):
    experience: List[Experience]
