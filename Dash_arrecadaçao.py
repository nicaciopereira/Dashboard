import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, Input, Output
import os

# Inicialize o app
app = Dash(__name__)

# Caminho do arquivo CSV
file_path = 'C:/Users/DELL/Desktop/Dashboards/arrecadacao-estado.csv'

# Verificar se o arquivo existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';', encoding='latin1')

# Definir corretamente as colunas de arrecadação
colunas_arrecadacao = [
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
]

# Limpar e converter as colunas de arrecadação
def limpar_e_converter(value):
    if pd.isna(value):
        return float('nan')  # Substituir valores vazios por NaN
    if isinstance(value, str):
        value = value.replace('.', '').replace(',', '.')
    try:
        return float(value)
    except ValueError:
        return float('nan')  # Substituir valores não conversíveis por NaN

# Aplicar a função a todas as colunas de arrecadação
for col in colunas_arrecadacao:
    df[col] = df[col].apply(limpar_e_converter)

df[colunas_arrecadacao] = df[colunas_arrecadacao].fillna(0)  # Preencher NaN com zero
df['TOTAL_ARRECADACAO'] = df[colunas_arrecadacao].sum(axis=1)

# Layout do Dash
app.layout = html.Div([
    dcc.Dropdown(
        id='estado-dropdown',
        options=[{'label': estado, 'value': estado} for estado in df['UF'].unique() if pd.notna(estado)],
        value=df['UF'].unique()[0]  # Valor inicial
    ),
    dcc.Graph(id='arrecadacao-total-grafico'),
    dcc.Graph(id='distribuicao-impostos-grafico'),
    dcc.Graph(id='crescimento-estados-grafico'),
    dcc.Graph(id='crescimento-impostos-grafico'),
    dcc.Graph(id='receita-per-capita-grafico'),
    dcc.Graph(id='comparacao-media-nacional-grafico'),
])

# Callbacks
@app.callback(
    Output('arrecadacao-total-grafico', 'figure'),
    Input('estado-dropdown', 'value')
)
def atualizar_arrecadacao_total(estado_selecionado):
    total_estado = df[df['UF'] == estado_selecionado].groupby('UF')['TOTAL_ARRECADACAO'].sum().reset_index()
    fig = px.bar(total_estado, x='UF', y='TOTAL_ARRECADACAO', title=f'Arrecadação Total em {estado_selecionado}')
    return fig

@app.callback(
    Output('distribuicao-impostos-grafico', 'figure'),
    Input('estado-dropdown', 'value')
)
def atualizar_distribuicao_impostos(estado_selecionado):
    estado_data = df[df['UF'] == estado_selecionado]
    impostos_por_estado = estado_data[colunas_arrecadacao].sum().reset_index()
    impostos_por_estado.columns = ['Imposto', 'Valor']
    fig = px.pie(impostos_por_estado, names='Imposto', values='Valor',
                 title=f'Distribuição da Arrecadação por Tipo de Imposto em {estado_selecionado}')
    return fig

@app.callback(
    Output('crescimento-estados-grafico', 'figure'),
    Output('crescimento-impostos-grafico', 'figure'),
    Input('estado-dropdown', 'value')
)
def atualizar_analise_crescimento(estado_selecionado):
    crescimento_por_estado = df.groupby('UF')['TOTAL_ARRECADACAO'].sum().reset_index()
    crescimento_por_estado = crescimento_por_estado.sort_values(by='TOTAL_ARRECADACAO', ascending=False)
    fig_estado = px.bar(crescimento_por_estado, x='UF', y='TOTAL_ARRECADACAO', title='Crescimento da Arrecadação por Estado')

    crescimento_por_imposto = df[colunas_arrecadacao].sum().reset_index()
    crescimento_por_imposto.columns = ['Imposto', 'Valor']
    fig_imposto = px.bar(crescimento_por_imposto, x='Imposto', y='Valor', title='Crescimento da Arrecadação por Tipo de Imposto')
    return fig_estado, fig_imposto

@app.callback(
    Output('receita-per-capita-grafico', 'figure'),
    Input('estado-dropdown', 'value')
)
def atualizar_receita_per_capita(estado_selecionado):
    receita_per_capita = df.groupby('UF')['TOTAL_ARRECADACAO'].sum().reset_index()
    populacao = {'SP': 46000000, 'RJ': 17000000, 'MG': 21000000, 'ES': 4000000}  # Exemplos
    receita_per_capita['População'] = receita_per_capita['UF'].map(populacao)
    receita_per_capita['Receita Per Capita'] = receita_per_capita['TOTAL_ARRECADACAO'] / receita_per_capita['População']
    fig = px.bar(receita_per_capita, x='UF', y='Receita Per Capita', title='Receita Per Capita por Estado')
    return fig

@app.callback(
    Output('comparacao-media-nacional-grafico', 'figure'),
    Input('estado-dropdown', 'value')
)
def atualizar_comparacao_media_nacional(estado_selecionado):
    arrecadacao_total = df['TOTAL_ARRECADACAO'].sum()
    media_nacional = arrecadacao_total / df['UF'].nunique()
    media_por_estado = df.groupby('UF')['TOTAL_ARRECADACAO'].sum().reset_index()
    media_por_estado['Média Nacional'] = media_nacional
    fig = px.bar(media_por_estado, x='UF', y='TOTAL_ARRECADACAO', title='Comparação com Média Nacional')
    fig.add_scatter(
        x=media_por_estado['UF'],
        y=media_por_estado['Média Nacional'],
        mode='lines+markers',
        name='Média Nacional',
        line=dict(color='red', width=2)
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
