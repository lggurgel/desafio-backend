# desafio-backend --> FilmRank

**Desenvolva uma API REST com Django usando o Django Rest Framework.** Siga as instruções abaixo cuidadosamente.

**Funcionalidades:**

1. A API deve permitir que os usuários se cadastrem usando seu e-mail e senha.
2. A API deve permitir a autenticação dos usuários usando seu e-mail e senha.
3. Usuários registrados devem completar seu perfil com informações básicas:
    - nome
    - localização
    - gênero de filme favorito
4. Usuários podem adicionar filmes à sua lista de "Filmes Assistidos":
    - título do filme
    - ano de lançamento
    - diretor
    - gênero
    - avaliação pessoal (de 1 a 5 estrelas)
5. A plataforma deve calcular e exibir um ranking geral dos filmes, com base nas avaliações médias de todos os usuários.
6. Os usuários podem visualizar um ranking individual baseado em suas próprias avaliações.
7. A API deve fornecer um endpoint para listar todos os filmes adicionados, em uma abordagem paginada e com capacidade de filtrar por gênero ou diretor.
8. A API deve ter um endpoint para listar todos os usuários e seus rankings individuais em uma abordagem paginada.
9. A API deve ter um endpoint para buscar um usuário específico usando sua chave primária e visualizar seus filmes avaliados.
10. Os usuários devem poder atualizar os detalhes do seu perfil e suas avaliações de filmes.

**Funcionalidades Adicionais:**

11. Implementar uma recomendação de filmes para os usuários baseada em seu gênero favorito.
12. Possibilidade de os usuários comentarem sobre os filmes e lerem comentários de outros.
13. Notificação para um usuário quando um filme adicionado por ele é avaliado por outros usuários.

**Notas:**

1. Padrão de design REST usando o método de requisição e códigos de status apropriados.
2. Use Postgres SQL ou qualquer outro RDBMS como seu banco de dados.
3. Seria interessante ter testes unitários, mas não é obrigatório.
4. Documente sua API usando Postman ou qualquer ferramenta de documentação com a qual se sinta mais confortável.
5. Hospede seu código no Github com o link da documentação da API no README.
6. Implemente a implantação (deploy) do seu código.
