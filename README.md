# Anson


We implement the following column types ourselves
- BSON
- INTERVAL
- VECTOR
- VARCHAR

We take INT and FLOAT from numpy
We take TIMESTAMP, DATA


ORSO_TO_PYTHON_MAP
    OrsoTypes.BOOLEAN: bool,
    OrsoTypes.BLOB: bytes,
    OrsoTypes.DATE: datetime.date,
    OrsoTypes.TIMESTAMP: datetime.datetime,
    OrsoTypes.TIME: datetime.time,
    OrsoTypes.INTERVAL: datetime.timedelta,
    OrsoTypes.STRUCT: dict,
    OrsoTypes.DECIMAL: decimal.Decimal,
    OrsoTypes.DOUBLE: float,
    OrsoTypes.INTEGER: int,
    OrsoTypes.ARRAY: list,
    OrsoTypes.VARCHAR: str,
    OrsoTypes.NULL: None,

    BSON
    VECTOR