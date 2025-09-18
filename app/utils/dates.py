from datetime import date

def days_between(start_date: date, end_date: date) -> int:
    """
    Return number of nights between two dates. Assumes start_date < end_date.
    """
    delta = end_date - start_date
    return delta.days

def ranges_overlap(a_start: date, a_end: date, b_start: date, b_end: date) -> bool:
    """Return True if [a_start, a_end] overlaps [b_start, b_end]."""
    return not (a_end <= b_start or b_end <= a_start)
