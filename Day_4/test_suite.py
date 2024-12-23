"""
this is test suite example and here are the steps

1) create the test cases
2) create the test suites
3) add test cases to the suites using addTest() method
4) run the test suite using the texttestrunner() and run() method
"""

import unittest

def person_info(first_name, last_name):
     return f"firstname: {first_name} lastname: {last_name}"

class mytestcases(unittest.TestCase):  # step1) creating the test cases
     def test_addition(self):
          self.assertEqual(1+1,2)

     def test_info(self):
          final_output=person_info("john","doe")
          self.assertEqual(final_output,"firstname: john lastname: doe")

     def test_info_1(self):
          final_output=person_info("lora","jin")
          self.assertEqual(final_output,"firstname: lora lastname: jin")

     def test_info_2(self):
          final_output=person_info("amber","rutherford")
          self.assertEqual(final_output,"firstname: amber lastname: rutherford")

     def test_substraction(self):
          self.assertEqual(2-4,-2)

     def test_multiplication(self):
          self.assertEqual(2*4,8)

     def test_division(self):
          self.assertEqual(4/2,2)
     
if __name__ == "__main__":

     suites=unittest.TestSuite() # step2) creating the test suites

     suites.addTest(mytestcases('test_addition')) # steps3) adding test cases via addTest() method
     suites.addTest(mytestcases('test_info'))
     suites.addTest(mytestcases('test_info_1'))
     suites.addTest(mytestcases('test_info_2'))
     suites.addTest(mytestcases('test_substraction'))
     suites.addTest(mytestcases('test_multiplication'))
     suites.addTest(mytestcases('test_division'))

     runner_suites=unittest.TextTestRunner() #steps4) run's  the test suites
     runner_suites.run(suites)

