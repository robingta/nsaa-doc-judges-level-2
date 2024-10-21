**To Install Sphinx**
```
pip3 install -U sphinx
```

**Install The Theme**
```
pip3 install sphinxawesome-theme
```

```
pip3 install bs4
```

```
pip3 install sphinx_sitemap
```

```
pip3 install sphinx_design
```

```
pip3 install sphinx_docsearch
```

```
pip3 install sphinxcontrib-images
```

**Configure the Envirnment**

First install the **dotenv** for

```
pip3 install python-dotenv
```

Then make a file **.env** and copy all the contents of **.env.example** to that.



**For Autobuilding use the following command**
```
pip3 install sphinx-autobuild
```

```
sudo apt install python3-sphinx-autobuild
```

```
sphinx-autobuild ./source ./build --port 8080
```

**Finally To Export The docs**
```
make html
```