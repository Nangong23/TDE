#!/bin/env python3
class TestCase:
    """
    A basic class of test case.
    """
    def __init__(self, name) -> None:
        self.name = name
    
    def run(self):
        raise NotImplementedError("Subclasses should implement this method")

class TestSuite:
    """
    A class to manage a collection of test cases.
    """
    def __init__(self) -> None:
        self.test_cases = []
    
    def add_test_case(self, test_case):
        """
        Add a test case to the suite.
        """
        self.test_cases.append(test_case)
    
    def run_all(self):
        """
        Run all test cases in the suite.
        """
        result = {'Pass': 0, 'Fail': 0}
        for test_case in self.test_cases:
            try:
                test_case.run()
                result['Pass'] += 1
                print(f"[✓] {test_case.name} passed")
            except AssertionError as e:
                result['Fail'] += 1
                print("[x] {test_case.name} failed}")
        print(result)
        return result

class MathTestCase(TestCase):
    """
    A test case for basic math operations.
    """
    def __init__(self, name, operation, expected_result):
        super().__init__(name)
        self.operation = operation
        self.expected_result = expected_result
    
    def run(self):
        result = eval(self.operation)
        assert result == self.expected_result, f"Expected {self.expected_result}, but got {result}"


class StringTestCase(TestCase):
    """
    A test case for string operations.
    """
    def __init__(self, name, operation, expected_result):
        super().__init__(name)
        self.operation = operation
        self.expected_result = expected_result
    
    def run(self):
        result = eval(self.operation)
        assert result == self.expected_result, f"Expected {self.expected_result}, but got {result}"

if __name__ == "__main__":
    # Create a test suite
    suite = TestSuite()

    # Add math test cases
    suite.add_test_case(MathTestCase("Addition Test", "1 + 1", 2))
    suite.add_test_case(MathTestCase("Subtraction Test", "5 - 3", 2))
    suite.add_test_case(MathTestCase("Multiplication Test", "2 * 3", 6))
    suite.add_test_case(MathTestCase("Division Test", "6 / 2", 3))

    # Add string test cases
    suite.add_test_case(StringTestCase("String Concatenation Test", "'Hello' + ' World'", "Hello World"))
    suite.add_test_case(StringTestCase("String Length Test", "len('hello')", 5))

    # Run all test cases
    results = suite.run_all()
    print(f"Results: {results}")
