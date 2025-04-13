import re

def valid_card(card_number):
  # must start with 4, 5 or 6
  if not re.match(r'^[4-6]', card_number):
    return False

  # must contains exactly digits
  if not re.match(r'^[\d-]+$', card_number):
    return False

  # may have digits in groups of , separated by one hyphen '-'
  if '-' in card_number:
    groups = card_number.split('-')
    if any(len(group) != 4 for group in groups):
      return False

  #
  card_clean = card_number.replace('-', '')
  if len(card_clean) != 16:
    return False

  #
  if re.search(r'(\d)\1{3,}', card_clean):
    return False

  return True


card_number = input()
if valid_card(card_number):
  print('Valid')
else:
  print('Invalid')
