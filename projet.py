# Big Data Project
# Authors: Augustin MAILLE - Martin DORE

import scipy.linalg as nla
import numpy as np
import pandas as pd


# ----------- QUESTION 1 -------------

def sum_column(matrix, column):
    total = 0
    for row in range(matrix.shape[0]):
        total += matrix[row][column]
    return total

def normalize_column(matrix):
    normalized_matrix = matrix.copy()
    for j in range(normalized_matrix.shape[1]):
        col_sum = sum_column(normalized_matrix, j)
        if col_sum != 0:
            for i in range(normalized_matrix.shape[0]):
                normalized_matrix[i, j] = normalized_matrix[i, j] / col_sum
    return normalized_matrix

# PageRank for an adjacency matrix A with a damping factor beta
def page_rank(A, beta):
    At = np.transpose(A)
    P = normalize_column(At)  # stochastic matrix
    n = P.shape[0]
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta * P
    iterations = 0
    diff = nla.norm(q_next - q)
    
    # Power method
    while diff > 0.0001:
        iterations += 1
        q_next = np.dot(betaP, q)
        s = sum(q)
        q_next += np.transpose(np.repeat(((1 - beta) / n) * s, n))
        q_next = q_next / sum(q_next)
        diff = nla.norm(q_next - q)
        q = q_next
        
    return q_next, iterations


# ------------ QUESTION 2 -------------

nodes = []  # Nodes representing different pages

# Filling nodes
# Find all available pages

# Create adjacency matrix

def contains_chevron(lst):
    try:
        lst.index('<')
        return True
    except ValueError:
        return False

with open("paths_finished.csv", "r") as f:
    for line in f.readlines():
        path = line.split(";")
        # Preprocessing: remove '<' with corresponding number of pages
        while contains_chevron(path):
            i = path.index('<')
            del path[i - 1: i + 1]
        for page in path:
            page = page.replace('\n', '')  # Remove newline
            if page not in nodes:
                nodes.append(page)  # Add the page if not already known

num_nodes = len(nodes)
graph = np.zeros((num_nodes, num_nodes))

with open("paths_finished.csv", "r") as f:
    for line in f.readlines():
        path = line.split(";")
        while contains_chevron(path):
            i = path.index('<')
            del path[i - 1: i + 1]
        for n in range(len(path) - 1):
            path[n] = path[n].replace('\n', '')
            path[n + 1] = path[n + 1].replace('\n', '')
            current_idx = nodes.index(path[n])
            next_idx = nodes.index(path[n + 1])
            graph[current_idx][next_idx] += 1

# Display top 10 most visited pages with their scores
def top_10_visited():
    page_rank_dict = two_lists_to_dict(nodes, page_ranks)
    sorted_dict = sorted(page_rank_dict.items(), key=lambda x: x[1], reverse=True)
    print("Top 10 most visited pages:\n")
    for i in range(10):
        print(sorted_dict[i])

def two_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Uncomment to run iterations for different beta values
"""
damping_factors = [0.1, 0.3, 0.5, 0.75, 0.98]

for beta in damping_factors:
    page_ranks, iterations = page_rank(graph, beta)
    print("\nNumber of iterations: " + str(iterations) + "\n")
"""


# --------------- Personalized PageRank -------------
def personalized_page_rank(A, beta, nodes_indexes):
    At = np.transpose(A)
    P = normalize_column(At)  # stochastic matrix
    n = P.shape[0]
    v = np.zeros(n)
    
    for i in nodes_indexes:
        v[i] = 1 / len(nodes_indexes)  # Initialize vector v with non-zero values at personalized nodes
    
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta * P
    iterations = 0
    diff = nla.norm(q_next - q)
    
    # Power method
    while diff > 0.0001:
        iterations += 1
        q_next = np.dot(betaP, q)
        s = sum(q)
        q_next += np.transpose(np.repeat(((1 - beta)) * s, n) * v)
        q_next = q_next / sum(q_next)
        diff = nla.norm(q_next - q)
        q = q_next
        
    return q_next, iterations


# --- Q6: Choose a personalized node set and compare with regular PageRank ---

def get_indexes_by_name(names):
    return [nodes.index(name) for name in names]

# Main code to run PageRank or personalized PageRank

q1 = input("What would you like to do?\n1. Calculate PageRank\n2. Calculate personalized PageRank\n")

if int(q1) == 1:
    beta_value = float(input("Please select a beta value (between 0 and 1):\n"))
    page_ranks, iterations = page_rank(graph, beta_value)
    print(f"Number of iterations: {iterations}\n")
    top_10_visited()

elif int(q1) == 2:
    names_input = input("Enter the names of the personalized nodes, separated by spaces:\n")
    name_list = names_input.split(" ")
    page_ranks, iterations = personalized_page_rank(graph, 0.8, get_indexes_by_name(name_list))
    print(f"Number of iterations: {iterations}\n")
    top_10_visited()
