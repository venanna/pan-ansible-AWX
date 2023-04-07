import string


def unique_strings(k: int, ntokens: int, pool: str = string.ascii_letters) -> set:
    """Generate a set of unique string tokens.

    k: Length of each token
    ntokens: Number of tokens
    pool: Iterable of characters to choose from

    For a highly optimized version:
    https://stackoverflow.com/a/48421303/7954504
    """

    seen = set()

    # An optimization for tightly-bound loops:
    # Bind these methods outside of a loop
    join = "".join
    add = seen.add

    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen
