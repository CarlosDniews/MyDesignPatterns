from BuilderConceitual import Diretor, ConstrutorConcreto1

diretor = Diretor()
construtor = ConstrutorConcreto1()
diretor.construtor = construtor

print("Produto básico padrão:")
diretor.constroi_produto_minimo()
construtor.produto.lista_partes()

print("\n")

print("Produto padrão completo:")
diretor.constroi_produto_completo()
construtor.produto.lista_partes()

print("\n")

print("Produto customizado:")
construtor.produz_parte_a()
construtor.produz_parte_b()
construtor.produto.lista_partes()
