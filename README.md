<p align = "center">
  <img src = "https://github.com/StefanoLambiase/biblionet/blob/master/.github/logo_BiblioNet.png" width = "256" heigth = "256">
</p>

<p align = "center">
  📕 AI Module built for <a href="https://github.com/StefanoLambiase/biblionet">BiblioNet</a>. 📕
  <br>
  A project for
  <br>
  Fundamentals of Artificial Intelligence
  <br>
  course of Computer Science at University of Salerno.
</p>

# Project description

📕 🎓 Our module's goal is to help new subscribers find a genre to start with. We let the user answer to 5 questions with a quiz, and then our AI will suggest
genres that he could like.
We achieved this with a machine learning agent, using Python, in particular we used parameter learning with Bayesian Model.
The training dataset was built from scratch, making peopleanswer our questions with an online form.



## Documentation

Process documentation can be found in <em>documents</em> directory.
The AI module has always been in our plans for Biblionet. You can find 
documentation about requirement analysis and system design at the following 
<a href="https://github.com/StefanoLambiase/biblionet/tree/master/projectDocs/Prodotto/Documenti"><b>link</b></a>

## Authors

* **Stefano Lambiase**      - *Project Manager*   - [StefanoLambiase](https://github.com/StefanoLambiase)
* **Gianmario Voria**       - *Developer*         - [yabokk](https://github.com/yabokk)
* **Viviana Pentangelo**    - *Developer*         - [vipenti](https://github.com/vipenti)
* **Nicola Pagliara**       - *Developer*         - [Nicola-Pagliara](https://github.com/Nicola-Pagliara)


# Technical informations

In this section we introduce technical informations and installing guides!

First of all, you need to install Biblionet.
Follow the instruction at this <a href="https://github.com/StefanoLambiase/biblionet"><b>link</b></a> to install the project, but do it with this repository, 
as it contains the module.


## Running the module

We assume you have followed previous instructions and that you have a correct installation of Python on your PC.
Under the folder <em>/src/main/java/it/unisa/c07/biblionet/moduloIntelligenzaArtificiale</em> you should find a file
named "model.obj", which contains our machine learning agent already trained.
You can now run the script named "prediction.py". This will create an API running on "localhost:5000" that the application is going to
use to make predictions.

Run Biblionet, register as "Lettore", go into your user area and press on "Questionario di Supporto" button. 

