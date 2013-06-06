Feature: Compute factorial | run 3 times
    In order to play with radish
    As beginners
    We'll implement factorial

    Scenario: Factorial of 0 - WILL PASS | run 500 times
        Given I have the number 0
        When I compute its factorial
        and I fail after 10 times

