def generate_unique_strings() -> Iterator[str]:
    """
    アルファベット26文字(a-z)から重複なしで
    長さ1～26のすべての文字列を列挙するジェネレータ。
    """
    letters = string.ascii_lowercase  # 'a'～'z'
    for length in range(1, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            yield ''.join(perm)

def generate_unique_strings_of_length(length: int) -> Iterator[str]:
    """
    アルファベット26文字(a-z)から重複なしで
    長さ length のすべての文字列を列挙するジェネレータ。
    length は 1～26 の整数を指定してください。
    """
    if not (1 <= length <= 26):
        raise ValueError("length は 1 以上 26 以下の整数で指定してください。")
    letters = string.ascii_lowercase  # 'a'～'z'
    for perm in itertools.permutations(letters, length):
        yield ''.join(perm)
