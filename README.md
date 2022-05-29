## Random-Forest

Leo Braiman's algorithm.  

You can follow video on my YuoTube

[![Alt text](https://img.youtube.com/vi/9dL3Uxw_Q0c/mq2.jpg)](https://www.youtube.com/watch?v=9dL3Uxw_Q0c)

It is an enssemble of Decision Trees for regression and classification problem.
The main idea is - base model should have low bias and high variance. But all trees in enssemble should not correlate to each over.
In this case enssemble will not overfit. 
Thus, the more models in enssemble the higher score.

How to eliminate correlaton between trees?
- randomly select features in their nodes while train them
- fit each trees on bootsrapped samples 

Error for classification problem (no overfitting).

![](accuracy.png)

Error for regression problem.

![](r2.png)
