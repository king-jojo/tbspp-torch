import ast
import pickle
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tree_dataset import TreeDataSet
from Anode2vec import EMBEDDING_DIM
from classifier import tbspp

def main():
	tbspp = torch.load('./data/tbspp.pth')
	with open('./data/algorithm_trees.pkl', 'rb') as fh:
		_, trees, labels = pickle.load(fh)
	with open('./data/vectors.pkl', 'rb') as fh:
		embeddings, embed_lookup = pickle.load(fh)

	embeddings_new = nn.Embedding(embeddings.weight.size(0)+1, embeddings.weight.size(1))
	# add one feature for padding
	with torch.no_grad():
		tensor_for_padding = torch.tensor([[0] * EMBEDDING_DIM], dtype=torch.float32)
		embeddings_pad = torch.cat((embeddings.weight, tensor_for_padding), 0)
		embeddings_new.weight.data.copy_(embeddings_pad)

	label_size = len(labels)
	testdata = TreeDataSet(trees, labels, embed_lookup)

	correct = 0
	total = 0
	with torch.no_grad():
		for batch in testdata.data_gen():
			nodes, children, label = batch
			nodes2vec = embeddings_new(torch.tensor(nodes, dtype=torch.long))
			children2tensor = torch.tensor(children, dtype=torch.long)
			label = torch.tensor(label)
			out = tbspp(nodes2vec, children2tensor)
			_, predicted = torch.max(out.data, 1)
			total += label.size(0)
			correct += (predicted == label).sum().item()
	print('Accuracy of the tework on the testing data set is: %.3f %%' % (100* correct/total))

if __name__ == '__main__':
	main()