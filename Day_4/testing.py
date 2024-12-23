
# unittest->  testing methods where individual units of source code like function, metho, class are tested to 
#             to verify or determine wheather they are working as intended or not

import unittest

def multi(a,b):
     return a*b

class multiply_testing(unittest.TestCase):
     def test_positive_test_cases(self):
          final_result=multi(3,4)
          self.assertEqual(final_result, 12)

     def test_negative_cases(self):
          final_negative_result=multi(-4,8)
          self.assertEqual(final_negative_result, -32)
     
     def test_zero_cases_function(self):
          final_zero_result=multi(10,0)
          self.assertEqual(final_zero_result, 0)

     def test_true_funtions(self):
          final_true_result=multi(2,2)
          self.assertTrue(final_true_result)

     # def test_false_funtions(self):
     #      final_false_result=multi(2,1)
     #      result=3
     #      self.assertFalse(final_false_result,result)

     def test_check_validation(self):
          keys="unit testing"
          expressions="this is unit testing and we are performing some test cases on unit testing concept"
          message="key container not found"
          self.assertIn(keys,expressions,message)

     def test_check_validation_assert_not(self):
          keys="message are on test"
          expressions="this is unit testing and we are performing some test cases on unit testing concept"
          message="key container not found"
          self.assertNotIn(keys,expressions,message)

if __name__ == "__main__":
     unittest.main()



# assertEqual->checks if the output of the method is equal to expected output
# assertTrue-> check if method evalutes True
# assertFalse-> checks if method evalutes False