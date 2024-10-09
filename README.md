# Credit Card Transactions Fraud Detection

# Branches

I left the branches intentionally in order to navigate easily to each scenario (Data Exploration and ML Predictions)

# Dataset

The data set comprised of simulated transactions of credit cards between January 1, 2020 and December 31, 2020, including both legitimate and fraudulent transactions in the western side of the United States of America.

link: https://www.kaggle.com/datasets/kartik2112/fraud-detection

scientific paper used: https://www.sciencedirect.com/science/article/pii/S2772662223000036

# Data Exploration

These exploratory analysis only focussed on a scenario where the transaction was labelled as fraudulent.

## Category of Merchant

![alt text](/eda_images/image-1.png)

* More fraudulent activities are done in grocery stores and internet shopping.
* While fewer fraudulent activities are done in travel transactions.

![alt text](/eda_images/image.png)

* Most amount was lost shopping online.
* misc_net and shopping_pos have similar amounts lost due to fraudulent activities.
* travel has the least amount lost to fraudulent activity.

## Fraudulent vs Normal Transactions

![alt text](/eda_images/image-2.png)

![alt text](/eda_images/image-3.png)

![alt text](/eda_images/image-4.png)

* There are more normal transactions compared to fraudulent ones.
* This dataset is heavily imbalanced, with fraud cases (i.e. represented as 1) being about 0.579% and cases with not fraud (i.e. represented as 0) being 99.421%.

## Seasonality

![alt text](/eda_images/image-5.png)

![alt text](/eda_images/image-6.png)

* Not much conclusion can be drawn here besides that the fraudulent activities happened across the entire period of the dataset.

![alt text](/eda_images/image-7.png)

* Most Fraud amount was lost in first half of the year compare to the second half.
* Most Fraud Amount was lost in May and July had the least amount lost.

![alt text](/eda_images/image-8.png)

* There are periods of increase followed by periods of decrease and then a repeat.
* The 5th and 6th days of the month have the least number of fraudulent amounts.
* 12th and 20th are the days to refrain from shopping as there most number of frauds amounts then.

![alt text](/eda_images/image-9.png)

* Sunday is the day with most amount lost to fraudulent activity.
* Friday, Saturday, Sunday and Monday are the days where fraudulent activities are high. Therefore avoid shopping then.

## Target Group For Fraud

### Gender

![alt text](/eda_images/image-10.png)

* It looks the activities happens equally to both male and females although females have lost less money compared to males.

### City

![alt text](/eda_images/image-11.png)

![alt text](/eda_images/image-12.png)

* ***Phenix City, Denham Springs, Phoenix and Kilgore*** have the least number of fraudulent activities compared to other cities.
* If you are in ***Denham Springs and Phoniex City***, you are less likely to encounter fraudulent activies however if it happens you will loose very small amounts.
* ***Houston*** is a city of Frauds! The highest number of frauds are recorded there and as well as the highest amount was lost there.

### State

![alt text](/eda_images/image-14.png)

![alt text](/eda_images/image-15.png)

* HI is a state least fradulent activities and the one with least amount lost to fraud, as well.
* NY is a state with most fraudulent activities and the most amount lost to fraud.

### Jobs

![alt text](/eda_images/image-22.png)

![alt text](/eda_images/image-23.png)

* You are safe if you work as a **contractor** and **english as a second language teacher** because there are only two fraudulent activities.
* **Materials Engineers** have suffered the most. They are a target!!
* **Materials Engineers** and **Naval Architect** has lost most money!! Two careers perhaps not to consider tho they earn more money...hahaha. On a serious note, if you are an either of these two careers. You ought to be vigilant when making transaction or everywhere you are!

### Age

![alt text](/eda_images/image-24.png)

![alt text](/eda_images/image-25.png)

* Minimum age is 15 years old
* Maximum age is 95 years old
* average age is 49.6 years old
* 75% of customers are 62 years old

![alt text](/eda_images/image-26.png)

* Fraud looks to happen similarly across all the ages

![alt text](/eda_images/image-27.png)

* Customers between 45 to 55 are target while customers over the age of 85 are less target.

## Fraud Activities vs Amount 

![alt text](/eda_images/image-13.png)

* As number of fraudulent activities increases, the amount lost increases.
* Therefore if you are in Houston (where many activities are), you are most likely to lose your money due to fraud.

## Highlight Worst and Better Cities in each State

![alt text](/eda_images/image-16.png)

![alt text](/eda_images/image-17.png)

## City Population and Fraud

![alt text](/eda_images/image-18.png)

![alt text](/eda_images/image-19.png)

![alt text](/eda_images/image-20.png)

* Majority of the cities have less than 10 000 credit card customers who have experienced fraud.
* It is not conclusive that as population increase, fraud amounts and counts increases.
* However at densely populated areas, number of fraud cases are few compared to sparsely populated areas.

## Summary Stats for Amount ($)

![alt text](/eda_images/image-21.png)

* Smallest amount lost to fraud is **$ 1.06** and that has happened 471 times.
* largest amount was **$ 1 376.04** at a **shopping store (Shopping_POS)** in Queen Anne and a state of Maryland and it was a female customer.

## Is there a state or city with no fraud activities?

* Fraud was committed in all the states
* There are 192 cities where there was no fraud committed. Green cities to consider for relocation!!