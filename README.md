# mescrappy - Python + Selenium **Youtube** scraper

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MerlinEmris/youtube_srapping_with_python">
    <img src="https://github.com/MerlinEmris/youtube_srapping_with_python/blob/master/Annotation%202021-08-17%20204528.png" alt="image" width="100%">
  </a>

  <h3 align="center"> Youtube Sraping With Python (Selenium)</h3>

  <!-- <p align="center">
    project_description
    <br />
    <a href="https://github.com/MerlinEmris/youtube_srapping_with_python"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MerlinEmris/youtube_srapping_with_python">View Demo</a>
    ·
    <a href="https://github.com/MerlinEmris/youtube_srapping_with_python/issues">Report Bug</a>
    ·
    <a href="https://github.com/MerlinEmris/youtube_srapping_with_python/issues">Request Feature</a>
  </p> -->
</p>

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#test">Test</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<!-- `merlinemris`, `youtube_srapping_with_python`, `@merlinemris96`, `merdanchariyarov@gmail.com`, `mescrap`, `Youtube video data scrapper` -->

### Built With

- [python3](https://www.python.org/)
- [selenium](https://selenium-python.readthedocs.io/)
- [chrome driver](https://chromedriver.chromium.org/downloads)
<!-- GETTING STARTED -->

## Getting Started

### Installation

1. To use this package first install it: [package](https://test.pypi.org/project/mescrappy)

`pip install mescrappy`

2. import sraper to your project

`from mescrappy.srappy import scrapper`
`scrapper.youtube_video_data_scrapper(url='', driver='')`

You can also run it directly using terminal:

`python mescrappy "https://www.youtube.com/watch?v=rMO7APyBiMI" "C:\Users\ME\projects\for_github\chromedriver_win32\chromedriver.exe"`

1'st argument is video url and 2'nd argument is browser driver location

## Usage

You can use this package to scrap youtube video's:

1. title
2. view count
3. description
4. like
5. dislike
6. post date
7. owner

EX:

`
python mescrappy "https://www.youtube.com/watch?v=rMO7APyBiMI" "C:\Users\ME\projects\for_github\chromedriver_win32\chromedriver.exe"

{

'title': 'Şeker (Cover)',

'description': 'Aýdymyň sazy : Soprano - Скорее забудь (ft. Ka-Re)\n\nLyrics:\n\nÖňler diýýärdim Aşgabat\nGerek däl başga zat\nIndi bolsa maşgalam\nGerek däl Aşgabat\n\nYanyñda oýanmak iñ uly keýp\nBaşymyz aýlanýar gerek däl meý,\nSeret! günem eýýäm günorta\nOýanmaly hiç, bulambujar otag\nBize name?! bolsun bulambujar dünýä,\nSamsyk pikirlem, şonda-da gülyäñ\n\nÝüregiñ aşagynda ýürejik urýar\nKime meñzeýärkä?, pikirlenip durýan,\nBilýäňmi näme?!, dakjak adyna Emin,\nMeñzesin ejesine, bolmasyn kemi\n\nGowy hasiyetleñ hemmesi geçmez belki,\nGeçse bolýa ejesiniñ göz reñki,\nYaşyl, öñem diýýärdim men yaşyla aşyk,\nMillet pula diýýärmikam diýýärdi, daşda...\n\nÇalyşman sizi hiç kime, \nGaraşyañ maňa giç gelsem\nUgradýañ meni ir gitsem,\nÝeke söýgimiñ biri sen,\nSöýülýänçämem diri men.\n\nDiñle! Sen meni söýýärdiñ hiçkimkäm,\nDurmuşyma geleliñ bäri men hiçkim däl.\nIşlisyraýanmy ýa çyndanam işim kän\nJaň edeýin, ýa söýýan diýmäne giçmikä?\n\nGaty seýrek hem söýmek hem söýülmek\nYüregiñ ýarysy garaşyp duranda öýüňde,\nGaýdasyñ gelýär oturan ýeriñden\nAýdasyñ gelýär oglanlara, gelenok diliñden,\nÝaýdanyp durýan, çykañok pikirden\nAýlanyp durýaň sen bedenimiñ içinde\nSaýlanyp durýar, gözelligiñ maña aýan,\nBerildi sadalyk, berildi haýa\n\nBu dünýäň oýnuny oýnasam\nMenemä ölmerin sen söýmäni goýmasañ\nGark bolman men söýgimiz meni boýlasa,\nPikire batýan sen barada oýlansam\n\nNädip saýladyñ meni hemem näme üçin,\nErbet hasiýetlem köp kemçiliklem näçe,\nBilyän, söygi şeýlerak bolaýýar nätjek\nÝüregiñ päkje özüne gatyrak çek meni\n\nJemi dört ýyldan gowrak bile eýýäm\nÖzümden gaçsamam ýene öýümize gelýän,\nHawa söýan sözi ýönekey söz däl\nSeniň ýaly tapylmaz başlasamam gözläp\n\nDaşymyzda göz kän\nÖzümede dözmän, seni bermen özgä\nYnan, muny ýazamda-da tolgunýan,\nAýlanýan ýaly depesinde tolkunlañ\n \nGerek däl bize hiçkim,\nÝyldyzlary sanamana äkideýin giçlik\nBolaly biraz işsiz\nUklap galaly asmany ýapynyp üstümize\nBir zat bor galany\n\nArzuw etmegem gowy zat\nDuýýan özümi sana zar, ýöne men azat\nGoşulmasyn duýgularymyza gazap\nAýyrmasyn biribar, degmesin nazar..\n\nDiñle! Sen meni söýýardiñ hiçkimkäm,\nDurmuşyma geleliñ bäri men hiçkim dal.\nMenema ölmerin bu söýgimiz dirika,\nDañama atdy söýýän diýmäne irmika\n\nSen men söýgülim, joram, hakyky dostum\nSen maňa hossar ýekelikden dolsam\nMeni ýumşadyañ aladalar üstüme gonsa\nSöýýän sözi ýaly gerek ýene on söz\n\nHarplar ýerini alýar, setirler dolýar\nPikirlerimi saña ýetiren bolsam bolýar,\nBar iki göz - diňe seni görýän\nBar diýjegim iki söz - Seni söýýän.\n\nBar diýjek bolanym - Seni söýýän!\nDiňe sen hakyky meni görýäň...',

'owner': 'Dali Dade',

'date': 'Premiered Jul 1, 2021',

'views': '29,392',

'like': '888',

'dislike': '5'

}`

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/MerlinEmris/youtube_srapping_with_python/issues) for a list of proposed features (and known issues).

<!-- Test -->

## Test

for testing :

`python mescrappy\test.py`

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Merdan Chariyarov - [@merlinemris96](https://twitter.com/merlinemris96) - merdanchariyarov@gmail.com

Project Link: [https://github.com/MerlinEmris/youtube_srapping_with_python](https://github.com/MerlinEmris/youtube_srapping_with_python)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [https://towardsdatascience.com/how-to-package-your-python-code-df5a7739ab2e](https://towardsdatascience.com/how-to-package-your-python-code-df5a7739ab2e)
