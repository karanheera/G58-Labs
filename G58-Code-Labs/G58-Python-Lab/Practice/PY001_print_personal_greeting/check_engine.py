import subprocess
import json
import os


# =========================
# LOAD TEST CASES
# =========================
def load_tests():
    with open("tests.json", "r") as f:
        return json.load(f)


# =========================
# RUN USER CODE
# =========================
def run_user_code(input_data):
    try:
        result = subprocess.run(
            ["python", "starter.py"],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5
        )
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"


# =========================
# SHOW HINT
# =========================
def show_hint():
    if os.path.exists("hint.txt"):
        print("\n💡 HINT:\n")
        print(open("hint.txt").read())
    else:
        print("\nNo hint available.")


# =========================
# SHOW SOLUTION
# =========================
def show_solution():
    path = "reference_solution/solution.py"

    if os.path.exists(path):
        print("\n📌 SOLUTION:\n")
        print(open(path).read())
    else:
        print("\nNo solution found.")


# =========================
# MAIN ENGINE
# =========================
def run_tests():
    tests = load_tests()

    total = len(tests)
    passed = 0

    print("\n🧪 Running Test Cases...\n")

    for i, test in enumerate(tests, 1):
        input_data = test["input"]
        expected = test["output"]

        actual = run_user_code(input_data)

        if actual == expected:
            print(f"Test {i}: ✅ PASS")
            passed += 1
        else:
            print(f"Test {i}: ❌ FAIL")
            print(f"  Input   : {input_data}")
            print(f"  Expected: {expected}")
            print(f"  Got     : {actual}")

    print("\n========================")
    print(f"RESULT: {passed}/{total} PASSED")
    print("========================\n")

    # FINAL DECISION
    if passed == total:
        print("🎉 ALL TESTS PASSED! Great job!")
    else:
        print("❌ Some tests failed.")

        choice = input("\nNeed help? (hint / solution / skip): ").strip().lower()

        if choice == "hint":
            show_hint()
        elif choice == "solution":
            show_solution()


# =========================
# RUN
# =========================
if __name__ == "__main__":
    run_tests()