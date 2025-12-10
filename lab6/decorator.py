def require_args(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Перевірка кількості переданих аргументів
            if len(args) + len(kwargs) < n:
                return f"Помилка: потрібно мінімум {n} аргументів, отримано {len(args) + len(kwargs)}"
            return func(*args, **kwargs)
        return wrapper
    return decorator