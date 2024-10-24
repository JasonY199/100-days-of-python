HANDS = {
    1: '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    2: '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    3: '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

def show(hand):
    """Return string representation of the hand."""
    if hand in HANDS:
        return HANDS[hand]
    else:
        raise ValueError("Invalid hand")
