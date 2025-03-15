# [variáveis]

str = "touro"
list = ["touro", "furão"]
int: 3

print(str)
print(list)
print(int)

# [condicionais]

# if str == "bode":
#     print("Está")
    
# else:
#     print("Não está")
    
# [estrutura de repetições]  

# while cond.: - não sabe quantas vezes vai repetir
# for cond. in cond.: - sabe quantas vezes vais repetir

for t in list:
    if str == t:
        print("YES!")
        break
        
else:
    print("NO!")
    
    