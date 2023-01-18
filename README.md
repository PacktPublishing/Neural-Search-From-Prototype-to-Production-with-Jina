


# Neural Search - From Prototype to Production with Jina

<a href="https://www.packtpub.com/product/neural-search-from-prototype-to-production-with-jina/9781801816823?utm_source=github&utm_medium=repository&utm_campaign=9781801816823"><img src="https://static.packt-cdn.com/products/9781801816823/cover/smaller" alt="Neural Search - From Prototype to Production with Jina" height="256px" align="right"></a>

This is the code repository for [Neural Search - From Prototype to Production with Jina](https://www.packtpub.com/product/neural-search-from-prototype-to-production-with-jina/9781801816823?utm_source=github&utm_medium=repository&utm_campaign=9781801816823), published by Packt.

**Build deep learning–powered search systems that you can deploy and manage with ease**

## What is this book about?
Search is a big and ever-growing part of the tech ecosystem. Traditional search, however, has limitations that are hard to overcome because of the way it is designed. Neural search is a novel approach that uses the power of machine learning to retrieve information using vector embeddings as first-class citizens, opening up new possibilities of improving the results obtained through traditional search. 

This book covers the following exciting features:
* Understand how neural search and legacy search work
* Grasp the machine learning and math fundamentals needed for neural search
* Get to grips with the foundation of vector representation
* Explore the basic components of Jina
* Analyze search systems with different modalities
* Uncover the capabilities of Jina with the help of practical examples

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1801816824) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter06.

The code will look like the following:
```
  - name: keyValueIndexer
    uses:
      jtype: KeyValueIndexer
      metas:
        workspace: ${{ ENV.HW_WORKDIR }}
        py_modules:
          - ${{ ENV.PY_MODULE }}
    needs: segment
  - name: joinAll
    needs: [textIndexer, imageIndexer, keyValueIndexer]
```

**Following is what you need for this book:**
If you are a machine learning, deep learning, or artificial intelligence engineer interested in building a search system of any kind (text, QA, image, audio, PDF, 3D models, or others) using modern software architecture, this book is for you. This book is perfect for Python engineers who are interested in building a search system of any kind using state-of-the-art deep learning techniques.

With the following software and hardware list you can run all code files present in the book (Chapter 1-7).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-7 | Python 3.7, JINA 3.7, DocArray 0.13 | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/minUU).

### Related products
* Machine Learning on Kubernetes [[Packt]](https://www.packtpub.com/product/machine-learning-on-kubernetes/9781803241807?utm_source=github&utm_medium=repository&utm_campaign=9781803241807) [[Amazon]](https://www.amazon.com/dp/1803241802)

* Practical Deep Learning at Scale with MLflow [[Packt]](https://www.packtpub.com/product/practical-deep-learning-at-scale-with-mlflow/9781803241333?utm_source=github&utm_medium=repository&utm_campaign=9781803241333) [[Amazon]](https://www.amazon.com/dp/1803241330)

## Get to know the authors
**Bo Wang**
 is a machine learning engineer at Jina AI. He has a background in computer science, especially interested in the field of information retrieval. In the past years, he has been conducting research and engineering work on search intent classification, search result diversification, content-based image retrieval, and neural information retrieval. At Jina AI, Bo is working on developing a platform for automatically improving search quality with deep learning. In his spare time, he likes to play with his cats, watch anime, and play mobile games.

**Cristian Mitroi**
 is a machine learning engineer with a wide breadth of experience in full stack, from infrastructure to model iteration and deployment. His background is based in linguistics, which led to him focusing on NLP. He also enjoys, and has experience in, teaching and interacting with the community, and has given workshops at various events. In his spare time, he performs improv comedy and organizes too many pen-and-paper role-playing games.

**Feng Wang**
 is a machine learning engineer at Jina AI. He received his Ph.D. from the department of computer science at the Hong Kong Baptist University in 2018. He has been a full-time R&D engineer for the past few years, and his interests include data mining and artificial intelligence, with a particular focus on natural language processing, multi-modal representation learning, and recommender systems. In his spare time, he likes climbing, hiking, and playing mobile games.

**Shubham Saboo**
 has taken on multiple roles, from a data scientist to an AI evangelist, at renowned firms across the globe, where he was involved in building organization-wide data strategies and technology infrastructure to create and scale data teams from scratch. His work as an AI evangelist has led him to build communities and reach out to a broader audience to foster the exchange of ideas and thoughts in the burgeoning field of AI. As part of his passion for learning new things and sharing knowledge with the community, he writes technical blogs on the advancements in AI and its economic implications. In his spare time, you can find him traveling the world, which enables him to immerse himself in different cultures and refine his worldview.

**Susana Guzmán**
 is the product manager at Jina AI. She has a background in computer science and for several years was working at different firms as a software developer with a focus on computer vision, working with both C++ and Python. She has a big interest in open source, which was what led her to Jina, where she started as a software engineer for 1 year until she got a clear overview of the product, which made her make the switch from engineering to PM. In her spare time, she likes to cook food from different cuisines around the world, looking for her new favorite dish.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801816823">https://packt.link/free-ebook/9781801816823 </a> </p>