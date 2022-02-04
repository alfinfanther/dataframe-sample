import pandas as pd

df1 = pd.read_csv('sample-listing-properti-1.csv')
df2 = pd.read_csv('sample-listing-properti-2.csv')
  
print(df1)
print(df2)


   
inner_join = pd.merge(df1, 
                      df2, 
                      on ='Agent', 
                      how ='inner')

print(inner_join)

left_join = pd.merge(df1, 
                     df2, 
                     on ='Agent', 
                     how ='left')

print(left_join)

right_join = pd.merge(df1, 
                      df2, 
                      on ='Agent',
                      how ='right')

print(right_join)

outer_join = pd.merge(df1, 
                      df2, 
                      on ='Agent', 
                      how ='outer')
print(outer_join)