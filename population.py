# project population
# current population = 380,123,456
# one person born every 60 seconds
# one person dies every 12 seconds
# one person immigrates every 40 seconds

# work out how many people are born in three years
# work out how many people die in three years
# work out how many people immigrate in the three years
# use an equation using the answers from above to calculate the population three years on.

# how many people born in three years?
one_person_born_in_seconds = 60
days_in_year = 365
hours_in_a_day = 24
minutes_in_a_day = (hours_in_a_day * 60)
people_born_in_a_day = (minutes_in_a_day / one_person_born_in_seconds)
people_born_in_a_year = (people_born_in_a_day * days_in_year)
people_born_in_three_years = (people_born_in_a_year * 3)


# how many people die in three years
one_person_dies_in_seconds = 12
person_dies_in_a_day = (minutes_in_a_day / one_person_dies_in_seconds)
people_dies_in_a_year = (person_dies_in_a_day * days_in_year)
people_die_in_three_years = (people_dies_in_a_year * 3)


# how many people immigrate in three years
one_person_immigrates_in_seconds = 40
person_immigrates_a_day = (minutes_in_a_day/ one_person_immigrates_in_seconds)
people_immigrates_in_a_year = (person_immigrates_a_day * days_in_year)
people_immigrate_in_three_years = (people_immigrates_in_a_year * 3)


# population in three years
population_three_years = (380123456 + people_born_in_three_years + people_immigrate_in_three_years - people_die_in_three_years)
print( population_three_years)
# populuation in three years = 380,057,756


