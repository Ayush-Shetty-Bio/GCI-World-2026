# Homework 2 — Cleaning Data Using Pandas

Completed as part of the GCI World 2026 program.

> *Note:* The assignment problem, notebook structure, and dataset were provided by GCI World 2026. This repository documents my completed work and the programming and data-analysis skills I practiced through the assignment.

## Overview

This assignment focused on data cleaning and analysis using Python and Pandas.

The task involved analyzing the MyAnimeList dataset and calculating the mean Score for each anime Type, followed by sorting the results in descending order.

## Task

Using the prepared MyAnimeList dataset:

1. Group the data according to anime Type.
2. Calculate the mean Score for each type.
3. Sort the calculated means from highest to lowest.
4. Return the result as a Pandas Series.

## Concepts Practiced

- Python
- Pandas
- DataFrames
- Data cleaning
- Data manipulation
- groupby()
- Aggregation
- Mean calculation
- Sorting
- Working with numerical and categorical data

## Approach

The solution uses Pandas operations to group the dataset by the Type column, calculate the mean Score for each group, and sort the resulting values in descending order.

The core approach was:

```python
anime_data_extracted.groupby("Type")["Score"].mean().sort_values(ascending=False)
