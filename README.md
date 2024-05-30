# inequality-metrics

## National income distributions
Introducing income distributions from six real countries, ranging from low to high income and low to high inequality to help us understand the full variation in measuring income inequality.

![Image: Income distributions of the United States, Sweden, Czechia, Brazil, Armenia and Nigeria](viz/real%20income%20distributions.png)


## Atkinson index and the marginal utility of income
Atkinson index's "inequality aversion parameter", E. It is equivalent to the income elasticity of the marginal utility of income, in other words how

Typically this is denoted in economics as rho. When rho is 1, the marginal utility of income is inversely proportional to income:

EQUATION

Source: [Layard et al. 2007](https://eprints.lse.ac.uk/19745/1/The_Marginal_Utility_of_Income.pdf)

The Atkinson measure used in the IHDI also sets this parameter to 1. 

But it can be set to any non-negative value, and the higher the value is, the more that inequality at lower ends of the income distribution is emphasised. We can try to intuitively understand this by relating it to the utility function of income.

![Image: Utility functions across different income elasticities](viz/utility%20across%20elasticity.png)

On the left is utility plotted against increasing income, while on the right we see the marginal utility at each level of income (in other words, it is plotting the derivative of the utility function presented in the first graph).

When rho or E is at 1, utility has a logarithmic relationship with income, and the marginal utilities are inversely proportional to income, as seen in the equation above. If we increase rho or E even further, marginal utiilty decays even more strongly, and utility "plateaus" even sooner against income. And if we set rho or E to 0, there is no decay in marginal utility over income and utility increases linearly with income.

When the Atkinson measure incorporates a value of E above 0, it is assuming that differences in incomes among poorer sections of society are more important than other differences in incomes. We can see how this bears out mathematically in the next section.

## Visualising how E responds to inequalities in different parts of the income distribution

The equation for the Atkinson measure is as follows:

This is actually equivalent to this much simpler formula:

In other words, varying the exponent 1 - e varies the generalised mean. The lower the generalised mean is than the arithmetic mean, the higher the Atkinson measure of inequality will be.

We can simply demonstrate this by plotting the generalised mean of 1 and *x* across different values of E:

![Image: Generalised means for simple two-segment distribution](viz/generalised%20mean%20simple%20dist.png)

The higher the parameter of E, the lower the generalised mean compared to the arithmetic mean (the blue line). But this is only the mean of two values and we want to understand how this "inequality aversion parameter" E responds to inequalities in a fuller income distribution.

Below, I take a distribution representing average incomes at four quartiles. For each quartile, we vary its value while keeping the rest of the distribution fixed and plot the resulting generalised mean across different values of E. The line in blue represents the **arithmetic mean** whereas the line in green represents the **geomtric mean**, which is where a logarithmic relationship between income and utility is assumed.

![Image: Generalised means for quartile-segmented distribution](viz/generalised%20mean%20quartiles%20dist.png)

A look at the first quartile (top left) compared the rest immediately shows how the Atkinson measure treats inequalities at the lower end of the distribution more severely. Recall that the distance between the arithmetic mean and the generalised mean(s) determines the level of inequality. In the first quartile, therefore, varying x creates both the most *and* the least inequality compared to any other quartile in the distribution.

In other words, making the lowest quartile particularly poor hugely affects increases the level of inequality determined across the whole income distribution. Whereas making it nearly indistinguishable to the quartile above it also makes the whole income distribution more equal than when varying any other quartile. Comparatively, adjustments to the other quartiles yield only moderate levels of inequality at any level of that quartile.

And what of the effect of E on how severely inequality is determined? In these graphs, we should focus less on the relative positions of the curves on the y-axis and more on the steepness of each individal curve to understand the effect of E. We can shed light on this artefact further by using real national income distributions.


## Effect of E on the generalised means of real income distributions

![Image: Generalised means for real national income distribution](viz/generalised%20means%20countries.png)

In this plot, we take the six income distributions introduced earlier and plot their generalised means at different levels of E. As an E of 0 yields the arithmetic mean, we can see how steeper drop-offs in the curves of certain countries must indicate stronger inequalities in the lower parts of their national income distributions. 


## Just how differently do countries rank with Gini vs. Atkinson

![Image: Gini and Atkinson scatter plot](viz/atkinson%20gini%20scatter%20plot.png)

![Image: Gini and Atkinson correlation](viz/atkinson%20gini%20correlation.png)

![Image: Income varying E correlation](viz/income%20varying%20E%20correlation.png)