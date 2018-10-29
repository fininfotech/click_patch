# -*- coding:utf-8 -*-
from click.core import Parameter
from click._compat import text_type
def process_value(self, ctx, value):
    if value is not None:
        if isinstance(value, str):
            value = text_type(value, encoding='utf-8')
        return self.type_cast_value(ctx, value)
Parameter.process_value = process_value
