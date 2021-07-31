# romanization_wrapper


romanization_wrapper is a python module for romanazing different languages into latin alphabet.

It is a wrapper of different romanization modules:


* Chinese: https://github.com/lxyu/pinyin
* Japanese: https://github.com/miurahr/pykakasi
* Korean: https://github.com/osori/korean-romanizer
* Thai:  https://github.com/PyThaiNLP/thainlp


## Usage

Create an instance with the language code.


```

from romanization_wrapper.romanizer import Romanizer

romanizer_wrapper = Romanizer("zh")
romanizer_wrapper.romanize("你好") 
# output: 'nǐhǎo'
```


```
romanizer_wrapper = Romanizer(language="ja",format="hepburn")
romanizer_wrapper.romanize("おはよう ございます") 
# output: 'ohayou gozaimasu'
```

The parameter format is optional and indicates the format of the output:
* Chinese:  diacritical | numerical | strip
* Japanese: hepburn | kunrei | passport
* Thai:  split | continue
