# EcoClima 🌍

> Uma plataforma interativa com Inteligência Artificial para descobrir,
> compreender e acompanhar os principais problemas ambientais e
> climáticos de diferentes países.

## 📌 Sobre o projeto

O **EcoClima** é um site educativo e informativo integrado a uma
Inteligência Artificial (IA). A plataforma permite que o usuário escolha
um país em um mapa interativo ou informe o nome de um país aleatório. A
partir dessa escolha, a IA apresenta um panorama dos principais
problemas ambientais e dos impactos das mudanças climáticas naquela
região.

A proposta é tornar informações ambientais mais acessíveis, organizadas
e fáceis de compreender, incentivando a conscientização sobre os
desafios climáticos enfrentados em diferentes partes do mundo.

## 🎯 Objetivos

-   Apresentar os principais problemas ambientais e climáticos de cada
    país.
-   Explicar as possíveis causas desses problemas e sua relação com as
    mudanças climáticas.
-   Identificar quais ecossistemas, atividades econômicas e populações
    são afetados.
-   Facilitar o acesso a notícias e informações ambientais de fontes
    confiáveis.
-   Promover a educação ambiental e a conscientização sobre questões
    climáticas globais.
-   Ampliar a acessibilidade por meio de recursos de voz e tradução.

## 🧭 Como a plataforma funciona

1.  O usuário acessa o site e visualiza um mapa-múndi interativo.
2.  Escolhe um país diretamente no mapa ou informa o nome de um país no
    campo de pesquisa.
3.  A plataforma envia a seleção para a IA.
4.  A IA reúne e organiza informações sobre os principais desafios
    ambientais e climáticos do país.
5.  O resultado é apresentado em uma página ou painel com explicações,
    impactos e, quando disponíveis, notícias relacionadas.

Também poderá existir um modo de descoberta aleatória, no qual o sistema
sugere um país para que o usuário conheça seus desafios ambientais.

## 🌱 Informações apresentadas pela IA

Para cada país selecionado, a plataforma poderá apresentar:

-   **Principais problemas ambientais:** desmatamento, queimadas,
    poluição do ar e da água, desertificação, perda de biodiversidade,
    entre outros.
-   **Impactos das mudanças climáticas:** aumento da temperatura, secas,
    enchentes, elevação do nível do mar, eventos extremos e alterações
    nos padrões de chuva.
-   **Causas:** fatores naturais e atividades humanas que contribuem
    para os problemas identificados.
-   **Áreas afetadas:** ecossistemas, cidades, regiões costeiras, áreas
    rurais e outros territórios impactados.
-   **Consequências para a população:** efeitos sobre saúde, moradia,
    alimentação, disponibilidade de água e economia.
-   **Possíveis soluções:** políticas públicas, iniciativas locais,
    tecnologias e ações de preservação.
-   **Notícias relacionadas:** notícias ambientais recentes do próprio
    país ou sobre ele, acompanhadas de links e fontes.

> **Importante:** a IA deverá diferenciar problemas ambientais gerais
> daqueles diretamente associados às mudanças climáticas. As informações
> precisam ser contextualizadas e acompanhadas de fontes, datas e links
> sempre que possível.

## ♿ Acessibilidade e internacionalização

A plataforma poderá incluir recursos para tornar o conteúdo acessível a
diferentes públicos:

-   **Leitura em voz alta:** conversão do conteúdo apresentado em áudio.
-   **Comandos por voz:** possibilidade de pesquisar ou selecionar um
    país por meio da fala.
-   **Tradução automática:** tradução das informações para o idioma
    escolhido pelo usuário.
-   **Notícias em outros idiomas:** apresentação de notícias publicadas
    em veículos do próprio país, com opção de tradução.
-   **Interface acessível:** contraste adequado, navegação por teclado,
    textos alternativos e estrutura compatível com leitores de tela.

## ✨ Funcionalidades previstas

  -----------------------------------------------------------------------
  Funcionalidade                      Descrição
  ----------------------------------- -----------------------------------
  Mapa interativo                     Permite selecionar visualmente um
                                      país.

  Busca por país                      Permite digitar o nome de um país.

  País aleatório                      Sugere um país para exploração.

  Análise com IA                      Gera um resumo dos problemas
                                      ambientais e climáticos.

  Causas e impactos                   Explica as origens dos problemas e
                                      o que é afetado.

  Notícias ambientais                 Exibe notícias relacionadas ao país
                                      selecionado.

  Tradução                            Traduz conteúdos para o idioma
                                      escolhido.

  Leitura em voz alta                 Lê os resultados para o usuário.

  Fontes e referências                Permite consultar a origem das
                                      informações.
  -----------------------------------------------------------------------

## 🧠 Papel da Inteligência Artificial

A IA será responsável por interpretar a seleção do usuário e transformar
informações ambientais em explicações claras e estruturadas.

Um exemplo de solicitação que poderá ser enviada ao modelo:

> Analise os principais problemas ambientais e impactos das mudanças
> climáticas enfrentados pelo país selecionado. Explique as causas, as
> regiões e populações afetadas, as consequências ambientais e sociais e
> possíveis medidas de enfrentamento. Diferencie os problemas ambientais
> gerais daqueles relacionados às mudanças climáticas. Apresente
> informações recentes quando disponíveis e indique fontes confiáveis.

A IA não deverá ser tratada como fonte primária de dados. Sempre que
possível, suas respostas serão fundamentadas em bases de dados,
relatórios científicos, órgãos ambientais e veículos de imprensa
confiáveis.

## 🛠️ Tecnologias previstas

As tecnologias ainda poderão ser definidas durante o desenvolvimento.
Uma possibilidade de arquitetura é:

-   **Frontend:** React ou Next.js.
-   **Estilização:** Tailwind CSS.
-   **Mapa interativo:** Leaflet ou MapLibre GL, com dados geográficos
    de países.
-   **Backend:** Node.js com Express ou rotas de API do Next.js.
-   **Inteligência Artificial:** integração com uma API de modelo de
    linguagem.
-   **Notícias e dados ambientais:** APIs de notícias e fontes
    institucionais, conforme disponibilidade e licença.
-   **Acessibilidade por voz:** APIs de síntese e reconhecimento de fala
    do navegador, quando compatíveis.
-   **Tradução:** serviço de tradução integrado ou modelo com suporte
    multilíngue.

Essa lista é uma sugestão inicial, não uma definição obrigatória da
stack.

## 🗺️ Fluxo simplificado

``` text
Usuário
   |
   v
Seleciona um país no mapa ou na busca
   |
   v
Frontend envia o país selecionado
   |
   v
Backend consulta fontes e solicita análise à IA
   |
   v
IA organiza problemas, causas e impactos
   |
   v
Plataforma apresenta resultados e notícias
   |
   +--> Tradução
   |
   +--> Leitura em voz alta
   |
   v
Usuário explora as informações
```

## 📚 Fontes de informação sugeridas

Para aumentar a confiabilidade das respostas, o projeto poderá utilizar
fontes como:

-   [IPCC](https://www.ipcc.ch/) --- relatórios científicos sobre
    mudanças climáticas.
-   [Programa das Nações Unidas para o Meio Ambiente
    (PNUMA)](https://www.unep.org/) --- informações e iniciativas
    ambientais globais.
-   [NASA Climate](https://climate.nasa.gov/) --- dados e explicações
    sobre o clima.
-   [Organização Meteorológica Mundial (OMM)](https://wmo.int/) ---
    informações meteorológicas e climáticas.
-   [Our World in Data](https://ourworldindata.org/) --- indicadores e
    visualizações sobre meio ambiente e clima.
-   Órgãos ambientais, institutos de pesquisa e veículos jornalísticos
    reconhecidos de cada país.

A disponibilidade, atualização e licença de uso de cada fonte deverão
ser verificadas durante a implementação.

## 🚀 Etapas de desenvolvimento

-   [ ] Definir identidade visual e estrutura das páginas.
-   [ ] Desenvolver a interface inicial e o mapa interativo.
-   [ ] Implementar a seleção e a busca de países.
-   [ ] Criar a opção de país aleatório.
-   [ ] Desenvolver o backend para processar as solicitações.
-   [ ] Integrar a API de Inteligência Artificial.
-   [ ] Estruturar a apresentação de causas, problemas e impactos.
-   [ ] Integrar fontes de dados e notícias ambientais.
-   [ ] Implementar tradução de conteúdo.
-   [ ] Implementar leitura em voz alta e avaliar comandos por voz.
-   [ ] Validar a qualidade das respostas e a confiabilidade das fontes.
-   [ ] Realizar testes de acessibilidade e usabilidade.
-   [ ] Publicar a primeira versão da plataforma.

## 🤝 Contribuição

Contribuições, sugestões de funcionalidades e melhorias são bem-vindas.
Para colaborar:

1.  Faça um fork do repositório.
2.  Crie uma branch para sua alteração.
3.  Realize as modificações e testes.
4.  Envie um Pull Request explicando o que foi desenvolvido.

## 📄 Licença

A licença do projeto ainda será definida.

------------------------------------------------------------------------

**EcoClima --- Conhecer os desafios ambientais do mundo é um passo para
transformar o futuro.** 🌎
