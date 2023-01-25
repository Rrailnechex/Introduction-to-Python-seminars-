from tabulate import tabulate

the_database = [["8(908) 739 7966", "пранкер", "не брать"],
                ["8(904) 285 4897", "Patryk Kuczyński"],
                ["8(966) 116 6273", "реклама", "не брать"],
                ["8(939) 014 3794", "спамер", "не брать"],
                ["8(901) 164 8516", "Mirosław Grzelak", "скучный"],
                ["8(980) 649 3910", "Ludwik Kaczor"],
                ["8(904) 959 3235", "Jerzy Mróz", "машинист"],
                ["8(904) 707 5635", "Tomasz Stefański", "тот друг"],
                ["8(983) 178 5129", "Rafał Dziedzic", "тот должник"],
                ["8(982) 803 7508", "Izabela Kucharska"]]


""" def print_database():
    i = 0
    for i in range(len(the_database)):
        for j in range(len(the_database[i])):
            print(the_database[i][j], end=" ")
        print()


print_database()
print(111) """


print(tabulate(the_database,
               headers=['Number', 'Name', 'Comment'],
               tablefmt='orgtbl',
               showindex="always",
               missingval="---"))
