The null hypothesis is that the coin is fair, and the alternative hypothesis is that the coin is biased: biased towards tails _(note that this a one-sided test):_

$H_0 : p_0 = 0.5$

$H_1 : p_0 < 0.5$

Since the sample size here is 10, we cannot apply the Central Limit Theorem and so cannot approximate a binomial using a normal distribution.

The p-value here is the probability of observing results as extreme as, or more extreme than, those actually observed given that the null hypothesis is true, i.e., under the assumption that the coin fair. For 10 flips of a coin, there are $2^{10} = 1024$ possible outcomes, only 10 of which yield 9 tails and one heads, and one outcome which yields 10 tails and no heads.

In a one-sided test like this, where we're testing if the coin is biased towards tails, it's not just about how often we see the specific outcome of 9 tails and 1 head; it's also about capturing all outcomes that are at least as extreme as this. The scenario of getting 10 tails in 10 flips is included because it represents an even more extreme case of the coin showing a bias towards tails. This inclusion is vital to fully assess the strength of the evidence against the null hypothesis. By considering both the exact result of 9 tails and the more extreme result of 10 tails, we ensure a comprehensive evaluation of all possible outcomes that would support the alternative hypothesis, thereby providing a more accurate measure of the p-value.

Hence, the exact probability of the given result is the p-value, which is $10/1024 + 1/1024= 0.0107$. Therefore, we can reject the null hypothesis at a 0.05 significance level, since 0.0107 < 0.05, and accept the alternative hypothesis that the coin is not fair and biased towards tails.
