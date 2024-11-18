# GitHub Automated Analysis

PROJECT DESCRIPTION
This project is a Python-based tool which, when given a GitHub users URL, returns the most technically complex and challenging repository from that users profile. The tool will use GPT and LangChain to assess each repository individually before determining the most technically challenging one.

Requirements:
Fetch a user’s repositories from their GitHub user URL.

Preprocess the code in repositories before passing it into GPT. Specifically, implement memory management techniques for large repositories and the files within them. Consider that repositories may contain large Jupyter notebooks or package files which, if passed raw through GPT, would greatly exceed token limits.

Implement prompt engineering when passing code through GPT for evaluation to determine its technical complexity.

Identify which of the repositories is the most technically complex. Use GPT to justify the selection of the repository.

Then, the interface should display a link to the most complex repository as well as GPT analysis justifying the selection.

Deployed to a hosting platform like Vercel, Netlify, or GitHub pages. The interface has a simple text box where users can input a GitHub user URL for analysis.