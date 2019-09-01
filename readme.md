### Idiom Graph - 成语接龙

This repository uses neo4j graph database server to build a idiom graph. Given a Chinese idiom, the goal is to find another idiom whose first character matches the last character of the given idiom. The process continues.

#### Graph Design
* Node: every character located at the beginning or end of an idiom creates a node
* Edge: every idiom creates a **directed** edge, pointing from the last character (source node) of an idiom to the beginning character (destination node) of another idiom.

![alt-text](assets/combined.jpg)

Two versions are implemented. The first version only requires pinyin(拼音) match (left graph). The second version requires exact character match (right graph).

|                | Nodes     | Edges
| :------------- | :-------- | :---
| Version 1      | 382       | 7874
| Version 2      | 2507      | 7874

Note that there are 2507 distinct Chinese characters located at the beginning or end of idioms (2507 nodes in version 2). Those characters have 382 pronunciations (382 nodes in version 1). The number of edges is the same in both versions, because the file contains 7874 idioms.

#### Implementation

```bash
# Install Dependencies
pip install pandas py2neo xpinyin
```

* Version 1: requiring pinyin/pronounciation match [[idiom_graph_v1.ipynb](idiom_graph_v1.ipynb)]
* Version 2: requiring exact character match [[idiom_graph_v2.ipynb](idiom_graph_v2.ipynb)]

Sample query result: [output/坚定不移.csv](output/坚定不移.csv)
<p align="center">
    <img src="assets/demo.png">
</p>

Follow installation guide for [python3](https://flask.palletsprojects.com/en/1.0.x/installation/#install-install-virtualenv).
```bash
mkdir api
cd api

# activate
python3 -m venv venv
. venv/bin/activate

pip install Flask
pip install py2neo
pip install pandas

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
