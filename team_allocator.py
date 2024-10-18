import os
'''
    This is the team allocator project solution example project
'''
def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']

def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []
    for student in student_list:
        if 'Durban' in student:
            dbn_students.append(student)
    return dbn_students

def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []
    for student in student_list:
        if 'Cape Town' in student:
            cpt_students.append(student)

    return cpt_students

def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []
    for student in student_list:
        if 'Johannesburg' in student:
            jhb_students.append(student)
    return jhb_students

def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []
    for student in student_list:
        if 'Phokeng' in student:
            nw_students.append(student)
    return nw_students
  
def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students = []
    for student in dbn_students:
        if 'Durban Physical' in student:
            dbn_physical_students.append(student)
    return dbn_physical_students
    
def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    dbn_physical_teams = []
    for i in range(0,len(dbn_physical_students)-1,4):
        dbn_physical_teams.append(dbn_physical_students[i:i +4])



    return dbn_physical_teams

def dbn_teams_file(dbn_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    #create a file called durban physical teams
    file = open("./campus_teams.txt", "a")
    for team in dbn_physical_teams:
        file.write(", ".join(team) + '\n')
    file.close()

def cpt_physical_students(cpt_campus_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    new_phy = []
    for student in cpt_campus_students:
        if 'Cape Town Physical' in student:
            new_phy.append(student)
    return new_phy
    
def cpt_physical_teams(cpt_physical_students):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    cpt_physical_teams = []
    for i in range(0,len(cpt_physical_students)-1,4):
        cpt_physical_teams.append(cpt_physical_students[i:i +4])



    return cpt_physical_teams

def cpt_teams_file(cpt_physical_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    file = open("./campus_teams.txt", "a")
    for team in cpt_physical_teams:
        file.write(", ".join(team)+"\n")   
    file.close()

def jhb_physical_students(jhb_campus_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    new_phy = []
    for student in jhb_campus_students:
        if 'Johannesburg Physical' in student:
            new_phy.append(student)
    return new_phy

def jhb_physical_teams(jhb_physical_students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    jhb_physical_teams = []
    for i in range(0,len(jhb_physical_students)-1,4):
        jhb_physical_teams.append(jhb_physical_students[i:i +4])



    return jhb_physical_teams

def jhb_teams_file(jhb_physical_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    file = open("./campus_teams.txt", "a")
    for team in jhb_physical_teams:
        file.write(", ".join(team)+"\n")   
    file.close()

def nw_physical_students(nw_campus_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    new_phy = []
    for student in nw_campus_students:
        if 'Phokeng Physical' in student:
            new_phy.append(student)
    return new_phy

def nw_physical_teams(nw_physical_students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    nw_physical_teams = []
    for i in range(0,len(nw_physical_students)-1,4):
        nw_physical_teams.append(nw_physical_students[i:i +4])



    return nw_physical_teams

def nw_teams_file(nw_physical_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    file = open("./campus_teams.txt", "a")
    for team in nw_physical_teams:
        file.write(", ".join(team)+"\n")   
    file.close()

def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []
    for student in student_list:
        if 'Virtual' in student:
            virtual_campus.append(student)

    return virtual_campus

def virtual_teams(get_virtual_students):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []
    
    for i in range(0, len(get_virtual_students)-1,4):
        virtual_teams.append(get_virtual_students[i:i+4])
    return virtual_teams

def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    file = open("./virtual_teams.txt", "w")
    for team in virtual_teams:
        file.write(", ".join(team)+"\n")   
    file.close()

def clear():
    if os.path.exists("campus_teams.txt"):
        os.remove("campus_teams.txt")
    else:
        pass

if __name__ == '__main__':
    # dbn_campus_students(student_list())
    # cpt_campus_students(student_list())
    # jhb_campus_students(student_list())
    # nw_campus_students(student_list())
    # dbn_physical_students(dbn_campus_students(student_list()))
    # cpt_physical_students(cpt_campus_students(student_list()))
    # jhb_physical_students(jhb_campus_students(student_list()))
    # nw_physical_students(nw_campus_students(student_list()))
    # get_virtual_students(student_list())

    # dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list())))
    # cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list())))
    # jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list())))
    # nw_physical_teams(nw_physical_students(nw_campus_students(student_list())))
    # virtual_teams(get_virtual_students(student_list()))
    clear()
    dbn_teams_file(dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list()))))
    cpt_teams_file(cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list()))))
    jhb_teams_file(jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list()))))
    nw_teams_file(nw_physical_teams(nw_physical_students(nw_campus_students(student_list()))))
    virtual_teams_file(virtual_teams(get_virtual_students(student_list())))










