import re 
from enums import PropertyType, ApartmentSubtype, HouseSubtype, CommonSubtype

def get_subtype_options(property_type: PropertyType):
    common = [e.value for e in CommonSubtype]
    if property_type == PropertyType.APARTMENT:
        specific = [e.value for e in ApartmentSubtype]
    elif property_type == PropertyType.HOUSE:
        specific = [e.value for e in HouseSubtype]
    else:
        specific = []
    return [""] + common + specific

def add_space_before_caps(s: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", " ", s)