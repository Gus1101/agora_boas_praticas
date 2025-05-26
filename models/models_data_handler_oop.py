# Libs import
import pandera.pandas as pa
from pandera.typing import Series

# Models
class SchemaExtractExcelDataOut(pa.DataFrameModel):
    customer_name: Series[str]
    customer_email: Series[str]
    customer_age: Series[int] = pa.Field(ge=1, le=100)

class SchemaTransformDataIn(SchemaExtractExcelDataOut):
    pass

class SchemaTransformDataOut(pa.DataFrameModel):
    customer_name: Series[str]
    customer_email: Series[str]

class SchemaLoadDataIn(SchemaTransformDataOut):
    pass