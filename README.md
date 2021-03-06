# viztree

[![](https://img.shields.io/github/license/sky-joker/viztree?style=for-the-badge)](https://github.com/sky-joker/viztree/blob/main/LICENSE)

Viztree can generate an html for visualizing the directory tree.  
The directory tree is visualized with [Fancytree](https://github.com/mar10/fancytree).

![](images/sample.png)

# Requirements

* jinja2

# Installing

You can install viztree with pip.

```
$ pip install viztree
```

Or it is possible to install from GitHub repository.

```
$ pip install git+https://github.com/sky-joker/viztree.git
```

# Usage

The html file that has the directory tree does generate by executing the below command.

```
$ viztree
```

If you'd like to specify the directory to generate the tree, please specify the path in the argument of the command.

```
$ viztree some_directory
```

The skin can change by specifying the skin option.

```
$ viztree --skin lion
```

You can look at the visualized directory tree by opening the html file with your browser.
