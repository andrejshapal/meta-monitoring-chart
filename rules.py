import yaml

# Чтение вашего YAML-файла
with open('/Users/andrejs.sapals/repos/meta-monitoring-chart/charts/meta-monitoring/src/rules/mimir-rules.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Перебор всех групп и правил, чтобы получить все значения из поля 'record'
records = []

# Процесс перебора
for group in data.get('groups', []):
    for rule in group.get('rules', []):
        record_value = rule.get('record')
        if record_value:
            records.append(record_value)

# Вывод всех найденных значений из поля 'record'
for record in records:
    print(record)