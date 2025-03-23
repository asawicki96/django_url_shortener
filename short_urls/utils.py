from snowflake import SnowflakeGenerator
from django.conf import settings

snowlake_id_generator = SnowflakeGenerator(instance=settings.INSTANCE_ID)

def generate_snowflake_id() -> int:
    """
    Generates globally unique ID in Snowflake manner.
    """
    return next(snowlake_id_generator)
