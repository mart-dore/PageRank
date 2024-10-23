# Big Data Project: PageRank

## 🎓 Project Overview

This project was developed as part of a university course with the goal of implementing the **PageRank algorithm** on Wikipedia pages. The dataset is based on the results from the **Wiki Speed Run** game, where players attempt to connect two Wikipedia pages as quickly as possible by navigating through clickable links between pages. This analysis simulates the PageRank process using these paths to rank Wikipedia pages based on their importance.

## 🚀 How to Run the Classic PageRank Program

To execute the classic PageRank algorithm, run the following command:
```bash
python projet.py
```
Make sure the file `paths_finished.csv` is in the same directory as the executable file.

## 🛠 Method Selection

When prompted, choose the desired method:
1. **PageRank Classic**
2. **Custom Method**

### 🔹 For Classic PageRank:
You will need to input the beta value (a float between [0,1]).

### 🔹 For Custom PageRank:
You will be asked to input specific page names separated by spaces. For example:
```bash
France Germany Africa
```

## 📊 Output Example

An example output for PageRank with `beta = 0.5` might look like this:

| **PAGE**          | **SCORE** |
|-------------------|------------|
| United_States     | 0.02246299 |
| Europe            | 0.01025971 |
| England           | 0.00926042 |
| United_Kingdom    | 0.00921579 |
| Africa            | 0.00584046 |
| World_War_II      | 0.00549170 |
| Earth             | 0.00464188 |
| France            | 0.00433498 |
| Germany           | 0.00411631 |

In this example, *United_States* and *Europe* are the two pages with the highest rank, meaning that they are most used to reach other pages.

## 🛠 Running the Program for Unfinished Paths

To run the program that also takes into account unfinished paths, use the following command:
```bash
python projet_path_unfinished.py
```
Ensure both `paths_finished.csv` and `paths_unfinished.csv` are in the same directory as the executable file.
