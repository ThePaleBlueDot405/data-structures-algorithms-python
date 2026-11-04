# 1. Monthly Expenses

mexp = [2200,2350,2600,2130,2190]

# In Feb, how many dollars extra compared to January?
print(mexp[1] - mexp[0])

# Total expense in first quarter
print(mexp[0] + mexp[1] + mexp[2])

# Did I spend exactly 2000 in any month?
print(2000 in mexp)

# Add June expense
mexp.append(1980)
print(mexp)

# April refund of 200 dollars
mexp[3] = mexp[3] - 200
print(mexp)



