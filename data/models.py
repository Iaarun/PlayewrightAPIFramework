from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional


@dataclass
class Rating:
    rate: float
    count: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Product:
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating
    id: Optional[int] = None

    def to_dict(self, include_id: bool = False) -> Dict[str, Any]:
        data = {
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "image": self.image,
            "rating": self.rating.to_dict()
        }

        if include_id and self.id is not None:
            data["id"] = self.id

        return data