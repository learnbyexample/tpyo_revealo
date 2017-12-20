![tpyo gif](tpyo.gif)

<br>

#### Why?

* Saw couple of typos while reading a fantasy book and wondered why weren't they caught
* Felt like a good mini-project to improve my Python and programming skills

<br>

#### Idea

1. Compare list of dictionary words with words extracted from e-book using Python code
    * as of now, working on docx/epub formats
2. The output generated has to be manually checked to validate
    * in-world terms like names, places, etc
    * words not found in reference dictionary
    * hyphenated words
3. These words can then be added to reference list of words so that further runs will reveal only typos
4. Repeat steps 1-3 when input documents change

<br>

#### Caveats

* Use the program at your own risk
    * files/directories are read/created programmatically, bug could corrupt your system
    * I only have Linux, so don't know how it'll behave when used with other operating systems
* at best, project could be said to be at alpha stage

<br>

#### Instructions

For Linux and Unix-like systems

First, clone the repo or download the [zip](https://github.com/learnbyexample/tpyo_revealo/archive/master.zip)

```bash
$ git clone https://github.com/learnbyexample/tpyo_revealo.git

$ cd tpyo_revealo/
$ mkdir ref_words input_doc
$ # multiple documents and reference lists can be put in these directories
$ cp samples/sample.docx input_doc/
$ cp /usr/share/dict/words ref_words/words.txt

$ # this will create a log directory using current time as directory name
$ python3 tpyo_revealo.py

$ cat 2017-12-20_15_38_07.341621/hyphenated_words.log
en-IN: 1
full-fledged: 1
$ cat 2017-12-20_15_38_07.341621/tpyo_words.log
LibreOffice/5.2.0.4$Linux_X: 1
LibreOffice_project/20m0$Build: 1
rny: 1
T12:10:00Z: 1
T16:21:07Z: 1
tpyo: 1
wordswithoutspace: 1

$ # create ignore lists and run again
$ cat > ref_words/ignore.txt
en-IN
LibreOffice/5.2.0.4$Linux_X
LibreOffice_project/20m0$Build
T12:10:00Z
T16:21:07Z
$ echo 'full-fledged' > ref_words/hyphenated_words.txt

$ python3 tpyo_revealo.py
$ cat 2017-12-20_15_40_45.505735/hyphenated_words.log
$ cat 2017-12-20_15_40_45.505735/tpyo_words.log
rny: 1
tpyo: 1
wordswithoutspace: 1
```

<br>

#### Where to get word lists

* this [stackoverflow Q&A](https://stackoverflow.com/questions/4456446/dictionary-text-file) might help
* [aspell](http://app.aspell.net/create) looked good (mentioned in above link)
    * American/British/Canadian/Australian spellings
    * SCOWL size 95, Variants 3, Diacritic stripped gives 660+K words
        * The script finished in less than 3 seconds for Oathbringer book(450+K words) against 660+K reference words, so performance not an issue
    * Can be downloaded for both Windows/Unix
    * See [scowl-readme](http://wordlist.aspell.net/scowl-readme/) for more details including usage and license

<br>

#### Wishlist

* Better parsing for xhtml files. As of now xml extraction is used, so things like `T<span class="XXX">HOSE words` messes up things
* Code organization - need to break up into different functions, etc
* Features - repeated words, adverbs repeated in short space, etc
* Look into NLTK

<br>

#### Contributing

* Open an issue for suggestions, feature requests, bugs, etc

<br>

#### License

MIT, see [LICENSE](./LICENSE) file
