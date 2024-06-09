# inequality-metrics

![Image: Income distributions of the United States, Sweden, Czechia, Brazil, Armenia and Nigeria](viz/real%20income%20distributions.png)

There are many ways of measuring inequality in an income distribution. One of the best known ways is the **Gini coefficient**. Taking values from 0 to 1, it is calculated as "the expected gap as a share of twice the mean income." In other words, if you were to find two random people on the street, what is the expected difference in their incomes (relative to the average income in that population)? This is a pure calculation of the distribution of income in a population, but provides no information about whether that inequality is a result of a few extreme "haves", or of many "have-nots". Nor does it make any judgements about whether either type of inequality is more important.

One inequality measure that does make such judgements is the **Atkinson index**. Its best known use is in the United Nations' inequality-adjusted Human Development Index (IHDI). Also taking values from 0 to 1, the Atkinson index's key difference is that it assumes a diminishing marginal utility of income. Thus, it actively de-emphasises inequality at the upper end of the distribution, putting more weight on differences between lower incomes. This assumption is regulated in the Atkinson by an "inequality aversion parameter", $\epsilon$. 

In this repository, we explore how the Atkinson index works, its relationship to the utility function of income, how it reacts to changes in lower parts of the income distribution compared to higher parts and to what extent its results differ with Gini coefficients of real countries' income distributions.





## Atkinson index and the marginal utility of income

The equation for the Atkinson index is as follows:

$$
A_\epsilon (y_1, \ldots, y_N) =
\begin{cases}
1 - \frac{1}{\mu} \left( \frac{1}{N} \sum_{i=1}^{N} y_i^{1-\epsilon} \right)^{1/(1-\epsilon)} & \text{for } 0 \leq \epsilon \neq 1 \\
1 - \frac{1}{\mu} \left( \prod_{i=1}^{N} y_i \right)^{1/N} & \text{for } \epsilon = 1 \\
1 - \frac{1}{\mu} \min (y_1, \ldots, y_N) & \text{for } \epsilon = +\infty
\end{cases}
$$

where $y_i$ is individual income $(i = 1, 2, \ldots, N)$ and  $\mu$ is the mean income.

$\epsilon$ represents the "**inequality aversion parameter**". It is equivalent to the income elasticity of the marginal utility of income, in other words it is the rate at which the marginal utility of income changes as income itself changes. In economics, this same parameter is typically denoted as $\rho$. Under the standard theory of the diminshing marginal utility of income, additional increases in utility diminish as income increases. The higher $\rho$ is, the stronger that decay in marginal utility becomes:

$$
u =
\begin{cases}
\frac{y^{1-\rho} - 1}{1-\rho} & \rho \neq 1 \\
\log y & \rho = 1
\end{cases}
$$

Let's visualise this by plotting the utility function of income (left), and its derivative, the marginal utility of income (right):


![Image: Utility functions across different income elasticities](viz/utility%20across%20elasticity.png)

With increasing values of $\rho$, and thus $\epsilon$, we can see how marginal utility decays even more strongly and utility plateaus even sooner. Therefore, when applied to the context of measuring inequality and the Atkinson index, higher values of $\epsilon$ assume that differences in incomes among poorer sections of society are more important than other differences among higher incomes. 

Let's see how this all works empirically when applied to income distributions of different shapes.

## Visualising how E responds to inequalities in different parts of the income distribution

Earlier, we wrote the full equation to calculate the Atkinson measure. In fact, it can be understood in a much simpler form:

$$
A_\epsilon  =
1 - \frac{\text{generalised mean}^{1-\epsilon}}{\text{arithmetic mean}} $$

In other words, the Atkinson index is the complement to 1 of the ratio of the Hölder generalized mean of exponent $1 − \epsilon$ to the arithmetic mean of the incomes (where the generalized mean of exponent $0$ is equivalent to the geometric mean). So, varying the exponent $1 - \epsilon$ varies the generalised mean. The IHDI sets $\epsilon$ to 1, which sets the generalised mean to the geometric mean and, returning to the utility function, assumes a logarithmic relationship between utility and income.

The lower the generalised mean is from the arithmetic mean, the higher the Atkinson measure of inequality will be.

We can demonstrate this dynamic by taking a simple distribution and plotting its **arithmetic mean** (blue, $\epsilon = 0$) against its various **generalised means** (coloured lines, $\epsilon > 0$). From this, we interpret inequality as the distance between those two lines. 

Let's take a simple, ordered array of four values, $[2, 4, 6, 8]$, to represent quartiles of an income distribution. For each quartile, we vary its value $x$ and see what effect it has on the generalised means of the distribution:

![Image: Generalised means for quartile-segmented distribution](viz/generalised%20mean%20quartiles%20dist.png)

At higher positive values of $\epsilon$, the lower the generalised mean of the distribution generally is compared to the arithmetic mean. But this effect is different when $x$ is varied at different quartiles.

A look at the first quartile (top left) compared to the rest of the quartiles immediately shows how the Atkinson index treats inequalities at the lower end of the distribution more severely. Recall that the distance between the arithmetic mean and the generalised mean(s) determines the level of inequality. In the first quartile, varying $x$ from low to high yields both the most *and* the least inequality compared to any other quartile in the distribution.

In other words, making the lowest quartile particularly poor hugely affects increases the level of inequality determined across the whole income distribution. Whereas bringing it closer to the middle incomes makes the whole income distribution more equal than when varying any other quartile. Comparatively, adjustments to the other quartiles yield only moderate levels of inequality at any level of that quartile.

And what of the effect of $\epsilon$ on how severely inequality is determined? We can see that for higher values of $\epsilon$, the gap between the arithmetic mean and the generalised mean increases. But also, the curve rises later when $\epsilon$ is higher, exhibiting greater sensitivity to inequalities at lower incomes. We can shed light on this dynamic further by testing the effects of $\epsilon$ on real national income distributions.


## Effect of $\epsilon$ on the generalised means of real income distributions

![Image: Income distributions of the United States, Sweden, Czechia, Brazil, Armenia and Nigeria](viz/real%20income%20distributions.png)
![Image: Generalised means for real national income distribution](viz/generalised%20means%20countries.png)


Here, we introduce six countries all with different combinations of income and inequality levels, to help us understand the full variation in measuring income inequality. In the left plot, we can see each country's income distribution over ten deciles, while in the right plot, we plot the generalised means of their distributions at different levels of the inequality aversion parameter, $\epsilon$.

Recalling that an $\epsilon$ of 0 (leftmost point on the graph) yields the arithmetic mean, and that the Atkinson index is determined by the difference between the arithmetic mean and the generalised mean, we can see how countries with more inequalities in their income distributions (especially in the lower deciles), like the United States, Brazil and Nigeria, have steeper drop-offs in their curves. On the other hand, Sweden, the Czech Republic and Armenia (all countries with drastically different income per capita levels but similarly flat income distributions) correspondingly have flatter curves on the right graph.


## How differently do Gini and Atkinson treat the same distribution?

Recall that Gini is insensitive to inequalities in specific parts of the income distribution. Rather, it interprets inequality in the population holistically. Returning to the simple, quartile-based distributions we introduced earlier, we can observe how the Atkinson index and Gini coefficient differ when measuring the same distribution:

![Image: Gini and Atkinson quartiles](viz/gini%20vs%20atkinson%20quartiles%20dist.png)

When varying the second to fourth quartiles, the Gini and Atkinson measures yield similar slopes. However, looking at the first quartile, again we see how dramatically the Atkinson measure varies across different values of $x$. When $x$ is low enough here (representing extreme inequality amongst the poorest), the Atkinson index actually exceeds the Gini coefficient - the only situation in which it does that.

## Exploring Atkinson inequalities of European countries in more detail

Having gained a more intuitive understanding of how the Atkinson measure reacts to different types of income distributions, let's explore one of its most notable applications - the inequality-adjusted Human Development Index - in more detail. 

Check out [**this repository**](https://github.com/tigran-sog/clustering-europe) where I decompose the index into its Human Development score and its Atkinson measure and use *k*-means clustering to categorise European countries based on their societal development and their inequality.

![Image: European countries by human development and inequality](viz/plot%20k4.png)
