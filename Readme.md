# Dashboard de Arrecadação de Impostos por Estado

Este projeto é um dashboard interativo desenvolvido com **Dash** e **Plotly** para analisar dados de arrecadação de impostos por estado no Brasil. O dashboard oferece visualizações detalhadas sobre arrecadação total, distribuição de impostos, crescimento por estado e tipo de imposto, receita per capita e comparação com a média nacional.

## Funcionalidades

- **Arrecadação Total**: Visualiza a arrecadação total do estado selecionado.
- **Distribuição de Impostos**: Mostra a proporção de arrecadação por tipo de imposto.
- **Crescimento da Arrecadação por Estado**: Exibe o crescimento da arrecadação entre estados.
- **Crescimento da Arrecadação por Tipo de Imposto**: Analisa o crescimento por tipo de imposto.
- **Receita Per Capita**: Calcula e mostra a receita per capita por estado.
- **Comparação com Média Nacional**: Compara a arrecadação de cada estado com a média nacional.

## Requisitos

- Python 3.x
- `pandas`
- `plotly`
- `dash`

Instale as dependências com:

pip install pandas plotly 



Configuração
Prepare o Arquivo CSV

O arquivo CSV deve conter as seguintes colunas para arrecadação:

arduino
Copiar código
'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO', 'IPI - FUMO', 'IPI - BEBIDAS', 
'IPI - AUTOMÓVEIS', 'IPI - VINCULADO À IMPORTACAO', 'IPI - OUTROS', 'IRPF', 
'IRPJ - ENTIDADES FINANCEIRAS', 'IRPJ - DEMAIS EMPRESAS', 'IRRF - RENDIMENTOS DO TRABALHO', 
'IRRF - RENDIMENTOS DO CAPITAL', 'IRRF - REMESSAS P/ EXTERIOR', 'IRRF - OUTROS RENDIMENTOS', 
'IMPOSTO S/ OPERAÇÕES FINANCEIRAS', 'IMPOSTO TERRITORIAL RURAL', 'IMPOSTO PROVIS.S/ MOVIMENT. FINANC. - IPMF', 
'CPMF', 'COFINS', 'COFINS - FINANCEIRAS', 'COFINS - DEMAIS', 'CONTRIBUIÇÃO PARA O PIS/PASEP', 
'CONTRIBUIÇÃO PARA O PIS/PASEP - FINANCEIRAS', 'CONTRIBUIÇÃO PARA O PIS/PASEP - DEMAIS', 'CSLL', 
'CSLL - FINANCEIRAS', 'CSLL - DEMAIS', 'CIDE-COMBUSTÍVEIS (parc. não dedutível)', 'CIDE-COMBUSTÍVEIS', 
'CONTRIBUIÇÃO PLANO SEG. SOC. SERVIDORES', 'CPSSS - Contrib. p/ o Plano de Segurid. Social Serv. Público', 
'CONTRIBUICÕES PARA FUNDAF', 'REFIS', 'PAES', 'RETENÇÃO NA FONTE - LEI 10.833, Art. 30', 
'PAGAMENTO UNIFICADO', 'OUTRAS RECEITAS ADMINISTRADAS', 'DEMAIS RECEITAS', 'RECEITA PREVIDENCIÁRIA', 
'RECEITA PREVIDENCIÁRIA - PRÓPRIA', 'RECEITA PREVIDENCIÁRIA - DEMAIS'
Atualize a variável file_path com o caminho do seu arquivo CSV.

Execute o Aplicativo

Execute o script com:
python nome_do_script.py
O dashboard estará disponível em http://127.0.0.1:8050/.

Uso
Dropdown de Estado: Selecione um estado para visualizar dados específicos.
Gráficos: Os gráficos serão atualizados automaticamente com base no estado selecionado.
Contribuição
Contribuições são bem-vindas! Envie pull requests ou reporte problemas.

Licença
Este projeto está licenciado sob a MIT License.



