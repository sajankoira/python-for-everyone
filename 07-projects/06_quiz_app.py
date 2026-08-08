"""
PROJECT 6: Quiz App (JSON based)
"""
import json
import random

QUESTIONS = [
    {
        "question": "Who created Python?",
        "options": ["A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "A",
        "explanation": "Guido van Rossum created Python in 1991"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B",
        "explanation": "def keyword defines function"
    },
    {
        "question": "What is output of 2**3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B",
        "explanation": "** is exponentiation, 2^3=8"
    },
    {
        "question": "Which data type is mutable?",
        "options": ["A. tuple", "B. string", "C. list", "D. int"],
        "answer": "C",
        "explanation": "List is mutable, can change"
    },
    {
        "question": "What does len('Python') return?",
        "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
        "answer": "B",
        "explanation": "Python has 6 letters"
    }
]

def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    print("📝 Python Quiz - 5 Questions")
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for opt in q["options"]:
            print(f"  {opt}")
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            print(f"✅ Correct! {q['explanation']}")
            score += 1
        else:
            print(f"❌ Wrong! Correct is {q['answer']} - {q['explanation']}")

    print(f"\n--- Result: {score}/{len(questions)} ---")
    if score == len(questions):
        print("🏆 Perfect! You're Python pro!")
    elif score >= 3:
        print("👍 Good job!")
    else:
        print("📚 Keep learning! Check 01-basics again")

if __name__ == "__main__":
    run_quiz(QUESTIONS)
