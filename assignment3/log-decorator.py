import logging

# Setup logger
logger = logging.getLogger("parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Format arguments
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"
        
        # Execute function and capture return value
        result = func(*args, **kwargs)
        
        # Log details
        log_msg = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n"
            + "="*50
        )
        logger.log(logging.INFO, log_msg)
        return result
    return wrapper

@logger_decorator
def print_hello():
    print("Hello, World!")

@logger_decorator
def check_true(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    print_hello()
    check_true(1, 2, 3)
    return_decorator(a=1, b=2)