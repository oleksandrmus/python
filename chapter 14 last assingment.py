def list_benefits():
    list_of_benefits=[ "More organized code", "More readable code", "Easier code reuse",
                       "Allowing programmers to share and connect code together"]
    print(list_of_benefits)
    return list_of_benefits
list_benefits()
def build_sentence(benefit):
    return benefit+"is a benefit of functions!"
    print(benefit+"is a benefit of functions!")
def name_the_benefits_of_functions():
    list_of_benefits=list_benefits()
    print(build_sentence(list_of_benefits[0]))

    print(build_sentence(list_of_benefits[1]))

    print(build_sentence(list_of_benefits[2]))

    print(build_sentence(list_of_benefits[3]))
name_the_benefits_of_functions()