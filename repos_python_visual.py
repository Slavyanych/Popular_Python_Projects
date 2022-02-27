import requests
from plotly.graph_objs import Bar
from plotly import offline

# Making an API call and saving the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Storing the answer in a variable
response_dict = r.json()

# Analysis of information about repositories
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

# Summary of the most popular repositories
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Adding hints
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

# Building a visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(0, 182, 79)',
        'line': {'width': 1.5, 'color': 'rgb(8, 13, 115)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 30},
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')




