#bibliotecas
import platform as p
import winapps as w

#exibir o Sistema operacional do usuario
print(f"Sistema Operacional do Usuario: {p.system()} {p.release()}.")

print("\nLISTA DE TODOS OS PROGRAMAS INSTALADOS:\n")
for programa in w.list_installed():
    print(f"Programa: {programa.name}.")
    print(f"versao: {programa.version}.")
    print(f"Data instalação: {programa.install_date}.")
    print(f"Data da publicaçaõ: {programa.publisher}.")
    print(f"local da desinstalaçao: {programa.uninstall_string}.")
    print(f"{'_'*30}")
