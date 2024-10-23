# Big Data Project
# Authors: Augustin MAILLE, Martin DORE

import scipy.linalg as nla
import numpy as np
import pandas as pd

#-----------QUESTION 1-------------

def sum_column(matrix, column):
    total = 0
    for row in range(matrix.shape[0]):
        total += matrix[row][column]
    return total

def normalize_column(matrix):
    mat_copy = matrix.copy()
    for j in range(mat_copy.shape[1]):
        column_sum = sum_column(mat_copy, j)
        if column_sum != 0:
            for i in range(mat_copy.shape[0]):
                elem = mat_copy[i, j]
                mat_copy[i, j] = elem / column_sum
    return mat_copy

# PageRank algorithm for a given adjacency matrix A
def page_rank(A, beta):
    At = np.transpose(A)
    P = normalize_column(At)  # stochastic matrix
    n = P.shape[0]
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta * P
    it = 0
    d = nla.norm(q_next - q)
    
    # Power method
    while d > 0.0001:
        it += 1
        q_next = np.dot(betaP, q)
        s = sum(q)
        q_next += np.transpose(np.repeat(((1-beta)/n)*s, n))
        q_next = q_next / sum(q_next)
        d = nla.norm(q_next - q)
        q = q_next
    return q_next, it

#------------QUESTION 2-------------

pages = []  # List of unique pages (each page is a different node)

# Filling the list of pages
# Finding all available pages

# Function to check if a list contains '<'
def contains_chevron(lst):
    try:
        lst.index('<')
        return True
    except ValueError:
        return False

# Combine paths_finished.csv and paths_unfinished.csv into all_paths.csv
finished = open("paths_finished.csv", "r")
unfinished = open("paths_unfinished.csv", "r")
all_paths = open("all_paths.csv", "w")

for line in finished.readlines():
    all_paths.write(line)
for line in unfinished.readlines():
    all_paths.write(line)

finished.close()
unfinished.close()
all_paths.close()

# Process the combined paths
f = open("all_paths.csv", "r")
for line in f.readlines():
    path = line.split(";")
    if path[-1] in ["restart", "timeout"]:
        del path[-2:]  # Remove the last and target if restart or timeout

    # Preprocess: remove '<' and the associated pages
    while contains_chevron(path):
        i = path.index('<')
        del path[i-1:i+1]
    
    for page in path:
        page = page.replace('\n', '')  # Remove end-of-line characters
        if page not in pages:
            pages.append(page)  # Add page if not already in the list

f.close()

# Create the adjacency matrix
num_pages = len(pages)
graph = np.zeros((num_pages, num_pages))

f = open("all_paths.csv", "r")
for line in f.readlines():
    path = line.split(";")
    if path[-1] in ["restart", "timeout"]:
        del path[-2:]

    while contains_chevron(path):
        i = path.index('<')
        del path[i-1:i+1]

    for n in range(len(path) - 1):
        path[n] = path[n].replace('\n', '')
        path[n+1] = path[n+1].replace('\n', '')
        current_page_idx = pages.index(path[n])
        next_page_idx = pages.index(path[n+1])
        graph[current_page_idx][next_page_idx] += 1

f.close()

# Function to display the top 10 most visited pages
def top_ten_pages():
    page_dict = two_lists_to_dict(pages, PG)
    sorted_dict = sorted(page_dict.items(), key=lambda x: x[1], reverse=True)
    print("Top 10 most visited pages:\n")
    for i in range(10):
        print(sorted_dict[i])

# Function to convert two lists into a dictionary
def two_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Personalized PageRank algorithm
def personalized_page_rank(A, beta, node_indices):  # node_indices are the indexes of personalized nodes
    At = np.transpose(A)
    P = normalize_column(At)  # stochastic matrix
    n = P.shape[0]
    v = np.zeros(n)
    for i in node_indices:
        v[i] = 1 / len(node_indices)  # Initialize v with 0 everywhere except personalized nodes
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta * P
    it = 0
    d = nla.norm(q_next - q)

    # Power method
    while d > 0.0001:
        it += 1
        q_next = np.dot(betaP, q)
        s = sum(q)
        q_next += np.transpose(np.repeat((1-beta)*s, n) * v)
        q_next = q_next / sum(q_next)
        d = nla.norm(q_next - q)
        q = q_next
    return q_next, it

# Function to get node indices from names
def get_indices_from_names(names):
    return [pages.index(name) for name in names]

# Main program
choice = input("What would you like to do?\n1. Calculate PageRank\n2. Calculate personalized PageRank\n")
if int(choice) == 1:
    B = float(input("Please select a beta value (between 0 and 1):\n"))
    print("Calculating...\n")
    PG, n_iter = page_rank(graph, B)
    print(f"Number of iterations: {n_iter}\n")
    top_ten_pages()
elif int(choice) == 2:
    node_names = input("Enter the exact names of the nodes to personalize, separated by spaces:\n").split()
    B = float(input("Please select a beta value (between 0 and 1):\n"))
    print("Calculating...\n")
    PG, n_iter = personalized_page_rank(graph, B, get_indices_from_names(node_names))
    print(f"Number of iterations: {n_iter}\n")
    top_ten_pages()
