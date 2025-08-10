def sanitize_string(text: str) -> str:
    """문자열 정리 (XSS 방지 등)"""
    if not text:
        return ""

    # HTML 태그 제거
    import html
    text = html.escape(text)

    # 불필요한 공백 제거
    text = " ".join(text.split())

    return text


def generate_random_string(length: int = 10) -> str:
    """랜덤 문자열 생성"""
    import secrets
    import string

    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
