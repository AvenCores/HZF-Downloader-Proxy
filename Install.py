import os

print("Установка библиотек")
os.system("pip3 install --upgrade pip")
bib = ["requests"]
for i in range(len(bib)):
        os.system("pip3 install "+bib[i])
os.system('cls')

while True:
    print = input("\nУстановка завершена!\n\nНажмите ENTER чтобы выйти")
    exit()
