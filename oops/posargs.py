def create_person(**kwargs):
    print(kwargs)

create_person(name="hari",age="35",n_place="pkd",w_place="ekm")
#kwargs shows the results as dictionary

#args shows the result as tuple
def create_person(*args):
    print(args)

create_person("hari","35","pkd","ekm")
