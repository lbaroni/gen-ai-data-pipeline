
from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    prod1 = "Zapflow com Gemini"
    prod2 = "Zapflow com ChatGPT"
    prod3 = "Zapflow com Lhama"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtde: PositiveInt
    produto: ProdutoEnum

