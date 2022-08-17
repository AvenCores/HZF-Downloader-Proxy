import os

print("Установка библиотек")
os.system("pip3 install --upgrade pip")
bib = ["requests"]
for i in range(len(bib)):
        os.system("pip3 install "+bib[i])
os.system('cls' if os.name == 'nt' else 'clear')
print("Установка завершена!")
print("\nНажмите Enter чтобы закрыть")
input()
