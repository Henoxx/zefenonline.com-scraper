# zefenonline.com scraper

I made a simple scraper to scrap music informations from the website [zefenonline.com](http://zefenonline.com).

Although the website is somehow **old** and outdated, it has got a lot of music libraires with mp3 links.
The scraper scrapped a link for *every music available for every artist* in the site.

It's basic task is to generate a temporary json file for every artist and music scraped in case the process fail and create a final data json file after completion successfully.

My next task is to use the parsed data to create a website like [zefenonline.com](http://zefenonline.com) but in more advanced features and create a telegram bot for music lovers to easly download a vast music data.

#### Sample output
```json
[
    {
        "artist": "Abbush Zallaqaa",
        "link": "http://www.zefenonline.com/music/artist/abbush-zallaqaa/abbush-zallaqaa.html",
        "music_link": [
            "http://www.zefenonline.com/music/artist/abbush-zallaqaa/Abbush_Zallaqaa_~_+_Jordan_+_BekGeez_+_MaalooIntaloo.mp3",
            "http://www.zefenonline.com/music/artist/abbush-zallaqaa/Abbush_Zallaqaa_~_Arrooyi.mp3",
            "http://www.zefenonline.com/music/artist/abbush-zallaqaa/Abbush_Zallaqaa_~_Atiin_Nadabsaate.mp3",
            .
            .
            .
        ]
    },
    {
        "artist": "Abby Lakew",
        "link": "http://www.zefenonline.com/music/artist/abby-lakew/abby-lakew.html",
        "music_link": [
            "http://www.zefenonline.com/music/artist/abby-lakew/Abby_Lakew_~_Desta_Keremela.mp3",
            "http://www.zefenonline.com/music/artist/abby-lakew/Abby_Lakew_~_Hoden_sew_rabew.mp3",
            "http://www.zefenonline.com/music/artist/abby-lakew/Abby_Lakew_~_Libik_liben_gabizat.mp3",
            .
            .
            .
        ]
    }
]
```

> All done for educational purpose.


Aug 23, 2020



