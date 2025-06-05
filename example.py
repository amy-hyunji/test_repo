import os
import sys
tracer_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../execution-tracing/src"))
sys.path.insert(0, tracer_path)
from tracer.core import start_tracing, stop_tracing

def generate_password(length=12):
    """Generate a random password with letters, numbers and special characters."""
    import random
    import string
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def reverse_words(sentence):
    """Reverse the words in a sentence while maintaining word order."""
    count_vowels_sentence(sentence)
    return ' '.join(word[::-1] for word in sentence.split())

def calculate_fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def count_vowels_sentence(sentence):
    """Count the number of vowels in a sentence."""
    words = sentence.split()
    cnt = 0
    for word in words:
        cnt += count_vowels(word)
    print(cnt)
    while cnt > 0:
        generate_password(cnt)
        cnt -=1 
    return  cnt

def count_vowels(text):
    """Count the number of vowels in a given text."""
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == "__main__":
    start_tracing(scope_path=os.getcwd(), track_external_calls=False)
    reverse_words("Hello World")
    stop_tracing("example.trace_output.json")
