import pandas as pd


list_dez = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99]

list_cent = [100, 200, 300, 400, 500, 600, 700, 800, 900, 999]


list_mat = ['Python', 'Ps', 'RAC', 'BD2', 'Português', 'Matemática', 'TPA', 'Direito', 'Atualidades', 'Monitor - Cara é bom']
list_prof = ['Rubens', 'Gleison', 'Gordo', 'Bernardo', 'Brisa', 'Conceição', 'Renato', 'Stella', 'Clebinho', 'Antônio']

list_prog = ['Python', 'Flask', 'Laravel', 'PHP', 'MySQL', 'SQLAlchemy', 'Sqlite3', 'Pandas', 'C#', 'Linux']

list_dec = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

dt_main = pd.DataFrame({"Dezenas": list_dez, "Centenas": list_cent, "Professores":list_prof, "Programas": list_prog, "Decada": list_dec})

dt_prof = pd.DataFrame({"Professores":list_prof, "Dezenas": list_dez}, index = list_mat)


print(dt_main, '\n')

print(dt_prof, '\n')


dt_main["Dezenas"] = dt_main["Dezenas"] + 1
print(dt_main["Dezenas"], '\n')

print(dt_prof.head(2), '\n')

print(dt_prof.tail(4), '\n')

dt_dict = dt_main.to_dict()

print(dt_dict)