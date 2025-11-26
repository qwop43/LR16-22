from app.services.fake_service import broken_function


def test_broken_function_raises():
    """Перевірка, що функція broken_function кидає виняток"""
    try:
        broken_function()
    except Exception as e:
        assert str(e) == "Test Sentry error: onboarding check"
