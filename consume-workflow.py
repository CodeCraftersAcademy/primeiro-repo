import requests

# Configurações
owner = 'CodeCraftersAcademy'
repo = 'primeiro-repo'
workflow_name = 'Python aplication'
token = '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'

# Autenticação
headers = {'Authorization': f'token {token}'}

# Obter ID do Workflow
workflow_url = f'https://api.github.com/repos/{owner}/{repo}/actions/workflows'
response = requests.get(workflow_url, headers=headers)
workflow_id = response.json()['workflows'][0]['id']  # Assume que você está pegando o primeiro workflow, ajuste conforme necessário

# Obter Status do Workflow
runs_url = f'https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs'
response = requests.get(runs_url, headers=headers)
workflow_run = response.json()['workflow_runs'][0]
status = workflow_run['conclusion']

# Verificar Status dos Testes
jobs_url = f'https://api.github.com/repos/{owner}/{repo}/actions/runs/{workflow_run["id"]}/jobs'
response = requests.get(jobs_url, headers=headers)
jobs = response.json()['jobs']

tests_passed = all(job['conclusion'] == 'success' for job in jobs)

if status == 'success' and tests_passed:
    print(f'O workflow "{workflow_name}" foi bem-sucedido e todos os testes passarGabyasam.')
    return True
else:
    print(f'O workflow "{workflow_name}" falhou ou alguns testes não passaram.')
    return False
