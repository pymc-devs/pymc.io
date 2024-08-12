---
sd_hide_title: true
---

# Home

<center><img src="https://raw.githubusercontent.com/pymc-devs/brand/main/pymc/pymc_logos/PyMC_banner.svg" width="75%"/></center>

{doc}`PyMC <pymc:index>` is a probabilistic programming library for Python that allows users to build Bayesian models with a simple Python API and fit them using Markov chain Monte Carlo (MCMC) methods.

## Features
PyMC strives to make Bayesian modeling as simple and painless as possible, allowing users to focus on their problem rather than the methods.

Here is what sets it apart:

* **Modern**: Includes state-of-the-art inference algorithms, including MCMC (NUTS) and variational inference (ADVI).
* **User friendly**: Write your models using friendly Python syntax. [Learn Bayesian modeling](https://www.pymc.io/projects/docs/en/latest/learn.html#) from the many [example notebooks](https://www.pymc.io/projects/examples/en/latest/gallery.html).
* **Fast**: Uses {doc}`PyTensor <pytensor:index>` as its computational backend to compile through C, Numba or JAX, [run your models on the GPU](https://www.pymc-labs.io/blog-posts/pymc-stan-benchmark/), and benefit from complex graph-optimizations.
* **Batteries included**: Includes probability distributions, Gaussian processes, ABC, SMC and much more. It integrates nicely with {doc}`ArviZ <arviz:index>` for visualizations and diagnostics, as well as {doc}`Bambi <bambi:index>` for high-level mixed-effect models.
* **Community focused**: Ask questions on [discourse](https://discourse.pymc.io), join [MeetUp events](https://meetup.com/pymc-online-meetup/), follow us on [Twitter](https://twitter.com/pymc_devs), and start [contributing](https://www.pymc.io/projects/docs/en/latest/contributing/index.html).

## Example from Linear Regression

This example demonstrates how to perform Bayesian inference for a linear regression model to predict plant growth based on environmental factors.

Plant growth can be influenced by multiple factors, and understanding these relationships is crucial for optimizing agricultural practices.

```python
import pymc as pm

# Taking draws from a normal distribution
seed = 42
x_dist = pm.Normal.dist(shape=(100, 3))
x_data = pm.draw(x_dist, random_seed=seed)

# Independent Variables:
# Sunlight Hours: Number of hours the plant is exposed to sunlight daily.
# Water Amount: Daily water amount given to the plant (in milliliters).
# Soil Nitrogen Content: Percentage of nitrogen content in the soil.


# Dependent Variable:
# Plant Growth (y): Measured as the increase in plant height (in centimeters) over a certain period.


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

## Get started
* [Installation instructions](https://www.pymc.io/projects/docs/en/latest/installation.html)
* [Beginner guide (if you **do not** know Bayesian modeling)](https://www.pymc.io/projects/docs/en/latest/learn/core_notebooks/pymc_overview.html)
* [API quickstart (if you **do** know Bayesian modeling)](https://www.pymc.io/projects/examples/en/latest/introductory/api_quickstart.html)
* [Example gallery](https://www.pymc.io/projects/examples/en/latest/gallery.html)
* [Discourse help forum](https://discourse.pymc.io)

## Announcements

:::::{container} full-width
::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} PyMC forked Aesara to PyTensor
:link: pytensor_announcement
:link-type: ref
:class-header: bg-pymc-three

Release announcement
^^^
PyTensor will allow for new features such as labeled arrays, as well as speed up development and streamline the PyMC codebase and user experience.
:::


:::{grid-item-card} PyMC 4.0 is officially released!
:link: v4_announcement
:link-type: ref
:class-header: bg-pymc-three

Release announcement
^^^
PyMC 4.0 is a major rewrite of the library with many great new features while keeping the same modeling API of PyMC3.
:::

:::{grid-item-card} PyMC - Office Hours
:link: https://discourse.pymc.io/tag/office-hours
:class-header: bg-pymc-one

Event
^^^
The PyMC team has recently started hosting office hours regularly.
Subscribe on Discourse to be notified of the next event!
:::

:::{grid-item-card} Probabilistic Programming in PyMC
:link: https://austinrochford.com/posts/intro-prob-prog-pymc.html
:class-header: bg-pymc-two

Talk
^^^
Austin Rochford gave the coolest talk on Probabilistic Programming in PyMC 4.0
:::

:::{grid-item-card} Sprint testimonials
:link: sprint_testimonial
:link-type: ref
:class-header: bg-pymc-one

Blog post
^^^
Read about the recent PyMC-Data Umbrella sprint in this interview with
Sandra Meneses, one of the participants who submitted a PR
:::

::::
:::::

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

<img src="https://github.com/pymc-labs/brand/blob/main/logos/4-pymc-labs-transp-black.png?raw=true"/>

PyMC Labs offers professional consulting services for PyMC.
:::
:::{grid-item-card} Mistplay
:link: https://www.mistplay.com/

<img src="https://github.com/pymc-devs/brand/blob/main/sponsors/sponsor_logos/mistplay2_white.png?raw=true"/>

Mistplay is the world's leading Loyalty Program for mobile gamers.
:::
:::{grid-item-card} ODSC
:link: https://odsc.com/california/?utm_source=pymc&utm_medium=referral

<img src="https://github.com/pymc-devs/brand/blob/main/sponsors/sponsor_logos/odsc/odsc_blue.png?raw=true"/>

The future of AI gathers here.
:::
:::{grid-item-card} Adia Lab
:link: https://www.adialab.ae/

<img src="https://github.com/pymc-devs/brand/blob/main/sponsors/sponsor_logos/adia-lab/adia-lab-transparent.png?raw=true"/>

Dedicated to basic and applied research in data and computational sciences.
:::

::::
:::::

:::{toctree}
:hidden:

about/ecosystem
about/history
about/testimonials
:::

:::{toctree}
:hidden:
:caption: External links

Discourse <https://discourse.pymc.io>
Twitter <https://twitter.com/pymc_devs>
YouTube <https://www.youtube.com/c/PyMCDevelopers>
LinkedIn <https://www.linkedin.com/company/pymc/>
Meetup <https://www.meetup.com/pymc-online-meetup/>
GitHub <https://www.github.com/pymc-devs/pymc>
:::
