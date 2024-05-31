# inequality-metrics

One of the most well known ways of measuring income inequality in a population is the **Gini coefficient**. Taking values from 0 to 1, it is calculated as "the expected gap as a share of twice the mean income." In other words, if you were to find two random people on the street, what is the expected difference in their incomes (relative to the average income in that population). As such, it is a pure calculation of income distribution in a population, but it provides no information about whether that is a result of a few extreme "haves" or many "have-notes". Nor does it make any judgements about whether either type of inequality is more important.

One inequality measure that does make such judgements is the **Atkinson index**. Its best known use is in the United Nations' inequality-adjusted Human Development Index (IHDI). Also taking values from 0 to 1, its key difference is that it assumes a diminishing marginal utility of income. Thus, it actively de-emphasises inequality at the upper end of the distribution, putting more weight on differences between lower incomes. This assumption is regulated in the Atkinson by an "inequality aversion parameter", $\epsilon$. 

In this repository, we explore how the Atkinson index works, its relationship with the utility function of income, how it reacts to changes in lower parts of the income distribution compared to higher parts, and to what extent its results differ with Gini coefficients of real countries' income distributions.





## Atkinson index and the marginal utility of income

The equation for the Atkinson measure is as follows:

$$
A_\epsilon (y_1, \ldots, y_N) =
\begin{cases}
1 - \frac{1}{\mu} \left( \frac{1}{N} \sum_{i=1}^{N} y_i^{1-\epsilon} \right)^{1/(1-\epsilon)} & \text{for } 0 \leq \epsilon \neq 1 \\
1 - \frac{1}{\mu} \left( \prod_{i=1}^{N} y_i \right)^{1/N} & \text{for } \epsilon = 1 \\
1 - \frac{1}{\mu} \min (y_1, \ldots, y_N) & \text{for } \epsilon = +\infty
\end{cases}
$$

where $y_1$ is individual income $(i = 1, 2, \ldots, N)$ and  $\mu$ is the mean income.

<div style="text-align: right"> Source: <a href="https://en.wikipedia.org/wiki/Atkinson_index">Wikipedia</a>
 </div>


Atkinson index's "inequality aversion parameter", $\epsilon$. It is equivalent to the income elasticity of the marginal utility of income, in other words it is the rate at which the marginal utility of income changes as income itself changes. Typically, this is denoted in economics as $\rho$. When $\rho$ is 1, the marginal utility of income is inversely proportional to income:

$$
u =
\begin{cases}
\frac{y^{1-\rho} - 1}{1-\rho} & \rho \neq 1 \\
\log y & \rho = 1
\end{cases}
$$


<div style="text-align: right"> Source: <a href="https://eprints.lse.ac.uk/19745/1/The_Marginal_Utility_of_Income.pdf">Layard et al. 2007</a>
 </div>

The Atkinson measure used in the IHDI also sets this parameter to 1. 

But it can be set to any non-negative value, and the higher the value is, the more that inequality at lower ends of the income distribution is emphasised. We can try to intuitively understand this by relating it to the utility function of income.

![Image: Utility functions across different income elasticities](viz/utility%20across%20elasticity.png)

On the left is utility plotted against increasing income, while on the right we see the marginal utility at each level of income (in other words, it is plotting the derivative of the utility function presented in the first graph).

When rho or E is at 1, utility has a logarithmic relationship with income, and the marginal utilities are inversely proportional to income, as seen in the equation above. If we increase rho or E even further, marginal utiilty decays even more strongly, and utility "plateaus" even sooner against income. And if we set rho or E to 0, there is no decay in marginal utility over income and utility increases linearly with income.

When the Atkinson measure incorporates a value of E above 0, it is assuming that differences in incomes among poorer sections of society are more important than other differences in incomes. We can see how this bears out mathematically in the next section.

## Visualising how E responds to inequalities in different parts of the income distribution

Above, we showed the full equation to calculate the Atkinson measure. In fact, it can be understood in a much simpler form:


$$
A_\epsilon  =
1 - \frac{\text{generalised mean}^{1-\epsilon}}{\text{arithmetic mean}} $$

In other words, the Atkinson index is the complement to 1 of the ratio of the Hölder generalized mean of exponent 1−$\epsilon$ to the arithmetic mean of the incomes (where as usual the generalized mean of exponent 0 is interpreted as the geometric mean).

Thus, varying the exponent 1 - e varies the generalised mean. The lower the generalised mean is than the arithmetic mean, the higher the Atkinson measure of inequality will be.

We can simply demonstrate this by plotting the generalised mean of 1 and *x* across different values of E:

![Image: Generalised means for simple two-segment distribution](viz/generalised%20mean%20simple%20dist.png)

The higher the parameter of E, the lower the generalised mean compared to the arithmetic mean (the blue line). But this is only the mean of two values and we want to understand how this "inequality aversion parameter" E responds to inequalities in a fuller income distribution.

Below, I take a distribution representing average incomes at four quartiles. For each quartile, we vary its value while keeping the rest of the distribution fixed and plot the resulting generalised mean across different values of E. The line in blue represents the **arithmetic mean** whereas the line in green represents the **geometric mean**, which is where a logarithmic relationship between income and utility is assumed.

![Image: Generalised means for quartile-segmented distribution](viz/generalised%20mean%20quartiles%20dist.png)

A look at the first quartile (top left) compared the rest immediately shows how the Atkinson measure treats inequalities at the lower end of the distribution more severely. Recall that the distance between the arithmetic mean and the generalised mean(s) determines the level of inequality. In the first quartile, therefore, varying x creates both the most *and* the least inequality compared to any other quartile in the distribution.

In other words, making the lowest quartile particularly poor hugely affects increases the level of inequality determined across the whole income distribution. Whereas making it nearly indistinguishable to the quartile above it also makes the whole income distribution more equal than when varying any other quartile. Comparatively, adjustments to the other quartiles yield only moderate levels of inequality at any level of that quartile.

And what of the effect of E on how severely inequality is determined? In these graphs, we should focus less on the relative positions of the curves on the y-axis and more on the steepness of each individal curve to understand the effect of E. We can shed light on this artefact further by using real national income distributions.


## Effect of E on the generalised means of real income distributions

![Image: Income distributions of the United States, Sweden, Czechia, Brazil, Armenia and Nigeria](viz/real%20income%20distributions.png)
![Image: Generalised means for real national income distribution](viz/generalised%20means%20countries.png)


Here, we introduce six countries ranging from low to high income and low to high inequality to help us understand the full variation in measuring income inequality. In the left plot, we can see each country's income distribution over ten quantiles, while in the right plot, we plot the generalised means of their distributions at different levels of $\epsilon$.

Recalling that an $\epsilon$ of 0 (leftmost point on the graph) yields the arithmetic mean, and the Atkinson index is determined by the difference between the arithmetic mean and the generalised mean, we can see how that countries with steeper drop-offs in their generalised means as $\epsilon$ increases correlate with countries with more inequalities in their income distributions -- especially in the lower deciles. Namely, the United States, Brazil and Nigeria.


## How differently do countries rank with Gini vs. Atkinson


![Image: Gini and Atkinson correlation](viz/atkinson%20gini%20correlation.png)

We can see in this graph that correlation between countries ranked by Gini and by Atkinson is actually always very high, at any levels of 0 < E <= 2 (and beyond).

And in the scatter plot below, we can see that generally the rankings of the countries are the same in both sets - the key dynamics being that the average Atkinson coefficient rises as E does, and that correlation only starts to break down after E increases beyond 1.

![Image: Gini and Atkinson scatter plot](viz/atkinson%20gini%20scatter%20plot.png)

So why do may we want Atkinson over Gini?

![Image: Income varying E correlation](viz/income%20varying%20E%20correlation.png)

![Image: Gini and Atkinson quartiles](viz/gini%20vs%20atkinson%20quartiles%20dist.png)
