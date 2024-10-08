# -----------
# User Instructions
#
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands.
#
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will
# tell you if you are correct.


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):  # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):  # flush
        return (5, ranks)
    elif straight(ranks):  # straight
        return (4, max(ranks))
    elif kind(3, ranks):  # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # 2 pair
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):  # kind
        return (1, kind(2, ranks), ranks)
    else:  # high card
        return (0, sorted(ranks, reverse=True))


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    rank_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    ranks = [int(rank_map.get(r, r)) for r, s in cards]
    ranks.sort(reverse=True)
    return ranks


def straight(ranks):
    prev_rank = ranks[0]
    for x in ranks[1:]:
        if x != prev_rank - 1:
            return False
        prev_rank = x
    return True


def flush(hand):
    _, suit = hand[0]
    for _, s in hand:
        if s != suit:
            return False
    return True


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    prev = ranks[0]
    i = 1
    for x in ranks[1:]:
        if x != prev and n == i:
            return prev
        if x != prev:
            i = 1
        else:
            i += 1
        prev = x
    if n == i:
        return prev
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    x = kind(2, ranks)
    if x is None:
        return None
    if x == ranks[0]:
        y = kind(2, ranks[2:])
    else:
        y = kind(2, ranks[3:])
    if y is None:
        return None
    return x, y







def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"
