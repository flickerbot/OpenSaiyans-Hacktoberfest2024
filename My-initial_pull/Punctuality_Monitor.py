print("Welcome to Punctuality Monitor!")
register = {'Elijah Opeyemi':8.00, 'Asogwu Justus':8.46, 'Ochia Daniel':8.51, 'Raheem David':8.55, 'Ogunyemlusi Ayobami':9.11, 'Omojeme Blessing':9.11, 'Ojeyinka Ameer':9.16, 'Ogbonna Michael':9.25, 'Sulaiman Hummisalam':9.30, 'Oyedokun Philip':9.30, 'Anjorin Toluwalola':9.37, 'Akerele Emmanuel':9.57, 'Uwaoma Gospel':9.59,'Adeogun John':10.08, 'Sewakanu Boluwatife':10.13, 'Taiwo David':10.13, 'Peace Orazu':10.16, 'John Samuel':10.27, 'Azeez Akorede':10.38, 'Agbemakinde Jude':11.19, 'Yoosuf Adedoyin':11.58}
print("\n")
while True:
    search = input("Want to know who's gonna sweep today? Enter name to search: ")
    result = []

    for name in register.keys():
        if search.lower() in name.lower():
            result.append(name)
   
    early_comers = []
    late_comers = []

    for name in result:
        if register[name] <= 10.00:
            early_comers.append(name)
        else:
            late_comers.append(name)
        
    last_two_late_comers = list(register.keys())[-2:]
    
    if result:
        for name in early_comers:
            print(f"{name} was punctual, hence excused from sweeping \n")
                  
        for name in late_comers:
            if name in last_two_late_comers:
                print(f"{name} arrived late, hence assigned to sweep today. \n")
            else:
                print(f"{name} came in late, but might not be the person to sweep. \n")
    else:
        print(f"{search} was absent today."),
        continue
