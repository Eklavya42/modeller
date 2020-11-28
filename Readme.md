# Modeller

Homology Modelling using [Modeller](https://salilab.org/modeller/) 

This repository is for following [Basic Modelling](https://salilab.org/modeller/tutorial/basic.html). Model a sequence with high identity to a template.

---

## Installation and Setup

Modeller is packaged to use with the Anaconda scientific Python distribution for Windows, Linux and Mac.

Modeller is free for academic use. To obtain an academic license key, which you will need during the installation, complete the [license agreement](https://salilab.org/modeller/registration.html). The license key will be sent to you in an email from our license server. 

Use [miniconda](https://docs.conda.io/en/latest/miniconda.html) for minimal conda installation and then proceed as following:

Create a conda virtul environment:
```bash
conda create -n modeller python=3.6
```
Activate the virtual environment:
```
conda activate modeller
```

To install Modeller using the ``conda`` package manager, simply run from a command line:

```bash
conda config --add channels salilab
conda install modeller
```

You will be prompted after installation to edit a file to add your Modeller license key. Alternatively, set the KEY_MODELLER environment variable to your license key before you run 'conda install'.

Additional Requirements:

Also install `matplotlib` for plotting profiles of model and template:

```
conda install -c conda-forge matplotlib
```

Create a directory where you will be working. In this directory add the files given below in the file structure:

Initial File Structure:

```
modeller :  Main Working Directory
|
└───pdb_95.pir : Required for scripts to run 
│  
└───qseq1.ali : query/target sequence
│   
└───template1.pdb : Template-1 (known structure and sequqence similar to qseq1)
│   
└───template2.pdb : Template-2 (known structure and sequqence similar to qseq1)
│   
└───template3.pdb : Template-3 (known structure and sequqence similar to qseq1)
│   
└───script[1-6].py : Scripts for creating the model based on templates  
|
└───plot_profile.py : plotting DOPE profile of model and template
```




---

## Steps

To learn what these steps do go to : [basic modelling tutorial](https://salilab.org/modeller/tutorial/basic.html)

* Create a query (or target) sequence in the PIR format readable by the MODELLER (file : `qseq1.ali`)

```
>P1;qseq1
sequence:qseq1:::::::0.00: 0.00
CZAADKEDDPNFFKMVEGFFDRGASIVEDKLVEGLRTRQSMEQRRHRVRGILRIIKPCNHVLSVSFPIKR
DDGZWEVIEGYRAQHSHQRTPCKGGIRYSLDVSVDEVKALASLMTYKCAVVDVPFGGAKAGVKINPKNYT
DEDLEKITRRFTMELAKKGFIGPGVDVPAPNMSTGEREMSWIADTYASTIGHYDINAHACVTKPGISQGG
IHGRISATGRGLFGHIENFIENASYMSILGMTPGFGDKTFAVQGFGNVGLHSMRYLHRFGAKCVAVGEFD
GSIWNPDGIDPKELEDYKLQHGTIMGFPKAQKLEGSILETDCDILIPAASEKQLTKANAHKVKAKIIAEG
ANGPTTPQADKIFLERNIMVIPDLYLNAGGVTVSAFZZKNLNHVSYGRLTFKYERDSNYHLLMSVQESLE
RKFGKHGGTIPVVPTAEFQDRISGASEKDIVHSGLAYTMERSARQIMRTAMKYNLGLDLRTAAYVNAIEK
VFKVYNEAGLTFT*
```

* After the query/ target sequence file has been created run `script1.py` and create a log file which will store the output of the script (make sure the environment and requried packages are installed):

```bash
python script1.py > script1.log
```

* Similarly run `script2.py` and thorugh `script2.log` find the best template out of all the templates (see the [basic modelling tutorial](https://salilab.org/modeller/tutorial/basic.html) ):

```bash
python script2.py > script2.log
```

* Lets take template1.pdb as best template now run `script3.py` for aligning query/target with the template:

```bash
python script3.py > script3.log
```

* Now we build models using template, run `script4.py` (creates 5 models) and look at the output. Select the model with lowest DOPE score (see the [basic modelling tutorial](https://salilab.org/modeller/tutorial/basic.html) ):

```bash
python script4.py > script4.log
```

* After selecting the best model (say `qseq1.B99990001.pdb` ) we evaluate model using `script5.py` as well as write energy profile of model, and script6.py for writing energy profile of template:

```bash
python script5.py > script5.log
python script6.py > script6.log
```

* Use `plot_profile.py` for plotting the energy profiles of model and template and save it as dope_profile.png:

```bash
python plot_profile.py > plot_profile.log
```

Now we have `qseq1.B99990001.pdb` (best model here) based on the template (`template1.pdb` here)