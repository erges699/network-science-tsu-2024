# Анализ данных и социальные медиа 2024

Проект создан в рамках обучения <a href="https://moodle.tsu.ru/course/view.php?id=34363&section=5" target="_blank" rel="noreferrer">Анализ данных и социальные медиа</a>. Использование открытого программного обеспечения при разработке геосервисов МИИГАиК.

Использованы следующие технологии и пакеты:
<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"> </a>
<a href="https://networkx.org" target="_blank" rel="noreferrer"> <img src="https://networkx.org/_static/networkx_logo.svg" alt="python" width="40" height="80"> </a>
</p>

<h3 align="left">Задания для лабораторных работ:</h3>

<p align="left"> 
1. Требуется написать скрипт на языке Python с реализацией алгоритма Дейкстры для заданного графа. Граф задаётся матрицей смежности или списком смежных вершин. Алгоритм должен находить кратчайшие пути от произвольной начальной вершины до всех остальных. Для представления графов разрешается использовать сторонние библиотеки, но не разрешается использовать реализацию алгоритма Дейкстры в составе сторонних библиотек.
</p>

```
ex_1_dijkstra.py
```

<p align="left"> 
2. С использованием библиотеки NetworkX требуется написать скрипт для вычисления меры центральности в собственных векторах для некоторого графа. Преподавателем будет предоставлена некоторая характеристика мер центральности вершин несложного графа, и требуется подобрать (вручную, не нужно автоматизировать) исходный граф, в которой меры центральности удовлетворяют заданным характеристикам.
</p>

```
ex_2_centrality.py
```

<p align="left"> 
3. С использованием библиотеки NetworkX требуется написать скрипт для генерации графа в модели Эрдёша-Реньи с заданными характеристиками. Преподавателем будут даны значения количества вершин и вероятность появления случайного ребра. Требуется вычислить в программе среднюю степень вершины и сравнить её со значением средней степени вершины, полученной по формуле из материала лекций.
</p>

```
ex_3_erdos_renyi.py
```

<h3 align="left">Установка:</h3>

### Клонировать репозиторий и перейти в него:

```
git@github.com:erges699/marigostraru-202404.git
```

### Создать и активировать виртуальное окружение, установить в него зависимости:

```
$ python3.9 -m venv venv
$ . venv/bin/activate
$ python3 -m pip install --upgrade pip
$ pip install -r requirements.txt
```

<h3 align="left">Об авторе:</h3>
<a href="https://github.com/erges699" target="_blank">Сергей Баляба</a>
