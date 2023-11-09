# calculate_bonus program 

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
