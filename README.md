![tpyo gif](tpyo.gif)

<br>

#### Why?

* Saw couple typos while reading a fantasy book and wondered why weren't they caught
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

$ # as of now, not using xml parser to get only relevant text
$ # so, xml related words/tags would show up
$ cat 2017-12-19_16\:04\:16.445426/tpyo_words.log 
CJK: 3
Serif: 4
tpyo: 1
xml: 8

$ # create ignore lists and run again
$ printf 'CJK\nSerif\nxml\n' > ref_words/ignore.txt
$ python3 tpyo_revealo.py
$ cat 2017-12-19_16\:06\:06.121312/tpyo_words.log 
tpyo: 1
```

<br>

#### Contributing

* Open an issue for suggestions, feature requests, bugs, etc

<br>

#### License

MIT, see [LICENSE](./LICENSE) file
