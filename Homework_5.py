def bio(name,born,pronoun):
    print(name.capitalize(), "was born in", born)
    print(pronoun.capitalize(), "will turn", 2024 - born, "years old this year")
    print(pronoun.capitalize(), "will be 67 in the year", born + 67)
    print("\n")

# PRINT BIOS
bio("stephen",1984,"he")
bio("mary",1990,"she")
bio("jane",2000,"she")
# EXIT
quit()