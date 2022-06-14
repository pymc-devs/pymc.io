(how_to_ask_on_discourse)=
# Asking Questions on the PyMC Discourse

This document provides some advice for those asking questions on the [PyMC Discourse site](https://discourse.pymc.io/), the main channel for communication among the PyMC community.  If you have questions regarding modeling, PyMC/Aesara/arviz usage, or Bayesian modeling in general, please create a new post and someone is likely help you out.

The items in this guide are designed to help maximize the chances that you good answers quickly.

- {ref}`search`
- {ref}`problem`
- {ref}`mwe`
- {ref}`title`
- {ref}`version`
- {ref}`tags`
- {ref}`example`

(search)=
## Search

The PyMC Discourse is full of questions that have already received useful answers.  So definitely use the search function to see if anyone has asked questions that are similar to yours.  Try different combinations of keywords because past questions don't necessarily include a great {ref}`title`.  If you find similar questions, but the answers do not solve your problem, include links to these past questions in your topic and explain why the answers do not solve your problem.  You can also search for topics by selecting relevant {ref}`tags` (or filter search results by tag).


(problem)=
## State Your Problem
Describe what you are trying to accomplish, how you are trying to accomplish it, and what problem(s), if any, you are encountering.  What did you expect and what happened instead?  Give enough information so that other people know what a useful answer would look like but not more information than is necessary.  Provide information about what solutions you have tried and why they did not solve your problem.  Is it possible for someone to answer the question you have written but not provide a useful solution? (e.g., Question: Is this a bug? Answer: No.)  If so, you may need to restate your problem.

(mwe)=
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
  - [`np.random.default_rng(12345)`](https://numpy.org/doc/stable/reference/random/generator.html)
  - `pm.sample(random_seed=12345)`

**Relevant output**

This includes error messages, warnings, diagnostics, statistics, and/or plots.  Describe what about these results are relevant to your question.  What are you seeing that you **did not** expect?  What are you **not** seeing that you **did** expect?

**Your example should demonstrate your problem**

After streamlining your code down to just the essentials, make sure that you double-check that your example code still produces your problem.  If not, perhaps you accidentally solved your own problem!


(title)=
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


(versions)=
## Versions
Please include information about what versions of the relevant packages you have installed and how they were installed, including:

- PyMC version
- Aesara version
- Python version
- System, etc. (e.g., linux, Mac, Windows, jupyter, docker, Google Colab)
- How you installed PyMC (e.g., pip, conda, mamba)



## Tags <a id='tags'></a>
Discourse includes two ways to classify topics: categories and tags.  Each topic belongs to exactly one category.  The most popular category is `Questions`, but `Development` and `Sharing` are also quite popular.  Each topic may have more than one tag.  When you post your topic, search through the tags for any key words that might be relevant.  Tags include things like `bug`, `gaussian_process`, and `gpu`.

Categories and tags are an important part of how discourse functions.  Users can subscribe to categories and/or tags that are of interest.  This means that careful selection of a category and one or more tags can alert the most relevant users to your question and get you answers quicker.


(example)=
### An Example
Here is an example of a post that incorporates most of the characteristics outlined above (though not things like category and tags).  

#### Starting point failure in Beta-Binomial model
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


