(how_to_ask_on_discourse)=
# Asking Questions on the PyMC Discourse

This document provides some advice for those asking questions on the [PyMC Discourse site](https://discourse.pymc.io/), the main channel for communication among the PyMC community.  If you have questions regarding modeling, PyMC/Aesara/arviz usage, or Bayesian modeling in general, please create a new post and someone is likely help you out.

The items in this guide are designed to help maximize the chances that you good answers quickly.

- {ref}`ask_discourse/search`
- {ref}`ask_discourse/problem`
- {ref}`ask_discourse/mwe`
- {ref}`ask_discourse/title`
- {ref}`ask_discourse/versions`
- {ref}`ask_discourse/tags`
- {ref}`ask_discourse/example`
- {ref}`ask_discourse/summary`

(ask_discourse/search)=
## Search

The PyMC Discourse is full of questions that have already received useful answers.  So definitely use the search function to see if anyone has asked questions that are similar to yours.  Try different combinations of keywords because past questions don't necessarily include {ref}`title`<a great title>.  You can also search disourse for topics by selecting relevant {ref}`tags` (or filter search results by tag).  You should also try searching {ref}`the PyMC documentation <pymc/>` because it covers both the PyMC API and common use-cases.  If you find something that is related but does not solve your specific problem, include links to these related pages and explain why the what you have found does not solve your problem.


(ask_discourse/problem)=
## State Your Problem
Describe what you are trying to accomplish, how you are trying to accomplish it, and what problem(s), if any, you are encountering.  What did you expect and what happened instead?  Give enough information so that other people know what a useful answer would look like but not more information than is necessary.  Provide information about what solutions you have tried and why they did not solve your problem.  Is it possible for someone to answer the question you have written but not provide a useful solution? (e.g., Question: Is this a bug? Answer: No.)  If so, you may need to restate your problem.

(ask_discourse/mwe)=
## Minimum Working Example
Please include an example to demonstrate the problem you are facing.  There are several critical properties of your example:

**Minimal**

Do not paste your entire script.  Only include the parts of your code/model/data/processing that are necessary to demonstrate your problem.  Do not include unnecessary import statements, unused function definitions, or code that will not be executed.

If you are currently running your code in a Jupyter notebook, export it as an executable Python script or reproduce the relevant code in a new Python script.

**Self-contained**

Anyone should be able to immediately run your example code.  This means that your example should include all import statements.  Your example should include any custom functions that are necessary.  If you code relies on data that is loaded from an external file/site, consider creating or generating toy data in your example itself:
  - `my_data = [[2, 7], [31, 9]]`
  - `mydata = np.random.default_rng(12345).random((2,2))`

If there are calls that (implicitly) rely on random seeds, explicitly set the seed
  - {func}`np.random.default_rng(12345) <numpy.random.default_rng>`
  - `pm.sample(random_seed=12345)`

**Relevant output**

This includes error messages, warnings, diagnostics, statistics, and/or plots.  Describe what about these results are relevant to your question.  What are you seeing that you **did not** expect?  What are you **not** seeing that you **did** expect?

**Your example should demonstrate your problem**

After streamlining your code down to just the essentials, make sure that you double-check that your example code still produces your problem.  If not, perhaps you accidentally solved your own problem!


(ask_discourse/title)=
## A Good Title
The title of your topic is critical because it's the first thing people will see when you submit your question.  If the question doesn't seem relevant or interesting or if people can't understand what your question might be about, then you may not get people to read and answer your question.

Highlight what you believe to be the critical aspects of your question.  Finally, if you have trouble summarizing what aspects of your problem are important, you can try waiting until you have written your entire topic, including the {ref}`mwe` before trying to write the title.

**Good titles**:
- "Why doesn't pm.sample() use all my cores?"
- "Multiprocessing BrokenPipeError: [Errno 32] Broken pipe"
- "How I get az.plot_dist() to show priors?"

**Not so good titles**:
- "How do I do Bayesian inference?"
- "Is there a better way to implement this model?"
- "Hierarchical models"


(ask_discourse/versions)=
## Versions
Please include information about what versions of the relevant packages you have installed and how they were installed, including:

- PyMC version
- Aesara version
- Python version
- System, etc. (e.g., linux, Mac, Windows, jupyter, docker, Google Colab)
- How you installed PyMC (e.g., pip, conda, mamba)


(ask_discourse/tags)
## Tags
Discourse includes two ways to classify topics: categories and tags.  Each topic belongs to exactly one category.  The most popular categories are for questions (e.g., `Questions/v4`, `Questions/v3`), but `Development` and `Sharing` are also quite popular.  Each topic may have more than one tag.  When you post your topic, search through the tags for any key words that might be relevant.  Tags include things like `bug`, `gaussian_process`, and `gpu`.

Categories and tags are an important part of how discourse functions.  Users can subscribe to categories and/or tags that are of interest.  This means that careful selection of a category and one or more tags can alert the most relevant users to your question and get you answers quicker.

```{important} Categories and tags are a critical part of how Discourse works.  Many users subscribe to categories and tags that are relevant to their own expertise.  This allows them to focus exclusively on questions that they are able to answer.  So if you post a questions under a generic category (e.g., "General") or post without any tags, your question is far less likely to attract the attention of those users most capable of answer your question!```
```

(ask_discourse/example)=
## An Example
Here is an example of a post that incorporates most of the characteristics outlined above (though not things like category and tags).  

### Starting point failure in Beta-Binomial model
I am new to PyMC and the world of Bayesian modeling.  I put together a simple coin-flipping model with a Binomial likelihood function and a Beta prior distribution.  When I run the model, the sampling seems to start, but then generates an error telling me that the starting point failed.    I tried changing the `alpha` and `beta` parameters in the Beta prior and I converted the Binomial to a Bernoulli, but none of those things seemed to help.   Here is a minimal example using the Bernoulli likelihood:

```python
import pymc as pm

my_data = 5 * [-1]

with pm.Model() as model:
    p = pm.Beta('p', alpha=1, beta=1)
    y = pm.Bernoulli('y', p=p, observed=my_data)
    idata = pm.sample()
```

Running this generates the following error:

```
SamplingError: Initial evaluation of model at starting point failed!
Starting values:
{'p_logodds__': array(0.83748875)}

Initial evaluation results:
{'p': -1.56, 'y': -inf}
```

Any ideas about what might the causing this?

PyMC version: 4.0.0\
Aesara version: 2.3.7\
Python version: 3.10.2\
Operating system: linux\
How you installed PyMC: conda


(ask_discourse/summary)=
```{admonition} Summary
- Search for information both on Discourse and in the PyMC documentation
- Precisely describe your problem
- Provide a self-contained bit of code that reproduces your problem as concisely as possible
- Use a descriptive title
- Provide information about the versions of relevant packages and the platform you are using
- Carefully select a category and one or more tags so that the right people find your question
```

