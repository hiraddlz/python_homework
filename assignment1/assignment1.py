# Write your code here.
# Task 1: Hello
# Write a hello function that takes no arguments and returns "Hello!".
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
# Write a greet function. It takes one argument, a name, and returns "Hello, Name!".
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "int_divide":
                return a // b
            case "modulo":
                return a % b
            case "power":
                return a ** b
            case _:
                raise ValueError(f"Unknown operation: {operation}")
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        # For operations like multiplying strings
        op_word = operation
        return f"You can't {op_word} those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, to_type):
    try:
        match to_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                raise ValueError(f"Unknown type: {to_type}")
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {to_type}."

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        total = sum(args)
        count = len(args)
        avg = total / count
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    if not kwargs:
        return None
    if mode == "best":
        # return name of highest scorer
        best_student = max(kwargs.items(), key=lambda kv: kv[1])[0]
        return best_student
    elif mode == "mean":
        avg = sum(kwargs.values()) / len(kwargs)
        return avg
    else:
        raise ValueError(f"Unknown mode: {mode}")

# Task 8: Titleize, with String and List Operations

def titleize(text):
    little = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    titled = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i == 0 or i == len(words) - 1 or lw not in little:
            titled.append(lw.capitalize())
        else:
            titled.append(lw)
    return " ".join(titled)

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    guessed = set(guess)
    for ch in secret:
        if ch in guessed:
            result += ch
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            cluster = ""
            while i < len(word) and word[i] not in vowels:
                if i < len(word) - 1 and word[i:i+2] == "qu":
                    cluster += word[i:i+2]
                    i += 2
                else:
                    cluster += word[i]
                    i += 1
            result.append(word[i:] + cluster + "ay")
    return " ".join(result)

if __name__ == "__main__":
    print(hello())
    print(greet("Alice"))
    print(calc(3, 4))
    print(data_type_conversion("123", "int"))
    print(grade(90, 80, 70))
    print(repeat("ha", 3))
    print(student_scores("best", Alice=90, Bob=95))
    print(titleize("the lord of the rings"))
    print(hangman("alphabet", "ab"))
    print(pig_latin("hello world"))
