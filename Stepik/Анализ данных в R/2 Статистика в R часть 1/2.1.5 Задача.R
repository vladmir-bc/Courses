# 1 вариант
red_men <- prop.table(HairEyeColor[ , ,'Male'], 2)[3,2]

# 2 вариант
red_men <- prop.table(HairEyeColor[ , ,'Male'], 2)['Red','Blue']
