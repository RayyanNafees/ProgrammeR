
def profile(ques:str) -> str:
    '''Enter profile type,Whether 'Standard' or 'Custom'.
    In Custom, you can create your own profile.
    In Standard, you have to fill the built-in profile query!'''

    profile = {}
    ques = str(ques)
    from time import sleep
                                            #Custom profile:-

    if ques.capitalize() == "Custom" :
        print('\n \n \t \t \t Custom profile :-  \n')
        num = int(input('How many details would you like to give in your profile info.?: ' ))

        for i in range(num):
            I = str(i+1)
            print()
            key = input(f'Name of the Category_{str(i+1)}: ')
            value = input(f'Enter your {key}: ')
            profile[key] = value
            print()

        sleep(1)
        print('Now, I got your profile: \n')
        sleep(0.5)
        print('Ask me anything about your info like, \n \t')

        category = input('What is your ') #Cases (Uppercase/lowercase) only matters in variables, not in 'inputs'...

        if category == key or category == key+'?':
            print("It's",profile[key],'\n \n')
            sleep(1)
            print('Here, check your feeds...\n \t',profile)
            sleep(0.5)
            print("\n \t \t \"As you can see, I'm NEVER wrong!\" ")
        else:
            print("Plz enter the category as you've EXACTLY entered in profile. Also look for the case.")

                                        #Standard profile:-

    elif ques.capitalize() == "Standard":
        print('\n \n \t \t \t Standard profile :-  \n')
        print('Enter the following categories:-      ...add\'?\' if you wish to leave any info. \n')

        personal = ['Name: ','Father\'s name: ', 'Mother\'s name: ', 'Religion: ', 'Hobbies: ', 'E-mail: ', 'Phone_no.: '] #make 3 diff. lists (list-1)
        address = ['Locality: ', 'City: ', 'State: ', 'Country: ']  #(list-2)
        work = []  #(list-3)

        for p in personal:
            profile[p] = input(p + ': ')

        print('\n Address:- \n \t')

        for a in address:
            profile[a] = input(a + ': ')

        ask = input('Are you in studying in school (yes/no): ')
        print()

        if 'y' in ask.lower():
            work.extend(['School', 'Class', 'Division', 'Class Teacher', 'Fav Teacher','Fav Subject', 'Best Friend', 'You\'r views'])
        else:
            work.extend(['Occupation', 'Post', 'Department', 'Company', 'Office\'s phone/e-mail'])

        for w in work:
            profile[w] = input(w + ': ')

                                        #Now you got the profile!(std)

        sleep(1)
        print('Now, I got your profile: \n')
        sleep(0.5)
        print('Ask me anything about your info like, \n \t')

        category = input('What is your ') #Cases (Uppercase/lowercase) only matters in variables, not in 'inputs'...

        if category in profile:
            print("It's",profile[category],'\n \n')
            sleep(1)
            print('Here, check your feeds...\n \n')
            sleep(0.5)

            for k,v in sorted(profile.items()):
                print('t'*2,k,':',v)

            sleep(0.5)
            print("""\n \t \t "As you can see, I'm NEVER wrong!""""")
        else:
            print("Plz enter the category as you've EXACTLY entered in profile. Also look for the case.")

    else:
        print("Sorry, only Standard or Custom profilez are supported! ")
