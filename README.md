# Tree-based Spatial Pyramid Pooling (Pytorch version)
Author: king-jojo
e-mail: zhenghuj@usc.edu

This is pytorch version of my bachelor's degree thesis. Applying tree based convolution and pyramid pooling to classify defferent algorithms into defferent categories. 

## Usage
Unzip algorithm file.

    $ Unzip ./data/algorithms.pkl.zip

Load nodes and tree structures from algorithm pickle file.
Nodes for vectorization. Trees for training and testing.

    $ python load_nodes.py
    $ python load_trees.py

Vectorization. 

    $ python Anode2vec.py

Training classifier. 

    $ python classifier.py

Test.

    $ python test.py 