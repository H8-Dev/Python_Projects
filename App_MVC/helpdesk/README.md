# Feitor por Heitor Araújo :D

- Como rodar o código
```
cd App_MVC\helpdesk
\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Usar um client para usar as urls do routes.py

- Formatação JSON de cadastro - Usuários

```
{
    "nome": "Rubens",
    "email": "snebur84@gmail.com",
    "setor": "Python"
}
```

- Formatação JSON de cadastro - Chamados
```
{
  "titulo": "Erro de cadastro",
  "descricao": "Não consigo cadastrar meu jogo corretamente",
  "prioridade": "Alta",
  "status": "Aberto",
  "tecnico": "AP5-Yisni",
  "usuario_id": "1"
}
```