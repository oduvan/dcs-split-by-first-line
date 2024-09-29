from dcs_split_by_first_line.types import SplitTranslation, SplitByFirstLine
from content_settings import permissions


COMPANY_DESCRIPTION = SplitTranslation(
    "The best Company",
    fetch_permission=permissions.any,
    help="The description of the company",
)

RATINGS = SplitByFirstLine("""
---BEST---
This is the best book in the world
---GOOD---
This is a good book
---BAD---
This is a bad book
""".strip(),
    split_default_key="BEST",
    help="Rating definitions",
)
