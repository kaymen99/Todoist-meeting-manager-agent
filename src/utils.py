import re
from datetime import datetime, timedelta

def convert_human_datetime(human_datetime):
    human_datetime = human_datetime.lower().strip()
    today = datetime.now().date()
    
    # Helper function to get the next occurrence of a weekday
    def next_weekday(target_weekday, current_date=today):
        today_weekday = current_date.weekday()
        delta_days = (target_weekday - today_weekday + 7) % 7
        if delta_days == 0:
            delta_days = 7  # Next week's day
        return current_date + timedelta(days=delta_days)
    
    # Helper function to get the occurrence of a weekday this week or next week
    def this_or_next_weekday(target_weekday):
        today_weekday = today.weekday()
        delta_days = (target_weekday - today_weekday + 7) % 7
        if delta_days == 0:
            return today  # If today is the target day
        elif delta_days < 7:
            return today + timedelta(days=delta_days)  # This week
        else:
            return next_weekday(target_weekday)  # Next week
    
    # Convert numerical words to integers
    def parse_number_word(word):
        number_words = {
            'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
        }
        return number_words.get(word, None)
    
    # Handle basic phrases
    if human_datetime in ['today', 'tod']:
        return today

    if human_datetime in ['tomorrow', 'tom']:
        return today + timedelta(days=1)

    if human_datetime == 'next week':
        return next_weekday(0)  # Next Monday

    if human_datetime == 'next month':
        year = today.year
        month = today.month + 1
        if month > 12:
            month = 1
            year += 1
        return today.replace(year=year, month=month)

    if human_datetime == 'end of month':
        next_month = today.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)

    if human_datetime.startswith('mid '):
        return datetime.strptime(f"{human_datetime.split()[1]} 15", '%B %d').date().replace(year=today.year)

    # Handle phrases like "2 weeks", "in 3 weeks", "after 2 weeks"
    match = re.match(r'(\d+)\s+weeks?', human_datetime)
    if match:
        weeks = int(match.group(1))
        return today + timedelta(weeks=weeks)

    match = re.match(r'in\s+(\d+)\s+weeks?', human_datetime)
    if match:
        weeks = int(match.group(1))
        return today + timedelta(weeks=weeks)

    match = re.match(r'after\s+(\d+)\s+weeks?', human_datetime)
    if match:
        weeks = int(match.group(1))
        return today + timedelta(weeks=weeks)

    # Handle phrases like "in two weeks"
    match = re.match(r'in\s+([a-zA-Z]+)\s+weeks?', human_datetime)
    if match:
        weeks_word = match.group(1)
        weeks = parse_number_word(weeks_word)
        if weeks is not None:
            return today + timedelta(weeks=weeks)
        else:
            raise ValueError(f"Unable to parse number word: {weeks_word}")

    # Handle days of the week
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if human_datetime in days_of_week:
        target_weekday = days_of_week.index(human_datetime)
        return this_or_next_weekday(target_weekday)

    # Handle combined expressions like "Friday next week"
    match = re.match(r'([a-zA-Z]+)\s+next\s+week', human_datetime)
    if match:
        day_name = match.group(1)
        if day_name in days_of_week:
            target_weekday = days_of_week.index(day_name)
            return next_weekday(target_weekday, current_date=today + timedelta(weeks=1))
        else:
            raise ValueError(f"Unknown day of the week: {day_name}")

    match = re.match(r'this\s+([a-zA-Z]+)', human_datetime)
    if match:
        day_name = match.group(1)
        if day_name in days_of_week:
            target_weekday = days_of_week.index(day_name)
            return this_or_next_weekday(target_weekday)
        else:
            raise ValueError(f"Unknown day of the week: {day_name}")

    match = re.match(r'next\s+([a-zA-Z]+)', human_datetime)
    if match:
        day_name = match.group(1)
        if day_name in days_of_week:
            target_weekday = days_of_week.index(day_name)
            return next_weekday(target_weekday)
        else:
            raise ValueError(f"Unknown day of the week: {day_name}")

    # Handle specific date formats like "jan 27" or "27 jan"
    match = re.match(r'(\d{1,2})\s([a-zA-Z]+)', human_datetime)
    if match:
        day, month = match.groups()
        try:
            return datetime.strptime(f"{day} {month} {today.year}", '%d %b %Y').date()
        except ValueError:
            return datetime.strptime(f"{day} {month} {today.year}", '%d %B %Y').date()

    match = re.match(r'([a-zA-Z]+)\s(\d{1,2})', human_datetime)
    if match:
        month, day = match.groups()
        try:
            return datetime.strptime(f"{day} {month} {today.year}", '%d %b %Y').date()
        except ValueError:
            return datetime.strptime(f"{day} {month} {today.year}", '%d %B %Y').date()

    # Handle "27th" format
    match = re.match(r'(\d{1,2})(st|nd|rd|th)', human_datetime)
    if match:
        day = int(match.group(1))
        return today.replace(day=day)

    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', human_datetime)
    if match:
        return datetime.strptime(human_datetime, '%Y-%m-%d').date()

    raise ValueError(f"Unable to parse human datetime string: {human_datetime}")