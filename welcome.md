---
html_theme.sidebar_secondary.remove:
sd_hide_title: true
---

<!-- CSS overrides on the homepage only -->
<style>
.bd-main .bd-content .bd-article-container {
  max-width: 85rem; /* Make homepage a little wider instead of 60em */
}
/* Extra top/bottom padding to the sections */
article.bd-article section section {
  padding: 3rem 0 7rem;
}
article.bd-article section section section {
  padding: 0;
}

/* Override all h1 headers except for the hidden ones */
h1:not(.sd-d-none) {
  font-weight: bold;
  font-size: 48px;
  text-align: center;
  margin-bottom: 4rem;
}
/* Override all h3 headers that are not in hero */
h2:not(#hero h2) {
  border-bottom: 2px solid #e6e7e5;
  padding-bottom: .5rem;
}
/* Remove breadcrumbs element */
.bd-header-article {
  visibility: hidden;
  height: 0pt;
}
</style>

# Home

<div id="hero">
<div id="hero-left">
  <h2 style="font-size: 58px; font-weight: bold; margin: 2rem auto 0;">Probabilistic modeling at your fingertips</h2>

<div class="homepage-button-container">
  <div class="homepage-button-container-row">
      <a href="https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/pymc_overview.html" class="homepage-button primary-button">Get Started</a>
      <a href="https://www.pymc.io/project/examples/en/latest/gallery.html" class="homepage-button secondary-button">See Examples</a>
  </div>
  <div class="homepage-button-container-row">
      <a href="https://www.pymc.io/project/docs/en/stable/api.html" class="homepage-button-link">See API Reference →</a>
  </div>
</div>
</div>
</div> 


<div style="display: flex; max-width: 55rem; margin: auto;">
<h3 style="font-size: 36px; font-weight: normal; text-align: center;">
PyMC is a probabilistic programming library for Python that allows users to build Bayesian models with a simple API. It features multiple inference algorithms, forward sampling, and model updates or interventions.
</h3>
</div>


## Built for insight

:::::{grid} 1 2 3 3

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`data_exploration`
:::
:::{grid-item}
:class: key-features-name

Modern
:::
:::{grid-item}
:class: key-features-body

Includes state-of-the-art inference algorithms, including MCMC (NUTS) and variational inference (ADVI).
:::
::::

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`how_to_reg`
:::
:::{grid-item}
:class: key-features-name

User-friendly
:::
:::{grid-item}
:class: key-features-body

Write your models using friendly Python syntax. [Learn Bayesian modeling](https://www.pymc.io/projects/docs/en/latest/learn.html#) from the many [example notebooks](https://www.pymc.io/projects/examples/en/latest/gallery.html).
:::
::::

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`speed`
:::
:::{grid-item}
:class: key-features-name

Fast
:::
:::{grid-item}
:class: key-features-body

 Uses {doc}`PyTensor <pytensor:index>` as its computational backend to compile through C, Numba or JAX, [run your models on the GPU](https://www.pymc-labs.io/blog-posts/pymc-stan-benchmark/), and benefit from complex graph-optimizations.
:::
::::

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`battery_saver`
:::
:::{grid-item}
:class: key-features-name

Batteries included
:::
:::{grid-item}
:class: key-features-body

Includes probability distributions, Gaussian processes, ABC, SMC and much more. It integrates nicely with {doc}`ArviZ <arviz:index>` for visualizations and diagnostics, as well as [Bambi](https://bambinos.github.io/bambi/) for high-level mixed-effect models.
:::
::::

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`alt_route`
:::
:::{grid-item}
:class: key-features-name

Hackable
:::
:::{grid-item}
:class: key-features-body

Allows updates and interventions to both data and model; supporting predictions, forecasts, counterfactuals, or analysis of user interventions on model inputs.
:::
::::

::::{grid} 1
:::{grid-item}
:class: key-features-icon

{material-twotone}`diversity_3`
:::
:::{grid-item}
:class: key-features-name

Community focused
:::
:::{grid-item}
:class: key-features-body

Ask questions on [discourse](https://discourse.pymc.io), join [MeetUp events](https://meetup.com/pymc-online-meetup/), follow us on [Twitter](https://twitter.com/pymc_devs), and start [contributing](https://www.pymc.io/projects/docs/en/latest/contributing/index.html).
:::
::::

:::::


## Ecosystem

### General purpose

<div style="max-width: 60rem;">

- [Bambi](https://github.com/bambinos/bambi): BAyesian Model-Building Interface (BAMBI) in Python.
- [PyMC-BART](https://www.pymc.io/projects/bart/en/latest/): Bayesian Additive Regression Trees for Probabilistic programming with PyMC
- [PyMC-Extras](https://github.com/pymc-devs/pymc-extras): A collection of PyMC extra features such as cutting-edge methodologies, highly specialized statistical distributions, or complex models appear.
- [calibr8](https://github.com/JuBiotech/calibr8): A toolbox for constructing detailed observation models to be used as likelihoods in PyMC.
- [CausalPy](https://github.com/pymc-labs/CausalPy): A package focussing on causal inference in quasi-experimental settings.
- [SunODE](https://github.com/pymc-devs/sunode): Fast ODE solver, much faster than the one that comes with PyMC.
- [pymc-learn](https://github.com/pymc-learn/pymc-learn): Custom PyMC models built on top of pymc3_models/scikit-learn API
- [BART-Survival](https://github.com/CDCgov/BART-Survival): BART-Survival is a Python package that supports discrete-time Survival analyses using the non-parametric machine learning algorithm, Bayesian Additive Regression Trees (BART).

</div>

### Domain specific

<div style="max-width: 60rem;">

- [PyMC-Marketing](https://www.pymc-marketing.io/en/stable/): Marketing analytic tools like Marketing Mix Modeling (MMM) or Customer Lifetime Value (CLV)
- [Exoplanet](https://github.com/dfm/exoplanet): a toolkit for modeling of transit and/or radial velocity observations of exoplanets and other astronomical time series.
- [beat](https://github.com/hvasbath/beat): Bayesian Earthquake Analysis Tool.

</div>

More about the {doc}`about/ecosystem`


## Example from Linear Regression

This example demonstrates how to perform Bayesian inference for a linear regression model to predict plant growth based on environmental factors.

Plant growth can be influenced by multiple factors, and understanding these relationships is crucial for optimizing agricultural practices.

Independent Variables:
- Sunlight Hours: Number of hours the plant is exposed to sunlight daily.
- Water Amount: Daily water amount given to the plant (in milliliters).
- Soil Nitrogen Content: Percentage of nitrogen content in the soil.

Dependent Variable:
- Plant Growth (y): Measured as the increase in plant height (in centimeters) over a certain period.

```python
import pymc as pm

# Taking draws from a normal distribution
seed = 42
x_dist = pm.Normal.dist(shape=(100, 3))
x_data = pm.draw(x_dist, random_seed=seed)

# Define coordinate values for all dimensions of the data
coords={
 "trial": range(100),
 "features": ["sunlight hours", "water amount", "soil nitrogen"],
}

# Define generative model
with pm.Model(coords=coords) as generative_model:
   x = pm.Data("x", x_data, dims=["trial", "features"])

   # Model parameters
   betas = pm.Normal("betas", dims="features")
   sigma = pm.HalfNormal("sigma")

   # Linear model
   mu = x @ betas

   # Likelihood
   # Assuming we measure deviation of each plant from baseline
   plant_growth = pm.Normal("plant growth", mu, sigma, dims="trial")


# Generating data from model by fixing parameters
fixed_parameters = {
 "betas": [5, 20, 2],
 "sigma": 0.5,
}
with pm.do(generative_model, fixed_parameters) as synthetic_model:
   idata = pm.sample_prior_predictive(random_seed=seed) # Sample from prior predictive distribution.
   synthetic_y = idata.prior["plant growth"].sel(draw=0, chain=0)


# Infer parameters conditioned on observed data
with pm.observe(generative_model, {"plant growth": synthetic_y}) as inference_model:
   idata = pm.sample(random_seed=seed)

   summary = pm.stats.summary(idata, var_names=["betas", "sigma"])
   print(summary)
```
From the summary, we can see that the mean of the inferred parameters are very close to the fixed parameters

| Params                  | mean  |  sd  | hdi_3% | hdi_97% | mcse_mean | mcse_sd | ess_bulk | ess_tail | r_hat |
|-------------------------|-------|------|--------|---------|-----------|---------|----------|----------|-------|
| betas[sunlight hours]   | 4.972 | 0.054 | 4.866 | 5.066 | 0.001 | 0.001 | 3003 | 1257 | 1 |
| betas[water amount]     | 19.963 | 0.051 | 19.872 | 20.062 | 0.001 | 0.001 | 3112 | 1658 | 1 |
| betas[soil nitrogen]    | 1.994 | 0.055 | 1.899 | 2.107 | 0.001 | 0.001 | 3221 | 1559 | 1 |
| sigma                   | 0.511 | 0.037 | 0.438 | 0.575 | 0.001 | 0 | 2945 | 1522 | 1 |

```python
# Simulate new data conditioned on inferred parameters
new_x_data = pm.draw(
    pm.Normal.dist(shape=(3, 3)),
    random_seed=seed,
)
new_coords = coords | {"trial": [0, 1, 2]}

with inference_model:
    pm.set_data({"x": new_x_data}, coords=new_coords)
    pm.sample_posterior_predictive(
        idata,
        predictions=True,
        extend_inferencedata=True,
        random_seed=seed,
    )

pm.stats.summary(idata.predictions, kind="stats")
```
The new data conditioned on inferred parameters would look like:

| Output            | mean  |  sd  | hdi_3% | hdi_97% |
|-------------------|-------|------|--------|---------|
| plant growth[0]   | 14.229 | 0.515 | 13.325 | 15.272 |
| plant growth[1]   | 24.418 | 0.511 | 23.428 | 25.326 |
| plant growth[2]   | -6.747 | 0.511 | -7.740 | -5.797 |

```python
# Simulate new data, under a scenario where the first beta is zero
with pm.do(
    inference_model,
    {inference_model["betas"]: inference_model["betas"] * [0, 1, 1]},
) as plant_growth_model:
    new_predictions = pm.sample_posterior_predictive(
        idata,
        predictions=True,
        random_seed=seed,
    )

pm.stats.summary(new_predictions, kind="stats")
```
The new data, under the above scenario would look like:

| Output            | mean  |  sd  | hdi_3% | hdi_97% |
|-------------------|-------|------|--------|---------|
| plant growth[0]   | 12.149 | 0.515 | 11.193 | 13.135 |
| plant growth[1]   | 29.809 | 0.508 | 28.832 | 30.717 |
| plant growth[2]   | -0.131 | 0.507 | -1.121 | 0.791 |


## Sponsors
:::::{container} full-width
::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card} NumFOCUS
:link: https://numfocus.org

<img src="https://www.numfocus.org/wp-content/uploads/2017/03/1457562110.png"/>

NumFOCUS is our non-profit umbrella organization.
:::

:::{grid-item-card} PyMC Labs
:link: https://pymc-labs.io

<img src="https://raw.githubusercontent.com/pymc-devs/brand/refs/heads/main/sponsors/sponsor_logos/pymc_labs.png"/>

PyMC Labs offers professional consulting services for PyMC.
:::

:::{grid-item-card} Open Wound Research
:link: https://www.openwoundresearch.com/

<img src="_static/sponsors_logo/OWR.svg"/>

A novel wound-care research organization committed to advancing actionable wound care research.
:::

::::
:::::

More about PyMC's {doc}`about/sponsors`


:::{toctree}
:hidden:

about/ecosystem
about/history
about/sponsors
about/testimonials
:::
