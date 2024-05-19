# Pandas4

# 1 Problem 1 : Nth Highest Salary (https://leetcode.com/problems/nth-highest-salary/solution/)

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N> len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    return df.sort_values(by =['salary'], ascending = False).head(N).tail(1)[['salary']].rename(columns={'salary':f'getNthHighestSalary({N})'})

# 2 Problem 2 : Second Highest Salary ( https://leetcode.com/problems/second-highest-salary/ )

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if 2 > len(df):
        return pd.DataFrame({'SecondHighestSalary':[None]})
    df = df.sort_values(by=['salary'], ascending = False)
    df = df.head(2).tail(1)[['salary']].rename(columns = {'salary':'SecondHighestSalary'})
    return df

    