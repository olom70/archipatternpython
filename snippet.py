#%%
from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple

@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

class Money(NamedTuple):
    currency: str
    value: int

Line = namedtuple('Line', ['sku', 'qty'])

assert Money('gbp', 10) == Money('gbp', 10)
assert Name("Harry", "One") != Name("Harry", "Two")
assert Line("RED-CHAIR", 5) == Line("RED-CHAIR", 5)

fiver = Money('gbp', 5)
tenner = Money('gbp', 10)

print(fiver*5)
assert fiver * 5 != Money('gbp', 25)
assert fiver + fiver == tenner