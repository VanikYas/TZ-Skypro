import unittest

def calculate_bonus(years_worked, sick_leave, annual_income):
   bonus = 0
   if years_worked > 3:
       bonus = (30 * annual_income)/100
   elif 1.5 <= years_worked <= 3:
       bonus = (25 * annual_income)/100
   elif 0.25 <= years_worked < 1.5:
       bonus = (15 * annual_income)/100
   if not sick_leave:
       bonus += (3 * annual_income)/100
   return bonus


class TestBonusCalculation(unittest.TestCase):

    def test_bonus_3_years_with_sick_leave(self):
        self.assertEqual(calculate_bonus(4, True, 50000), (30 * 50000)/100)

    def test_bonus_3_years_without_sick_leave(self):
        self.assertEqual(calculate_bonus(10, False, 50000), ((30 + 3) * 50000)/100)

    def test_bonus_3d1_years_with_sick_leave(self):
        self.assertEqual(calculate_bonus(3.1, True, 60000), (30 * 60000)/100)

    def test_bonus_2_years_with_sick_leave(self):
        self.assertEqual(calculate_bonus(2, True, 60000), (25 * 60000)/100)

    def test_bonus_2d9_years_without_sick_leave(self):
        self.assertEqual(calculate_bonus(2.9, False, 60000), ((25 + 3) * 60000)/100)    

    def test_bonus_1d6_years_with_sick_leave(self):

        self.assertEqual(calculate_bonus(1.6, False, 60000), ((25 + 3) * 60000)/100)
    
    def test_bonus_2_years_without_sick_leave(self):

        self.assertEqual(calculate_bonus(2, False, 60000), ((25 + 3) * 60000)/100)

    def test_bonus_less_than_1d5_years(self):

        self.assertEqual(calculate_bonus(1.4, True, 40000), (15 * 40000)/100)

    def test_bonus_less_than_90_days(self):

        self.assertEqual(calculate_bonus(0.1, True, 30000), 0)

if __name__ == '__main__':
    unittest.main()