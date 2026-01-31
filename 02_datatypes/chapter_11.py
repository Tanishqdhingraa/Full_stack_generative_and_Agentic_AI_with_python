# CONCEPT: External Libraries + Named Tuples
# DESCRIPTION: Shows date-time handling with a third-party module and lightweight structured data 
# using namedtuple

import arrow

brewing_time = arrow.utcnow()           # get current UTC date & time
brewing_time.to("Europe/Rome")          # convert time to a specific timezone

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])  # immutable, named data structure
