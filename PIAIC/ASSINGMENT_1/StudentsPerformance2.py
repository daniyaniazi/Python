# Input Data


# Is there any difference in student score if parents have Bachler level education in a specified score (we will take user input for choosing the score column)
# How many parents have bachelors education, master education, or some college degrees level education?
# in a user given score, is the top scorer a female or male?
# how many students have good in reading (> 75) but not good in writing( < 70)

labels = ['gender', 'parental level of education', 'test preparation course', 'math score', 'reading score', 'writing score']
data = [ 
   ['female', "bachelor's degree", 'none', '72', '72', '74'], 
  ['female', 'some college', 'completed', '69', '90', '88'], 
  ['female', "master's degree", 'none', '90', '95', '93'], 
  ['male', "associate's degree", 'none', '47', '57', '44'], 
  ['male', 'some college', 'none', '76', '78', '75'], 
  ['female', "associate's degree", 'none', '71', '83', '78'], 
  ['female', 'some college', 'completed', '88', '95', '92'], 
  ['male', 'some college', 'none', '40', '43', '39'], 
  ['male', 'high school', 'completed', '64', '64', '67'], 
  ['female', 'high school', 'none', '38', '60', '50'], 
  ['male', "associate's degree", 'none', '58', '54', '52'], 
 ['male', "associate's degree", 'none', '40', '52', '43'], 
 ['female', 'high school', 'none', '65', '81', '73'], 
 ['male', 'some college', 'completed', '78', '72', '70'], 
 ['female', "master's degree", 'none', '50', '53', '58'], 
 ['female', 'some high school', 'none', '69', '75', '78'], 
 ['male', 'high school', 'none', '88', '89', '86'], 
 ['female', 'some high school', 'none', '18', '32', '28'], 
 ['male', "master's degree", 'completed', '46', '42', '46'], 
 ['female', "associate's degree", 'none', '54', '58', '61'], 
 ['male', 'high school', 'none', '66', '69', '63'], 
 ['female', 'some college', 'completed', '65', '75', '70'], 
 ['male', 'some college', 'none', '44', '54', '53'], 
 ['female', 'some high school', 'none', '69', '73', '73'], 
 ['male', "bachelor's degree", 'completed', '74', '71', '80'], 
 ['male', "master's degree", 'none', '73', '74', '72'], 
 ['male', 'some college', 'none', '69', '54', '55'], 
 ['female', "bachelor's degree", 'none', '67', '69', '75'], 
 ['male', 'high school', 'none', '70', '70', '65'], 
 ['female', "master's degree", 'none', '62', '70', '75'], 
 ['female', 'some college', 'none', '69', '74', '74'], 
 ['female', 'some college', 'none', '63', '65', '61'], 
 ['female', "master's degree", 'none', '56', '72', '65'], 
 ['male', 's6ome college', 'none', '40', '42', '38'], 
 ['male', 'some college', 'none', '97', '87', '82'], 
 ['male', "associate's degree", 'completed', '81', '81', '79'], 
 ['female', "associate's degree", 'none', '74', '81', '83'], 
 ['female', 'some high school', 'none', '50', '64', '59'], 
 ['female', "associate's degree", 'completed', '75', '90', '88'], 
]
#########################
#Q1 Solution
# femalesScoreSum    = 0
# malesScoreSum    = 0
#
# # Processing
# scoreColumn = int("score Column (3= math,4=reading 5= writing")
# if scoreColumn > 3 and scoreColumn <6:
#     for innerList in data:
#         if InnerList[0] == 'female':
#             femalesSum = femaleSum + int(innerList[scoreColumn])
#         else:
#             malesSum = maleSum + int(innerList[scoreColumn])
#
# ############
# #Decision Making
# print("Females Score Total =", femalesSum, " Male Score Total =", malesSum)
#
# if femalesSum > MalesSum:
#     print("Famles performance is better than Males in ", Lables[scoreColumn]
# elif femalesSum < MalesSum:
#     print("Males performance is better than Females in ", Lables[scoreColumn]
# else:
#     print("Same level of performance", Lables[scoreColumn]





# How many parents have bachelors education, master education, or some college degrees level education?
parental_level=0
required_level=["bachelor's degree", "master's degree", "associate's degree",'some college']
length=len(data)
# print( length)
for i in range(length-1):
    if data[i][1] in required_level:
        parental_level=parental_level+1

print(f"total no of parent having some degree level education is : {parental_level}")
# in a user given score, is the top scorer a female or male?
#CALCULATE TOTAL SCORE
total_score=0

for i in range(length-1):
  for j in range(1,4):
     total_score=total_score+int(data[i][-j])
  data[i].append(total_score)
  total_score=0



labels.append("total_score")
print(data)

#COMPUTE TOTAL FEMALE AND MALE SCORE
female_total_score=0
male_total_score=0
for i in range(length-1):
    if data[i][0]=="female":
        female_total_score= female_total_score+data[i][-1]
    else:
        male_total_score = male_total_score + data[i][-1]
print(f"TOTAL FEMALE SCORE : {female_total_score}")
print(f"TOTAL FEMALE SCORE : {male_total_score}")


# COMPARE TOTAL SCORE
if female_total_score>male_total_score:
    print("Top scorer is a **Female**")
else:
    print("Top scorer is a **male**")


# how many students have good in reading (> 75) but not good in writing( < 70)
students=0
for i in range(length-1):
    if int(data[i][-2])<70 & int(data[i][-3])>75:
        students=students+1

print(f"Total no of  STUDENT have more tha 75 in reading but  less than 70 in writing : {students}")




