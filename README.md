# Sanctions analysis (DRAFT)

Project aims to compare influence of functions based on
[consolidated opensanctions dataset](https://www.opensanctions.org/datasets/sanctions/)
with economy factors and make comparison based on different models.

## Table of Content

## Overview

## Progression on Project Stages

1. Selecting a topic that is interesting to you
    1. Create hypnosis under test (TODO(1): disscuss with @lena and we might add/edit hypothesis)
    2. Write readme with task decomposition (TODO(1): finish readme after discussion)
    3. Decompose tasks (TODO(1): finish after discussion)
2. Collecting/finding data (TODO: partially done in "Sources" section, just refactor)
3. Cleaning data/handling missing values
4. Data analysis – attribute dependencies
5. Creating a dashboard - charts, tables, with descriptions so that you can learn more about the
   selected topic, data, etc.
6. *Deciding whether the problem is classification or regression and with the help of the sklearn library,
   selecting any model and its evaluation using accuracy or F1 score (depending on the data distribution).

## Hypothesis

Hypothesis Zero written in negative form. The main goal if this project is to proof of disproof H0 with significant
statistics difference.

1. H0: Sanctions don't impose effect on stock market prices and trade volumes of company.
2. H0: Spikes in amount of sanctions for country don't introduce negative effect on overall economy attributes:
   GDP, inflation, interest rates.
3. H0: Sections have no effect on foreign trade and its structure.
4. H0: Stock market price and trade volume can be used as estimator if company is under sanctions

## Benchmark models

1. Linear-regression
2. Classification
    1. Logistic-Regression
    2. KNN
    3. Naive Bayes
3. Decision Trees
4. Clustering
    1. K-mean
    2. Hierarchical clustering
5. TODO: Other model

## Sources

Note: some datasets are too large and needs to be downloaded manually. For example, please, refer
to [playground.py](playground.py)

1. [opensanctions](https://www.opensanctions.org/) - collection of already parsed data from global sanctions list. Bulk
   download is
   [documented](https://www.opensanctions.org/docs/bulk/) and we use 2 formats:
    1. [CSV](https://www.opensanctions.org/docs/bulk/csv/)
    2. [FollowTheMoney](https://www.opensanctions.org/docs/bulk/json/)
2. TODO: stock prices, different sources since different companies trade on different markets
3. [global trade data](https://oec.world/en/resources/bulk-download/international)

## Project Decomposition

| Task                | Description                                       | Eisenhower scores<br/>(urgency,importance) | Responsible       |
|---------------------|---------------------------------------------------|--------------------------------------------|-------------------|
| 1. Create readme.md | Description of the project must me full and clear | (10, 10)                                   | @rasskazovaleksey |

### Team

1. Astafyeva Elena
2. Rasskazov Alexey