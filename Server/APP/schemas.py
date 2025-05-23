from typing import Optional

from pydantic import BaseModel


class LineCreate(BaseModel):
    chinese_name: str
    start_time: str
    end_time: str
    mileage: float
    color: str
    first_opening: str
    intro: str
    url: str
    running_speed: float


class LineUpdate(BaseModel):
    chinese_name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    mileage: Optional[float] = None
    color: Optional[str] = None
    first_opening: Optional[str] = None
    intro: Optional[str] = None
    url: Optional[str] = None
    running_speed: Optional[float] = None


class StationCreate(BaseModel):
    chinese_name: str
    english_name: str
    district: str
    intro: str
    status: str


class StationUpdate(BaseModel):
    chinese_name: Optional[str] = None
    english_name: Optional[str] = None
    district: Optional[str] = None
    intro: Optional[str] = None
    status: Optional[str] = None


class LinesDetailCreate(BaseModel):
    station_id: int
    nums: int


class LinesDetailUpdate(BaseModel):
    nums: int


class PassengerCreate(BaseModel):
    id_number: str
    name: str
    phone_number: str
    gender: str
    district: str


class CardCreate(BaseModel):
    code: int
    money: float


class UserCreate(BaseModel):
    user_name: str
    password: str
    passenger_id: Optional[str] = None
    card_code: Optional[str] = None
    permission: str = "normal"


class UserUpdate(BaseModel):
    password: Optional[str] = None
    permission: Optional[str] = None


class UserDelete(BaseModel):
    password: str


class PassengerSearch(BaseModel):
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    price: Optional[int] = None
    start_station: Optional[str] = None
    end_station: Optional[str] = None


class CardSearch(BaseModel):
    start_station: Optional[str] = None
    end_station: Optional[str] = None
    price: Optional[int] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
